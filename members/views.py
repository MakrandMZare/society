from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Members!")

# Create your views here.
