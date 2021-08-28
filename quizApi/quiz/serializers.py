from django.db.models.base import Model
from quiz.models import Category, Question, Quizes, Answer, Updated
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        Model = Category
        fields = ('name')
