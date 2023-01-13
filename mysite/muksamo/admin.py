from django.contrib import admin
from .models import Question


#admin 페이지에 데이터 정보 추가를 위해선 여기에 admin.site.register(model명)
admin.site.register(Question)

# Register your models here.
