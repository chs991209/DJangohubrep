from django.shortcuts import render
from .models import Fcuser

# Create your views here.

# register로 들어오려는 요청이 두 가지가 생기게 됨
# 1. 웹사이트 url을 입력하여 접속하는 경우
# 2.  제출 버튼을 클릭하여 접속하는 경우


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
