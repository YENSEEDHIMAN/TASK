from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin  # Add PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, dob, gender, phone_number, address, profile_picture=None, password=None):
        """Creates and returns a user with all required fields."""
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            dob=dob,
            gender=gender, 
            phone_number=phone_number, 
            address=address, 
            profile_picture=profile_picture,  
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, dob, password=None, profile_picture=None):
        """Creates and returns a superuser with default values for required fields"""
        user = self.create_user(
            email=email,
            full_name=full_name,
            dob=dob,
            gender="Not Specified",
            phone_number="0000000000",
            address="Admin Address",
            profile_picture=profile_picture,
            password=password,
        )
        user.is_superuser = True  
        user.is_staff = True 
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):  # Add PermissionsMixin here
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to="profile_pics/", null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Required for Django Admin access

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "dob"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Returns True if the user has a specific permission."""
        return True  # Modify this if you implement custom permissions

    def has_module_perms(self, app_label):
        """Returns True if the user has permission to view the given app_label."""
        return True
