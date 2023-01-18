from django.shortcuts import render
from django.http import HttpResponse
from .models import Bung_List

def index(request):
    return render(request,'index.html',{})

def search_map(request):

    if request.method == 'POST':
        data = request.POST['search-place']
        print(data)
        context ={
            'data':data
        }
        return render(request,'search_map.html',context)
    else:
        data = "무한리필"
        context={
            'data':data
        }
        return render(request,'search_map.html',context)
    
# Create your views here.


def create_bung(request):
    print(f"지금 리퀘스트는?{request}")
    if request.method == 'POST':
        data = request.POST
        Bung_List.objects.create(
            Bung_Name = data['bung_name']+" 번개모임",
            content = data['bung_content'],
            create_date = data['bung_date']
        )
            
        context = {
            'bung_name' : data['bung_name'],
            'bung_content' : data['bung_content'],
            'bung_date' : data['bung_date']
        }
        return render(request,'Bung_List.html',context)
    else:
        return render(request,'Bung_List.html',{})

#3373af60e0702b00d075178d19793b57 kakao js key