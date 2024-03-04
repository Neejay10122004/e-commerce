from django.contrib import admin
from .models import contact_detail
from .models import checkout_detail

# Register your models here.

admin.site.register(contact_detail)
admin.site.register(checkout_detail)