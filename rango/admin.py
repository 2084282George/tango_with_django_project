from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
# Register your models here.
