from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from projectapp.models import Province,Pump,SubProvince,User
from projectapp.forms import PumpForm,UserForm
from django.http import JsonResponse


def register(requests):


    if requests.POST:
        data = requests.POST

        username = data.get('username', '')
        last_name = data.get('name', '')
        phone = data.get('phone', '')
        password = data.get('password', '')
       
     

       
        user = User.objects.filter(username=username).first()
        if user:
            return render(requests, 'auth/sign-up.html', {'error': "Bunaqa user bor"})

        user = User.objects.create(username=username, password=password, last_name=last_name, phone=phone, )

        login(requests, user)
        authenticate(requests)

        return redirect('index')

    return render(requests, 'auth/sign-up.html', {})
