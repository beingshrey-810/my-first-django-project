from django.contrib import admin

from home.models import Signup

# admin.site.register(Signup)

# Register your models here.

@admin.register(Signup)


class SignupAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'email')
    ordering = ('name',)
    # putting -name will give descending ordering
    search_fields = ('name', 'department')
    list_filter = ('department',)