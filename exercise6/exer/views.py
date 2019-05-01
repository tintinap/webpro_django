from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from exer.forms import LeaveModelForm
from .models import Dayoff
from django.contrib.auth.decorators import login_required, permission_required

import datetime

# Create your views here.
def my_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check are they match in database
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            print('Account logged in by '+username)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                if request.user.groups.filter(name="manager").exists():
                    return redirect('/admin')
                return redirect('index')

            return redirect('index')
        else:

            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name="dayoff/login.html", context=context)


def my_logout(request):
    print(request.user.username+' logged out.')
    logout(request)
    return redirect('login')


@login_required
def index(request):
    dayoff = Dayoff.objects.all()
    context = {'dayoff': dayoff}
    return render(request, template_name='dayoff/index.html', context=context)


@login_required
def leave(request):
    print(datetime.date.today())
    context = {}

    if request.method == 'POST':
        form = LeaveModelForm(request.POST)
        if form.is_valid():
            Dayoff = form.save(commit=False)
            Dayoff.create_by = request.user
            form.save()
            redirect('index')
    else:
        form = LeaveModelForm()

    context['form'] = form
    return render(request, template_name='dayoff/leavev.html', context=context)
