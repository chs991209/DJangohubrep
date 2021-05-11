from django.shortcuts import render
from .models import Fcuser

# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

    fcuser = Fcuser(
        username=username,
        password=password
    )

    fcuser.save()

    return render(request, 'register.html')
