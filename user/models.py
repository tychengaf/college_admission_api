from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.constants import UserType
from util.db.models import TimeStampedModel


class UserQuerySet(models.QuerySet):
    def admins(self):
        return self.filter(type='admins')

    def students(self):
        return self.filter(type='students')

    def staffs(self):
        return self.filter(type='staffs')


class UserManager(DjangoUserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def create_admin(
        self, username, email=None, password=None, **extra_fields
    ):
        extra_fields['type'] = UserType.ADMIN.value
        return self.create_superuser(username, email, password, **extra_fields)

    def create_student(
        self, username, email=None, password=None, **extra_fields
    ):
        extra_fields['type'] = UserType.STUDENT.value
        return self.create_user(username, email, password, **extra_fields)

    def create_staff(
        self, username, email=None, password=None, **extra_fields
    ):
        extra_fields['type'] = UserType.STAFF.value
        return self.create_user(username, email, password, **extra_fields)

    def admins(self):
        return self.get_queryset().admins()

    def students(self):
        return self.get_queryset().students()

    def staffs(self):
        return self.get_queryset().staffs()


class User(TimeStampedModel, AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    type = models.TextField(_('type'), choices=UserType.choices())
    email = models.EmailField(_('email address'), unique=True)
