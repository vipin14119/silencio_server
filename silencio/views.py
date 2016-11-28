from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from silencio.models import Record, User

OK_FLAG = "1"
NOTOK_FLAG = "0"
BAD_FLAG = "-1"


def get_data(request):
    obj1 = {
        "name": "Vipin Chaudhary",
        "roll_no": 2014119,
        "college": "IIIT Delhi",
        "weight": float(61.8)
    }
    obj2 = {
        "name": "Sonia Kauhsik",
        "roll_no": 2014120,
        "college": "IIIT Delhi",
        "weight": float(48)
    }
    obj3 = {
        "name": "Manisha Gupta",
        "roll_no": 2014118,
        "college": "IIIT Delhi",
        "weight": float(49.8)
    }
    return HttpResponse(json.dumps([obj1, obj2, obj3]))


@csrf_exempt
def post_record(request):
    if request.method == "POST":
        username = request.POST.get("username")
        user = User.objects.get(username=username)
        place = request.POST.get("name")
        db_level = float(request.POST.get("db_level"))
        Record(user=user, name=place, db_level=db_level).save()
        # data = json.loads(request.POST.get('data'))
        # print data['username']
        return HttpResponse(OK_FLAG)
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
        return HttpResponse(OK_FLAG)
    else:
        return HttpResponse(BAD_FLAG)


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username, password=password).exists():
            return HttpResponse(OK_FLAG)
        else:
            return HttpResponse(BAD_FLAG)
    else:
        return HttpResponse(NOTOK_FLAG)


# curl -H "Content-Type: application/x-www-form-urlencoded" -X POST --data data='{"username":"xyz","password":"xyz"}'
#  http://127.0.0.1:8000/silencio/post/
