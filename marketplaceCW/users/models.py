from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager, PermissionsMixin )
from django.core.validators import validate_email


class MyUserManager(BaseUserManager):
    def _create_user(self, email, date_of_birth, password, **extra_fields):
        validate_email(email)
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            date_of_birth= date_of_birth,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, date_of_birth, password, **extra_fields):
        extra_fields.setdefault('image', 'images/placeholder.jpg')
        user = self._create_user(email, date_of_birth, password, **extra_fields)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', unique=True)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def __iter__(self):
        return self

# Create your models here.
