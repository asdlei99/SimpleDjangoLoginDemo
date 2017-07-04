#_*_coding:UTF-8_*_
from django.shortcuts import render_to_response, Http404
from django.http.response import HttpResponse

from db import models
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def login_page(request):
    return render_to_response('login_page.html',context_instance=RequestContext(request))

@csrf_exempt
def login_submit(request):
    if request.method == 'POST':
        ret = {}
        u = request.POST.get('user', '').strip()
        p = request.POST.get('pass', '').strip()
        user_obj = models.Users.objects.filter(username=u, password=p)
        if user_obj.count() == 1:
            ret['username'] = user_obj[0].username
            #HttpResponseRedirect('/', ret)
            return render_to_response('index.html', ret)
        else:
            return HttpResponse('用户名或密码错误')
    else:
        raise Http404