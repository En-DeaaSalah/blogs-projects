from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import LoginForm, SingUpForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate


def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'index.html', {})
    else:
        return redirect('login')


def logOut(request):

    logout(request)

    return redirect('login')


def login_user(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

            userName = form.cleaned_data['userName']
            userPassword = form.cleaned_data['password']

            user = authenticate(username=userName, password=userPassword)
            print(user)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
    else:

        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)


def sing_up(request):

    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():

            userName = form.cleaned_data['userName']

            userEmail = form.cleaned_data['email']

            userPassword = form.cleaned_data['password']

            userRePassword = form.cleaned_data['re_password']

            if User.objects.filter(username__exact=userName).exists():
                return redirect('sing_up')

            if User.objects.filter(email__exact=userEmail).exists():

                return redirect('sing_up')

            if not userPassword == userRePassword:

                return redirect('sing_up')

            user = User.objects.create_user(
                username=userName, email=userEmail, password=userPassword)
            user.save()

            return redirect('login')

            # User.objects.get(username=userName)

            # user = authenticate(username=userName, password=Userpassword)
            # print(user)

            # if user is None:
            #     messages.error(request, "this user alrady exist")

            #     return redirect('sing_up')
            # else:
            #     userAccount = User.objects.create_user(
            #         userName, email, Userpassword)
            #     userAccount.save()
            #     return redirect('login')

        else:
            return redirect('sing_up')
    else:
        form = SingUpForm()
        context = {'form': form}
        return render(request, 'sign_up.html', context)
