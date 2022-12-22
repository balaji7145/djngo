from django.contrib import admin
from .models import FormModel
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=['name','age','address']
admin.site.register(FormModel,MovieAdmin) 