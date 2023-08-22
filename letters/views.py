from django.shortcuts import render
from .models import PrevLetter
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PrevLetterSerializer




def mymail(request):
    active_count = PrevLetter.objects.filter(is_active=True).count()
    question_list = PrevLetter.objects.order_by('-id').filter(is_active=True)
    question_context = {
        'question_list' : question_list ,
        'active_count': active_count
    }
    return render(request, 'letters/mymail.html',question_context)

def blockmail(request):
    return render(request, 'letters/blockmail.html')

#############unity##############
'''
@api_view(['POST'])
def receive_unity_data(request):
    serializer = PrevLetterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
'''

@api_view(['POST'])
def receive_unity_data(request):
    serializer = PrevLetterSerializer(data=request.data)

    if serializer.is_valid():
        received_data = serializer.validated_data
        question_type = received_data['question_type']
        level_type = received_data['level_type']
        question = received_data['question']
        option = received_data['option']

        # 중복 판별 로직
        if PrevLetter.objects.filter(
            question_type=question_type,
            level_type=level_type,
            question=question,
            option=option,
        ).exists():
            return Response({'message': 'Duplicate data'}, status=400)

        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)



#Level보내는
@api_view(['GET'])
def get_user_level(request):
    active_question_count = PrevLetter.objects.filter(is_active=True).count()

    if active_question_count < 15:
        level = 1
    elif active_question_count < 30:
        level = 2
    elif active_question_count < 50:
        level = 3
    elif active_question_count < 60:
        level = 4
    else:
        level = 5

    context = {
        'active_question_count': active_question_count,
        'level': level
    }
    return Response(context)


