from django.contrib import admin

from .models import User
from .models import Access

admin.site.register(User)
admin.site.register(Access)
