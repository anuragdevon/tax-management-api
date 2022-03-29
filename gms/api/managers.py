from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **args):
        if not email:
            raise ValueError(_('Email is empty!'))
        if not password:
            raise ValueError(_('Password is empty!'))

        email = self.normalize_email(email)

        user = self.model(email=email, **args)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **args):
        args.setdefault('is_active', True)
        args.setdefault('role', 1)

        if args.get('role') != 1:
            raise ValueError('Superuser must have role of Global Admin')
        return self.create_user(email, password, **args)
        