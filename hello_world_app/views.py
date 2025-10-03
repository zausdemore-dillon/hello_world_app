from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world! My name is Zac Ausdemore-Dillon.")

