from django.contrib.auth.models import User
from rest_framework import serializers

from catalog.models import Book, Library


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)

    class Meta:
        model = Library
        fields = ('url', 'id', 'name', 'state', 'books')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'books')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(many=False, view_name='user-detail', read_only=True)
    library = serializers.HyperlinkedRelatedField(many=False, view_name='library-detail', queryset=Library.objects.all())

    class Meta:
        model = Book
        fields = ('url', 'id', 'title', 'author', 'library', 'pub_date')
