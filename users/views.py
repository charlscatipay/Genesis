from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserProfileForm, UserCredentialForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.
def register(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST)
		form2 = UserCredentialForm(request.POST,initial={'user_profile':2})

		if form.is_valid() and form2.is_valid():
			user_profile = form.save(commit=False)
			user_profile.save()

			# get the UsersProfile Query to use as Foreign Key for UserCredential
			userprofile_query = models.UserProfile.objects.get(firstname=form.cleaned_data["firstname"]) 
			models.UserCredential.objects.create(
				username = form2.cleaned_data["username"], 
				password = form2.cleaned_data["password"], 
				user_profile = userprofile_query
			)

			# Redirect to homepage
			return redirect('/')
		print(f'HEEEEEEY!')
	else:
		form = UserProfileForm()
		form2 = UserCredentialForm()
	return render(
		request, 'register.html', {'form': form, 'form2': form2},
	)

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(
			username=request.POST['username'],
			password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			if 'next' in request.POST: # to see if there is a next query coming from login_required decorator
				return redirect(request.POST.get('next')) 
			else:
				return redirect('index')
		else:
			return render(request,
				'login.html',
				{'error':'username or password is incorrect.'})
	else:
		return render(request, 'login.html')

def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				# Check if username already exists
				user = models.UserCredential.objects.get(username=request.POST['username'])
				return render(
					request,
					'signup.html',
					{'error': 'Username already exists'})
			except models.UserCredential.DoesNotExist:
				# save UserProfile data
				user_profile = models.UserProfile.objects.create(
					firstname = request.POST['firstname'],
					lastname = request.POST['lastname'],
					email = request.POST['email'],
					location = request.POST['location'],
				)
				# save UserCredential data
				userprofile_query = models.UserProfile.objects.get(firstname=request.POST["firstname"]) # Think of this, what if another firstname already existed?
				user_credentials = models.UserCredential.objects.create(
					username = request.POST['username'],
					password = request.POST['password1'],
					user_profile = userprofile_query,
				)
				# register User data to django Users
				new_user = User.objects.create_user(
					username = user_credentials.username,
					password = user_credentials.password,
					email = user_profile.email,
					first_name = user_profile.firstname,
					last_name = user_profile.lastname
				)
				auth.login(request, new_user)
				return redirect('index')
		else:
			return render(
				request,
				'signup.html',
				{'error': 'Passwords must match'})
	
	return render(
		request, 'signup.html',
	)

def logout(request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('index')

@login_required(login_url='login')
def show_profile(request):
	# return HttpResponse('User Profile')
	context = {'user': models.UserCredential.objects.get}
	return render(
		request,
		template_name='profile.html',
		context=context,
	)
