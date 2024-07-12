from django.http import HttpResponse


def aboutUs(request):
    return HttpResponse(" Welcome to Nikhil Learning")

def cource(request):
    return HttpResponse("Cource page")

def course(request,courceid):
    return HttpResponse(courceid)