from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model.

    Wired via AUTH_USER_MODEL = 'accounts.User'. It subclasses
    AbstractUser so it behaves exactly like the default Django user out of
    the box — add your own fields, properties and methods here as the project
    grows. Having it from day one avoids the painful migration of swapping the
    user model later.
    """
