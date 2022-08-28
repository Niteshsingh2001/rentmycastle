from turtle import pos
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def home(request):
    data = post.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def signin(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(username=user_name, password=password)
        if user is not None:
            # messages.error("Something went wrong!!")

            login(request, user)
            cont = {"name": user, "status": True}
            print("done")
            return redirect("/")
        else:
            cont = {"error": "Something went wrong!! "}
            print("failed")
            return render(request, 'login.html', cont)

    return render(request, "login.html")


@csrf_protect
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        InputEmail1 = request.POST["InputEmail1"]
        InputPassword1 = request.POST["InputPassword1"]

        user = User.objects.create_user(
            username=username, email=InputEmail1, password=InputPassword1, first_name=fname, last_name=lname)
        user.save()

        user = authenticate(username=username, password=InputPassword1)
        if user is not None:
            # messages.error("Something went wrong!!")

            login(request, user)
            cont = {"name": user, "status": True}
            print("done")
            return redirect("/")
        else:
            cont = {"error": "Something went wrong!! "}
            print("failed")
            return render(request, 'signup.html', cont)
    print("not working")
    # data= users_data.create(
    #     username = username
    #     profile
    # )
    return render(request, "signup.html")


def signout(request):
    logout(request)
    return redirect("/")


@login_required(login_url='/login/')
def profile(request):

    context = {"user": request.user, "full_name": request.user.get_full_name()}
    try:
        data = post.objects.filter(posted_by=request.user)
        context["data"] = data
        context["user_post"] = True
    except:
        context["user_post"] = False
    user = request.user.username
    if request.method == "POST":
        img1 = request.FILES["img1"]
        img2 = request.FILES["img2"]
        img3 = request.FILES["img3"]
        title = request.POST.get("title")
        location = request.POST.get("location")
        desc = request.POST.get("desc")
        posted_by = user
        # post_date =timezone.now
        price = request.POST.get("price")
        city = request.POST.get("city")
        state = request.POST.get("state")

        info = post.objects.create(

            img1=img1,
            img2=img2,
            img3=img3,
            title=title,
            location=location,
            desc=desc,
            posted_by=posted_by,
            price=price,
            post_date=timezone.now(),
            city=city,
            state=state

        )

        info.save()

    return render(request, "profile.html", context)


def post_view(request, title):
    data = post.objects.get(title=title)
    context = {"data": data}
    return render(request, "post.html", context)


def contact(request):
    return render(request, "contactus.html")
