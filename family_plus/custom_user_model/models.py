from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# User model, user manager, and function below credits and inspired by
# CodingWithMitch. Tutorial link: https://youtu.be/SFarxlTzVX4
# With this custom user model, I can set users to log in with emails as
# opposed to Django's User model default, which is log in with username.

class MyUserManager(BaseUserManager):

    """Customize the user and superuser creation processes."""

    def create_user(self, email, username, password=None):
        """Manager for create user process."""
        if not email:
            raise ValueError("Users must have an email address.")
        if not username:
            raise ValueError("Users must have a username.")

        user = self.model(
            email=self.normalize_email(email),  # makes email all lowercase
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """Manager for create superuser process."""
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


def get_profile_image_filepath(self, filename):
    """Save user uploaded profile images to the media folder."""
    return 'profile_images/' + str(self.pk) + '/profile_image.png'


class CustomUserModel(AbstractBaseUser):

    """Customize a user model for overriding Django's default User model."""

    email         = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username      = models.CharField(max_length=30, unique=True)
    date_joined   = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login    = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255,
                                      upload_to=get_profile_image_filepath,
                                      null=True, blank=True)

    # Family relation status choices
    PARENT = "Parent"
    GUARDIAN = "Guardian"
    RELATIVE = "Relative"
    OTHER = "Other"
        
    FAMILY_RELATION_STATUS = [
        (PARENT, "Parent"),
        (GUARDIAN, "Guardian"),
        (RELATIVE, "Relative"),
        (OTHER, "Other")
    ]

    # Age verification, family relation status, and location of the user
    # making the account
    is_adult = models.BooleanField(default=False)
    family_relation_status = models.CharField(max_length=20,
        choices=FAMILY_RELATION_STATUS,
        default="Parent")
    # country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    # city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    # Apply the user manager to the custom model
    objects = MyUserManager()

    # Hide user emails from other users by default
    hide_email    = models.BooleanField(default=True)

    # Users log in with their email. Their username are viewable to other users.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        """Label users by their username."""
        return self.username

    def get_profile_image_filename(self):
        """Rename user uploaded profile images to profile_image.png"""
        return str(self.profile_image)[str(self.profile_image).index(
            'profile_images/' + str(self.pk) + "/"):]

    def has_perm(self, perm, obj=None):
        """Used to specify admin permissions for admin users."""
        return self.is_admin

    def has_module_perms(self, app_label):
        """Used to specify module permissions available to all users."""
        return True