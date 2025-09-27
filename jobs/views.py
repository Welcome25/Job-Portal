from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm
from django.db.models import Q

def job_list(request):
    query = request.GET.get('q')
    employment_type = request.GET.get('employment_type')
    location = request.GET.get('location')

    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(company__icontains=query)
        )
    if employment_type:
        jobs = jobs.filter(employment_type=employment_type)
    if location:
        jobs = jobs.filter(location__icontains=location)

    context = {
        'jobs': jobs,
        'query': query or '',
        'employment_type': employment_type or '',
        'location': location or '',
    }
    return render(request, 'jobs/job_list.html', context)

@login_required
def job_post(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('jobs:job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/job_post.html', {'form': form})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})
