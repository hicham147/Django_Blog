from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request,f'Account created successfully')
            return redirect('blog-home')
    else:
        form = CreateUserForm()

    return render(request, 'register.html',{"form":form})

