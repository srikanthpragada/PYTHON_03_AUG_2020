from django.http import HttpResponse


# Function view
def welcome(request):
    return HttpResponse('<h1 style="color:blue">Welcome To Django </h1>')
