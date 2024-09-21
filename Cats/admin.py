from django.contrib import admin
from Cats.models import Cat

class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(Cat, CatAdmin)
    
