from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signupview(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(email,'', password)
            return redirect('login')
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています。'})
    else:
        print('GET method')
    return render(request, 'signup.html', {'somedata':100})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username_data')
        password = request.POST.get('password_data')
        print(username)
        print(password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print('ログイン成功です！！')
        else :
            print('Userが存在しません')
        return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})

