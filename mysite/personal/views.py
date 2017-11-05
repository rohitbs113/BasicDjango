from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you like to contact me','Please mail me on rohitbs113@gmail.com']})