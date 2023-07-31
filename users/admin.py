from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser


class MyUserAdmin(UserAdmin):
    #add_form = MyUserCreationForm
    #form = MyUserChangeForm
    model = MyUser

    # layout of change user page on admin
    fieldsets = (
            ('User Information', {'fields': ('username', 'password')}),
            ('Personal Information', {'fields': ('wechat_id', 'first_name', 'last_name', 'email')}),
            ('Permissions', {'fields': ('is_tutor', 'is_staff', 'is_superuser', 'is_active')}),
            ('Important Dates', {'fields': ('last_login', 'date_joined')}),
            ('Other Info', {'fields': ('nickname', 'label', 'comment')})
    )

    # layout of add user page on admin
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "wechat_id"),
            },
        ),    
    )

    # layout of fields in user list
    list_display = (
        'username', 
        'wechat_id', 
        'nickname',  
        'is_tutor', 
        'is_staff', 
        'is_active'
    )



admin.site.register(MyUser, MyUserAdmin)