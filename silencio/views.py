from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

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
        data = json.loads(request.POST.get('data'))
        print data['username']
        return HttpResponse("got it")
    else:
        return HttpResponse("didnt get post data")


@ensure_csrf_cookie
def get_csrf_token(request):
    return HttpResponse("GOT NEW CSRF")



# curl -H "Content-Type: application/x-www-form-urlencoded" -X POST --data data='{"username":"xyz","password":"xyz"}' http://127.0.0.1:8000/silencio/post/
