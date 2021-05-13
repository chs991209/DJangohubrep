from django.http import HttpResponse
from django.shortcuts import render
from .models import Fcuser
from django.contrib.auth.hashers import make_password


# Create your views here.

def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and password and re_password and useremail):
            res_data['error'] = 'Input every values'

        elif password != re_password:
            res_data['error'] = 'Different Password'

        else:
                fcuser = Fcuser(
                    username=username,
                    password=make_password(password),
                    useremail=useremail
                )

                fcuser.save()

        return render(request, 'register.html', res_data)
