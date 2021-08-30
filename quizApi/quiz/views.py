from django.shortcuts import render
from .models import Quizes, Question, Answer, Category
from .serializers import QuizesSerializer, QuestionSerializer, AnswerSerializer, CategorySerializer, TopicRelatedQuestionSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

@csrf_exempt
def getQuizApi(request, id = 0):
    print("called method "+ request.method)
    if request.method == 'GET':
        quiz_data = Quizes.objects.all()
        quiz_serializer = QuizesSerializer(quiz_data, many = True)
        return JsonResponse(quiz_serializer.data, safe= False)

    elif request.method == 'POST':
        quiz_json = JSONParser().parse(request)
        quiz_serializer = QuizesSerializer(data=quiz_json)
        if quiz_serializer.is_valid():
            quiz_serializer.save()
            return JsonResponse('Successfully has been saved', safe=False)
        return JsonResponse('Failed to save quiz')

    elif request.method == 'PUT':
        quiz_data = JSONParser().parse(request)
        quiz = Quizes.objects.get(id = quiz_data['id'])
        quiz_serializer = QuestionSerializer(quiz,quiz_data)
        if(quiz_serializer.is_valid()):
            quiz_serializer.save()
            return JsonResponse('Successfully has been updated', safe=False)
        return JsonResponse('Failed to updated')
    elif request.method == 'DELETE':
        quiz = Quizes.objects.get(id)
        quiz.delete()
        return JsonResponse("Successfully has beed deletd")


@csrf_exempt 
def getRandomQuestion(request, **kwargs):
    if request.method == 'GET':
        question_data = Question.objects.filter(quiz__title = kwargs['topic']).order_by('?')
        question_serializer = QuestionSerializer(question_data,many = True)
        return JsonResponse(question_serializer.data, safe=False)

@csrf_exempt 
def getQuestions(request):
    if request.method == 'POST':
        json_data = JSONParser().parse(request)
        question_data = Question.objects.filter(difficulty = json_data['difficulty']).order_by('?')
        question_serializer = TopicRelatedQuestionSerializer(question_data,many = True)
        return JsonResponse(question_serializer.data, safe=False)