from  django.http import  HttpResponse

def index(request):

    return HttpResponse("Wellcome My Django App")