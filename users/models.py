import uuid
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        if not username:
            raise ValueError('The username field must be set')
        if not password:
            raise ValueError('The password field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user




class User(AbstractBaseUser):
    id = models.UUIDField(primary_key= True, default = uuid.uuid4, editable= False)
    username = models.CharField(max_length=225)
    email = models.CharField(max_length=225, unique = True)
    password = models.CharField(max_length=225)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return User.email