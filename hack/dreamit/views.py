from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact, Course, Chapters, SubCourse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(rquest):
    return render(rquest, "dreamit/index.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'dreamit/contact.html')

def courses(request):
    allcourse = Course.objects.all()
    params = {'allcourse' : allcourse}
    return render(request, 'dreamit/courses.html', params)

def subcourse(request):
    allsubcourse = SubCourse.objects.all()
    params = {'allsubcourse' : allsubcourse}
    return render(request, 'dreamit/subcourse.html', params)


def chapter(request):
    allchapter = Chapters.objects.all()
    params = {'allchapter' : allchapter}
    return render(request, "dreamit/chapter.html", params)

def about(request):
    return render(request, "dreamit/about.html")

def content(request):
    return render(request, 'dreamit/content.html')

def sign(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['emailid']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, "Your Account has been successfully created.")
        redirect("/signin")
        # return redirect('contact')

    return render(request, "dreamit/sign.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            # return render(request, "store/index.html", {"fname":fname})
            return redirect("/")
        else:
            messages.error(request, "Check your detail once again!")
            return redirect("/")

    return render(request, "dreamit/sign.html")
    # return redirect("/")

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect("/")