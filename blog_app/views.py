from django import http
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout, authenticate
from .models import *


def index(request):
    user = request.user
    if user.is_authenticated:

        blogs = Blog.objects.all()

        for blog in blogs:
            blog.content = blog.content.strip('"')
            print(blog.content)

        profile = Profile.objects.get(owner=user.id)

        image = profile.img

        if profile.img == 'blank-profile-picture.png':
            image = None

        return render(request, 'index.html', {

            'username': user.username,
            'blogs': blogs,
            'img': image

        })
    else:
        return redirect('login')


def delete_blog_admin(request, id):

    blog = Blog.objects.get(pk=id)
    blog.delete()

    return redirect('delete_blog')


def add_blog(request):

    if request.method == 'POST':
        print(request.POST['title'])
        print(request.POST['content'])
        print(request.POST['visibility'])
        print(request.POST['category'])
        user = User.objects.get(username=request.user.username)
        blog = Blog(publisher=user, content=request.POST['content'], title=request.POST['title'], category=request.POST['category'],
                    visibiliry=request.POST['visibility'])
        blog.save()

    return render(request, 'add_blog.html')


def choos_edit(request):

    user = User.objects.get(username=request.user.username)
    blogs = Blog.objects.filter(publisher_id__exact=user.id)

    print(blogs.count())

    if blogs.count() == 0:
        message = 'List is empry'
    else:
        message = None

    return render(request, 'choos_edit_blog.html', {

        "blogs": blogs,
        "message": message
    })


def edit_blog(request, id):

    blog = Blog.objects.get(pk=id)
    temp = blog
    blog.delete()

    return render(request, 'edit_blog.html', {

        "blog": temp

    })


def delete_blog(request):
    user = User.objects.get(username=request.user.username)
    blogs = Blog.objects.filter(publisher_id__exact=user.id)

    print(blogs.count())

    if blogs.count() == 0:
        message = 'List is empry'
    else:
        message = None

    return render(request, 'delete_blog.html', {

        "blogs": blogs,
        "message": message
    })


def setting(request):

    R_year = validate_date(str(request.user.date_joined.year))
    R_month = validate_date(str(request.user.date_joined.month))
    R_day = validate_date(str(request.user.date_joined.day))

    register_date = R_month+'/'+R_day+'/'+R_year
    print(register_date)

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        tel = request.POST['tel']
        old_pas = request.POST['old_pas']
        new_pas = request.POST['new_pas']
        img = request.POST.get('img')
        date = request.POST['date']

        user = User.objects.get(username=name)
        profile = Profile.objects.get(owner=user.id)
        user.username = name
        user.email = email
        if not date == '':
            profile.birth_date = date

        # user.password = new_pas

        # profile.img = img
        profile.phone_number = tel
        profile.save()
        user.save()
        image = profile.img

        if profile.img == 'blank-profile-picture.png':
            image = None
        return render(request, 'setting.html', {

            'name': name,
            'email': email,
            'tel': tel,
            'birth_date': date,
            'register_date': register_date,
            'img': image,
        })

    else:

        profile = Profile.objects.get(owner=request.user.id)

        image = profile.img

        if profile.img == 'blank-profile-picture.png':
            image = None

        if profile.birth_date is not None:

            B_year = validate_date(str(profile.birth_date.year))
            B_month = validate_date(str(profile.birth_date.month))
            B_day = validate_date(str(profile.birth_date.day))
        else:

            B_year = 'YYYY'
            B_month = 'MM'
            B_day = 'DD'

        birth_date = B_year+'-'+B_month+'-'+B_day

        return render(request, 'setting.html', {

            'name': request.user.username,
            'email': request.user.email,
            'tel': profile.phone_number,
            'birth_date': birth_date,
            'register_date': register_date,
            'img': image,
        })


def validate_date(arg):
    if len(arg) >= 2:
        return arg
    else:
        return '0'+arg


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
            profile = Profile(owner=user)
            profile.save()

            return redirect('login')

        else:
            return redirect('sing_up')
    else:
        form = SingUpForm()
        context = {'form': form}
        return render(request, 'sign_up.html', context)
