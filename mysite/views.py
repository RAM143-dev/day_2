from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Jenkins CI/CD with Django!")