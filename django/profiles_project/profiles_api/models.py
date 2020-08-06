from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps django works with our custom user model"""
    def create_user(self, email, name, password=None):
        """Create a new user profile object"""
        if not email:
            return ValueError('User must have a email address')
        email = self.normalize_email(email) # fix the format for email fields
        user = self.model(email=email, name=name)
        user.set_password(password) # this method encript the password by a hash method
        user.save(using=self._db)

        return user
    def create_superuser(self, email, name, password):
        """Creates and saves a new super user with given details credentials"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # is personal

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    # the fiels required by the app
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    def __str__(self):
        return self.email