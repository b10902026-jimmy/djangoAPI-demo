# Create your views here.
from django.shortcuts import render, redirect
from .models import User

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User(name=name, email=email, password=password)
        user.save()
        return redirect('user_profile', user_id=user.id)
    else:
        return render(request, 'register.html')


def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user_profile.html', {'user': user})