from django.contrib import admin

# Register your models here.
from . models import User_Data, Weight_Update

admin.site.register(User_Data)
admin.site.register(Weight_Update)
