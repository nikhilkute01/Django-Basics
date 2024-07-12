from django.http import HttpResponse
from django.shortcuts import render


def aboutUs(request):
    return HttpResponse(" Welcome to Nikhil Learning")

def cource(request):
    return HttpResponse("Cource page")

def course(request,courceid):
    return HttpResponse(courceid)
def index(request):
    data={
        'title':'Home page',
        'clist':['PhP','java','paython','jquery','js',],
        'number':[1,2,3,4,5,6,7,8,9],
        'student_info':[
            {'Name':'Nikhil','Roll_No':26},
            {'Name':'Rakesh','Roll_No':27}
        ]
    }
    return render(request,"index.html",data)