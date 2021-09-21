from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(
        required=True, allow_blank=False, max_length=100, allow_null=False)
    pages = serializers.IntegerField(
        required=True, allow_null=False)

    def create(self, validated_data):
        book_found = Book.objects.filter(title=validated_data['title']).first()
        if book_found:
            raise serializers.ValidationError(
                {"detail": "book has exists with title"})
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.save()
        return instance
