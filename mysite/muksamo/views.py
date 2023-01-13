from django.shortcuts import render
from django.http import HttpResponse


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
# Create your views here.
