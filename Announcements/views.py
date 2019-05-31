from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import HttpResponse,render, redirect
from .models import Announcements
from Log_In.models import RegisteredStaffs,RegisteredStd
from django.core.files.storage import FileSystemStorage


# Create your views here.
def announcement(request, STDN):


    user = Announcements.objects.filter(id=RegisteredStd.objects.filter(Std_no=STDN).count() - 1)



    context = {
        'user': user,
        'STDN': STDN,
    }


    return render(request, 'Register/Announcement.html', context)

def astudent(request, STDN):
    print("inside function")


    user = RegisteredStd.objects.filter(Std_no=STDN)
    announcement = Announcements.objects.all().order_by('-Created')


    print("below s")
    context = {
        'user': user,
        'STDN': STDN,
        'announcement': announcement,
    }
    print("inside function")

    return render(request, 'Register/View_announcement.html', context)

def astaff(request, Staff_No):
    print("inside function")


    user = RegisteredStaffs.objects.filter(Staff_no=Staff_No)
    #announcement = Announcements.objects.all()
    #announcement = Announcements.objects.filter(Lect_No=Staff_No)
    announcement = Announcements.objects.all().order_by('-Created')


    print(user)
    context = {
        'user': user,
        'STDN': Staff_No,
        'announcement': announcement,
    }
    print("inside function")

    return render(request, 'Register/View_announcement.html', context)