import re
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'you Account has been created !')
            return redirect('signIn')
    else:
        form = CreateUserForm()

    return render(request, 'Users/register.html',{"form":form})

@login_required
def profile(request):
    return render(request,'Users/profile.html')




def EditProfile(request):    
    if  request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'you Account has been updated !')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()


    context = {
        "u_form":u_form,
        "p_form":p_form,
    }
    return render(request,'Users/updatinfo.html',context)




