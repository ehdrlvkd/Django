from django.db import models

#새로운 data를 추가하고 싶다면 class 데이터클래스(models.Model) 내부에 스키마 데이터 작성



class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()


# Create your models here.
