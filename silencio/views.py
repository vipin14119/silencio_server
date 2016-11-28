from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from silencio.models import Record, User

def get_data(request):
    obj1 = {
    "name" : "Vipin Chaudhary",
    "roll_no" : 2014119,
    "college" : "IIIT Delhi",
    "weight" : float(61.8)
    }
    obj2 = {
    "name" : "Sonia Kauhsik",
    "roll_no" : 2014120,
    "college" : "IIIT Delhi",
    "weight" : float(48)
    }
    obj3 = {
    "name" : "Manisha Gupta",
    "roll_no" : 2014118,
    "college" : "IIIT Delhi",
    "weight" : float(49.8)
    }
    return HttpResponse(json.dumps([obj1, obj2, obj3]))


@csrf_exempt
def post_data(request):
    if request.method == "POST":
        names = str(request.POST.get("name"))
        db_level = float(request.POST.get("db_level"))
        Record(name=names, db_level=db_level).save()
        # data = json.loads(request.POST.get('data'))
        # print data['username']
        return render(request, 'silencio/index.html', {'request_data': request.POST})
    else:
        return HttpResponse("didnt get post data")


@ensure_csrf_cookie
def get_csrf_token(request):
    return HttpResponse("GOT NEW CSRF")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        User(username=username, password=password).save()
        return HttpResponse("1")
    else:
        return HttpResponse("-1")


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username, password=password).exists():
            return HttpResponse("1")
        else:
            return HttpResponse("-1")
    else:
        return HttpResponse("0")


# curl -H "Content-Type: application/x-www-form-urlencoded" -X POST --data data='{"username":"xyz","password":"xyz"}'
#  http://127.0.0.1:8000/silencio/post/
