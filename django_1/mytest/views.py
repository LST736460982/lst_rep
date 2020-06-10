from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime
from mytest.forms import Mail
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django import template
register=template.Library()
def hello(request):
    return HttpResponse("Hello World!")
def date_time(request):
    now=datetime.datetime.now()
    return HttpResponse("this time is %s"%now)
def hour_del(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    return HttpResponse("after %s hours is %s"%(offset,dt))
def position(request):
    pos={'site':"重庆邮电大学"}
    return render(request,'test_1.txt',pos)
def current_time(request):
    now=datetime.datetime.now()
    time={'current_time':now}
    return render(request,'time.html',time)
@csrf_exempt
def contact(request):
    if request.method=='POST':
        form=Mail(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            send_mail(data['subject'],data['message'],['lst123456@qq.com'],[data['email'],])
            return render(request,'mail.txt',{'sucess':'发送成功','form':form})
    else:
        form=Mail()
    return render(request,'mail.txt',{'form':form})
def list(request):
    article=[{'title':'蚊香','body':'可快速消灭蚊虫'},{'title':'书','body':'人丑就要多读书'}]
    return render(request,'list.html',{'articles':article})
@register.simple_tag
def value(v1,v2):
    return v1+v2
def test(request):
    return render(request,'albums-store.html')
# Create your views here.
