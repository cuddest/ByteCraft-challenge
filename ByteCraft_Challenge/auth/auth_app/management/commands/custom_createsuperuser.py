from django.contrib.auth.management.commands import createsuperuser
from auth_app.models import customuser as CustomUser


class Command(createsuperuser.Command):
    help = "Create a superuser account."

    def handle(self, *args, **options):
        username = options["username"]
        email = options["email"]
        password = options["password"]
        database = options["database"]

        User = CustomUser  # Use your custom user model

        try:
            User.objects.db_manager(database).get(email=email)
        except User.DoesNotExist:
            User.objects.db_manager(database).create_superuser(
                username=username, email=email, password=password
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
        else:
            self.stderr.write(
                self.style.ERROR("Error: This email already has an account.")
            )
