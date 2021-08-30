from django.db.models import fields
from django.db.models.base import Model
from quiz.models import Category, Question, Quizes, Answer, Updated
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class QuizesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    #category =  serializers.StringRelatedField()
    class Meta:
        model = Quizes
        fields = ('title','category','date_created')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id','answer_text','is_right')

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many = True, read_only = True)
    quiz = QuizesSerializer(read_only = True)
    class Meta:
        model = Question
        fields = ('quiz','answer','title','technique','difficulty','date_created','is_active')


class TopicRelatedQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many = True, read_only = True)
    quiz = QuizesSerializer(read_only = True)
    class Meta:
        model = Question
        fields = ('quiz','answer','title','is_active')



class UpdatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Updated
        fields = ('date_updated')
