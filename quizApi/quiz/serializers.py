from django.db.models import fields
from django.db.models.base import Model
from quiz.models import Category, Question, Quizes, Answer, Updated
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')

class QuizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizes
        fields = ('title','category','date_created')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('quiz','title','technique','difficulty','date_created','is_active')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('question','answer_text','is_right')

class UpdatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Updated
        fields = ('date_updated')
