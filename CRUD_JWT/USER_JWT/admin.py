from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAbs

class UserAbsAdmin(UserAdmin):
    list_display = ('username', 'email', 'telefone')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('idade', 'telefone', 'endereco',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('endereco', 'idade', 'escolaridade', 'animais', 'biografia')}),
    )

admin.site.register(UserAbs, UserAbsAdmin)


