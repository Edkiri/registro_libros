from django.contrib import admin
from books.models import Books, Authors, Sagas, Genders

# Register your models here.

class SagasAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class BooksAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

class GendersAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Books, BooksAdmin)

admin.site.register(Authors)

admin.site.register(Sagas, SagasAdmin)

admin.site.register(Genders, GendersAdmin)
