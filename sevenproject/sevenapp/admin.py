from django.contrib import admin
from sevenapp.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['number','title','author','publisheddate']

admin.site.register(Book,BookAdmin)
