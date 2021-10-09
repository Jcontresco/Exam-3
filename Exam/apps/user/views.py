import re
from django.shortcuts import redirect, render
from .forms import LoginForm, UserForm
from .models import User
import bcrypt
from django.contrib import messages
# Create your views here.

def logout(request):
    del request.session['user_id']
    del request.session['name']
    return redirect('/')
    
def login(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            formPassword = loginForm['password'].value()
            loginEmail = loginForm['email'].value()
            logged_user = User.objects.filter(email=loginEmail)

            if logged_user:
                logged_user = logged_user[0]
                if bcrypt.checkpw(formPassword.encode(), logged_user.password.encode()):
                    print('password is correct')
                    request.session['user_id'] = logged_user.id
                    request.session['name'] = logged_user.first_name
                    return redirect('/dashboard')
                else:
                    print('password is incorrect')
                    return redirect('/')
            else:
                print('Password or Email is not registered')
                return redirect('/')
        return redirect('/')
    else:
        return render(request, 'user/register.html')


def createUser(request):
    # POST 
    if request.method == 'POST':
        
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            print('errors exist')
        
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:

            user_exist = User.objects.filter(email=request.POST['email'])
            if not user_exist:
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                password = request.POST['password']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                logged_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=pw_hash)
                request.session['user_id'] = logged_user.id
                request.session['name'] = logged_user.first_name
                
                print('no errors found')
                
                return redirect('/dashboard')
            else:
                messages.error(request, 'Email is already being used')
                return redirect('/')

        
           



