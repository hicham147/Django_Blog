import re
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request,f'you Account has been created ! ')
            return redirect('profile')
    else:
        form = CreateUserForm()

    return render(request, 'Users/register.html',{"form":form})

@login_required
def profile(request):
    return render(request,'Users/profile.html')



