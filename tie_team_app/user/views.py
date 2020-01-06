from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .models import stats,ImgInfo
from .form import ChangeStatForm


def index(request):
    return render(request, 'user/index.html')


def logout_view(request):
    """log the user out """
    logout(request)
    return HttpResponseRedirect(reverse('user:index'))

def teamstats_view(request):
    info = ImgInfo.objects.all()
    stat = stats.objects.all()
    return render(request, 'user/teamstats.html', {'info':info,'stat':stat})

def myprofile_view(request):
    form = ChangeStatForm()
    return render(request,'user/test.html',{'form':form})
