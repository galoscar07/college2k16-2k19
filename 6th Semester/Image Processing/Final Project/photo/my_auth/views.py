from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from my_auth.forms import UserForm, UserProfileInfoForm


@login_required
def user_logout(request):
    # import pdb;pdb.set_trace()
    logout(request)
    return HttpResponseRedirect('/home/')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('photoeditor:index'))
            else:
                return render(request, 'login.html',
                              {
                                  'invalid_credential': True,
                                  'invalid_message': 'Your account is inactive.'
                              })
        else:
            return render(request, 'login.html',
                          {
                            'invalid_credential': True,
                            'invalid_message': 'Invalid login details given'
                          })
    else:
        return render(request, 'login.html', {})


