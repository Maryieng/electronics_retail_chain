from django.contrib import admin   # type: ignore

from users.models import User

admin.site.register(User)
