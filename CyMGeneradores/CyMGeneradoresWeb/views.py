from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import User
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return render(request, 'paginas/inicio.html')

def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Correo o contraseña incorrectos")

    return render(request, 'registration/login.html', {'form': form})