from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models


class CustomerUserManager(UserManager):
    def create_user(self, phone, email=None, password=None, status=True, is_staff=False, is_superuser=False,
                    is_active=True,
                    **extra_fields):
        user = self.model(phone=phone, password=password, is_staff=is_staff, is_superuser=is_superuser,
                          is_active=is_active, **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone=None, email=None, password=None, **extra_fields):
        return self.create_user(phone=phone, password=password, is_staff=True, is_superuser=True, is_active=True,
                                **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=128, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)
    email = models.EmailField()
    last_name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    groups = models.ManyToManyField('auth.Group', related_name='custom_users_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users_permissions')

    status = models.BooleanField(default=True)

    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = CustomerUserManager()

    USERNAME_FIELD = 'phone'


class OTP(models.Model):
    key = models.CharField(max_length=1024)
    phone = models.CharField(max_length=20)

    is_conf = models.BooleanField(default=False)
    is_expire = models.BooleanField(default=False)
    tires = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.tires >= 3:
            self.is_expire = True

        super(OTP, self).save(*args, **kwargs)
