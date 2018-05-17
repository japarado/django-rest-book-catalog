from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class TimestampModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Library(TimestampModel):
    name = models.CharField(max_length=500, unique=True)
    state = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Libraries'


class Book(TimestampModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='books')
    library = models.ForeignKey(Library, on_delete=models.DO_NOTHING, related_name='books')
    pub_date = models.DateField()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Book,self).save()

    def __str__(self):
        return self.title
