from django.shortcuts import render
from .models import Message
from django.db import models
from django.http import HttpResponse

# Create your views here.
def get_message(request):
    return render(request,'msg.html')

def get_content(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        message = request.POST.get('message','')

        Q_message = Message()
        Q_message.name = name
        Q_message.email = email
        Q_message.text = message

        Q_message.save()
        return HttpResponse('<h2>保存成功</h2>')
    else:
        return render(request,'msg.html')

def message_list(request):
    objs = Message.objects.all()
    context = {'objs':objs}   #return HttpResponse('<h2>请求成功</h2>')
    print(context)
    return render(request,'message-list.html',context)


