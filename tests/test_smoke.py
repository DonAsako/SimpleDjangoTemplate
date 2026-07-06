"""Smoke tests — confirm the project is wired together and boots."""

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command


def test_system_check_passes() -> None:
    """manage.py check finds no issues with the loaded settings."""
    call_command('check')


def test_custom_user_model_is_wired() -> None:
    assert settings.AUTH_USER_MODEL == 'accounts.User'


@pytest.mark.django_db
def test_can_create_user() -> None:
    user_model = get_user_model()
    user = user_model.objects.create_user(username='alice', password='s3cret-pw!')
    assert user.pk is not None
    assert user.check_password('s3cret-pw!')


@pytest.mark.django_db
def test_can_create_superuser() -> None:
    user_model = get_user_model()
    admin = user_model.objects.create_superuser(username='root', password='s3cret-pw!')
    assert admin.is_staff
    assert admin.is_superuser
