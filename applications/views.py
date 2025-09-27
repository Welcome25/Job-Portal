from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobs.models import Job
from .models import Application
from .forms import ApplicationForm

@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if Application.objects.filter(applicant=request.user, job=job).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('jobs:job_detail', pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.job = job
            application.save()
            messages.success(request, 'Your application has been submitted.')
            return redirect('applications:my_applications')
    else:
        form = ApplicationForm()
    return render(request, 'applications/apply.html', {'form': form, 'job': job})

@login_required
def my_applications(request):
    applications = Application.objects.filter(applicant=request.user).select_related('job')
    return render(request, 'applications/my_applications.html', {'applications': applications})

@login_required
def application_detail(request, pk):
    application = get_object_or_404(Application, pk=pk, applicant=request.user)
    return render(request, 'applications/application_detail.html', {'application': application})
