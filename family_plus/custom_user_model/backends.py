from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class CaseInsensitiveModelBackend(ModelBackend):

    """Make login email field case insensitive."""

    # Credit: https://youtu.be/SFarxlTzVX4
    # This class allows the login email field to become case insensitive.
    # Users can enter their email characters in any casing.

    UserModel = get_user_model()
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        """Authenticate user and make login field case insensitive."""
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        try:
            case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
            user = UserModel._default_manager.get(**{case_insensitive_username_field: username})
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user