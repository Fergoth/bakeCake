from django.contrib.auth import get_user_model


class NoPasswordBackend:
    def authenticate(self, request, phonenumber=None, name=""):
        User = get_user_model()
        try:
            user = User.objects.get(phonenumber=phonenumber)
        except User.DoesNotExist:
            user = User(phonenumber=phonenumber, name=name)
            user.save()
        return user

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
