from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from accounts.forms import RegistrationForm,EditProfileForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form=RegistrationForm()
    args = {'form':form}
    return render(request,'accounts/reg_form.html', args)

@login_required
def view_profile(request,pk=None):
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user= request.user
    args = {'user':user}
    return render(request,'accounts/profile.html',args)


@login_required
def edit_profile(request):
    if request.method=='POST':
        p_form= ProfileUpdateForm(request.POST , request.FILES , instance=request.user.userprofile)
        form =EditProfileForm(request.POST,instance=request.user)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            return redirect('/accounts/profile')
    else:
        p_form= ProfileUpdateForm(instance=request.user.userprofile)
        form=EditProfileForm(instance=request.user)
    args ={'form':form, 'p_form':p_form}
    return render(request,'accounts/edit_profile.html',args)

@login_required
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change_password')
    else:
        form=PasswordChangeForm(user=request.user)
    args ={'form':form}
    return render(request,'accounts/change_password.html',args)
