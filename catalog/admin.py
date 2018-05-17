from django.contrib import admin
from catalog.models import Book, Library

# put all models in a list
models = [Book,Library]

# Register your models here.
admin.site.register(models)