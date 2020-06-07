from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime
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
# Create your views here.
