from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from . import forms

def logoutview(request):
    logout(request)
    return redirect('blog:post_list')

def loginview(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if not user:
                return redirect('account:loginview')
            login(request, user)
            return redirect('blog:post_list')

    form = forms.LoginForm()
    return render(request, 'account/login.html', {'form':form})
