from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserLogin)
class UserLoginAdmin(admin.ModelAdmin):
    list_display = ['id','username']

@admin.register(UserCsvFile)
class UserCsvFileAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(CSVModel)
class UserCsvFileAdmin(admin.ModelAdmin):
    list_display = ['id','shop1','shop2','total_inventary','minimum_stock']
