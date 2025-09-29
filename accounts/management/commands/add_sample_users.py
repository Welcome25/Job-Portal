from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Add sample users to the database'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        sample_users = [
            {
                'username': 'employer1',
                'email': 'employer1@example.com',
                'first_name': 'sri',
                'last_name': 'ram',
                'user_type': 'employer',
                'company': 'Tech Corp',
                'phone': '1234567890',
            },
            {
                'username': 'jobseeker1',
                'email': 'jobseeker1@example.com',
                'first_name': 'iswarya',
                'last_name': 'vasan',
                'user_type': 'jobseeker',
                'phone': '0987654321',
            },
        ]

        for user_data in sample_users:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults=user_data
            )
            if created:
                user.set_password('password123')  # Set a default password
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Created user: {user.username}"))
            else:
                self.stdout.write(f"User already exists: {user.username}")

