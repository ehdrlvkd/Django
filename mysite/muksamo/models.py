from django.db import models

#새로운 data를 추가하고 싶다면 class 데이터클래스(models.Model) 내부에 스키마 데이터 작성



class Question(models.Model):
    Bung_Name = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.Bung_Name


# Create your models here.
