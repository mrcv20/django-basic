from django.contrib import admin
from .models import Category, Contact

# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
...
admin.site.unregister(User)

class UserAdmin(UserAdmin):
    model = User
    list_filter = ()

admin.site.register(User, UserAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display= ['id', 'nome', 'sobrenome', 'mostrar', 'telefone']

    list_display_links = ('id', 'nome', 'sobrenome')

    # list_filter = ('nome', 'sobrenome')

    list_per_page = 10

    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')

admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)