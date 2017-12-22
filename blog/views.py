from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'blog/index.html',context={
        'title':'博客首页',
        'welcome':'欢迎来到kuwe博客'
    })
