from django.db import models
from django.contrib.auth.models import User
class PrevLetter(models.Model):
    question_type = models.IntegerField(default=0) #previousQuestions[id-1][0]
    level_type = models.IntegerField(default=0) #previousQuestions[id-1][1]
    question = models.IntegerField(default=0) #previousQuestions[id-1][2]
    option = models.IntegerField(default=0) #previousQuestions[id-1][3]
    question_text = models.CharField(max_length=200) #문자열, 이전 편지를 띄움
    is_active = models.BooleanField(default=True) #사용자가 편지 그림을 그렸는지 안그렸는지 True or False

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(PrevLetter, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)