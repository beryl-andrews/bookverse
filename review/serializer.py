from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_id', 'book_id', 'title', 'content', 'rating', 'created_on']
        read_only_fields = ['id', 'created_on']