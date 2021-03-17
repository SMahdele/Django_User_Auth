from django.db import models


from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self,email,uid, password=None, *args, **extra_fields):
        if email is None:
            raise TypeError('email required')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.uid = uid
        user.save()
        return user

    def create_superuser(self, email, uid, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user( email, uid,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
