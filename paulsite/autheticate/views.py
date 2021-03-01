from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from autheticate.forms import SignUpForm, EditProfileForm
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request, 'autheticate/home.html', {})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			messages.success(request, ('Login Successfully!'))
			return redirect('home')
		else:
			messages.success(request,('Incorrect - Please try again!'))
			return redirect('login')

	else:
		return render(request, 'autheticate/login.html', {})

def logout_user(request):

	logout(request)
	messages.success(request,('Logout Successfully!'))
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('Register Successfully!'))
			return redirect('home')

	else:
		form = SignUpForm()
	context = {'form': form}
	return render(request, 'autheticate/register.html', context)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request,('You Have Edited Your Profile...'))
			return redirect('home')
	else:
		form = EditProfileForm(instance= request.user)

	context = {'form': form}
	return render(request, 'autheticate/edit_profile.html', context)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			messages.success(request,('You Have Edited Your Password...'))
			return redirect('home')
	else:
		form = PasswordChangeForm(user= request.user)

	context = {'form': form}
	return render(request, 'autheticate/change_password.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
from django.core.paginator import Paginator, EmptyPage, InvalidPage


lst = []
answers = Questions.objects.all()
anslist = []
for i in answers:
    anslist.append(i.answer)


@login_required(login_url='/login')
def quiz(request):
    obj = Questions.objects.all()
    count = Questions.objects.all().count()
    paginator = Paginator(obj,1)
    try:
       page = int(request.GET.get('page','1'))  
    except:
        page =1
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):

        questions=paginator.page(paginator.num_pages)
    
    return render(request,'autheticate/templates/quiz.html',{'obj':obj,'questions':questions,'count':count})

@login_required(login_url='/login')
def result(request):
    score =0
    for i in range(len(lst)):
        if lst[i]==anslist[i]:
            score+=1
    return render(request,'autheticate/templates/result.html',{'score':score,'lst':lst})

@login_required(login_url='/login')
def save_ans(request):
    ans = request.GET['ans']
    lst.append(ans)

def welcome(request):
    lst.clear()
    return render(request,'autheticate/templates/welcome.html')

