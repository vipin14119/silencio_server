from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from silencio.models import Record, User, Location
import datetime

# Login Return Values
LOGIN_OK = 1
USERNAME_DOESNT_EXIST = 2
INCORRECT_PASSWORD = 3
LOGIN_SERVER_ERROR = 4

# Signup Return Values
SIGNUP_OK = 5
USERNAME_EXIST = 6
SIGNUP_SERVER_ERROR = 7
PARAMETERS_INCORRECT = 8

# Post Record Bundle Return Values
DATETIME_FORMAT_ERROR = 9
SUCCESS_MSG = 'RECORD CREATED SUCCESSFULLY'
WRONG_METHOD = 'ITS NOT THE CORRECT METHOD FOR THIS URL'
LOCATION_DOESNT_EXIST = 10

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


def get_locations(request):
    locations = Location.objects.all()
    location_json = []
    for location in locations:
        data = get_records(location.name)
        location_json.append({
        'name': location.name,
        'mac': location.mac,
        'db': str(data[0]),
        'records': data[1]
        })
    return HttpResponse(json.dumps(location_json))

def get_records(location_name):
    records = Record.objects.filter(location__name=location_name)
    list = []
    avg = 0
    for record in records:
        avg += record.db_level
        list.append(record.db_level)
    if len(records) != 0:
        avg /= len(records)
    return (avg, list)

@csrf_exempt
def post_location(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mac = request.POST.get("mac")
        Location(name=name, mac=mac).save()
        return HttpResponse("1")
    else:
        return HttpResponse("0")

@csrf_exempt
def post_record_bundle(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            location = request.POST.get("location")
            start_time = request.POST.get("start_time")
            end_time = request.POST.get("end_time")
            db_level = float(request.POST.get("db_level"))
        except:
            return HttpResponse(PARAMETERS_INCORRECT)
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse(USERNAME_DOESNT_EXIST)
        try:
            location = Location.objects.filter(name=location)[0]
        except:
            return HttpResponse(LOCATION_DOESNT_EXIST)
        try:
            start_time = datetime.datetime.strptime(start_time, "%Y/%m/%d %H:%M:%S")
            end_time = datetime.datetime.strptime(end_time, "%Y/%m/%d %H:%M:%S")
        except:
            return HttpResponse(DATETIME_FORMAT_ERROR)
        record = Record(user=user, location=location, db_level=db_level, start_time=start_time, end_time=end_time)
        record.save()
        return HttpResponse(SUCCESS_MSG)
    else:
        return HttpResponse(WRONG_METHOD)


@ensure_csrf_cookie
def get_csrf_token(request):
    return HttpResponse("GOT NEW CSRF")


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
        except:
            return HttpResponse(PARAMETERS_INCORRECT)

        if User.objects.filter(username=username).exists():
            return HttpResponse(USERNAME_EXIST)
        else:
            User(username=username, password=password).save()
            return HttpResponse(SIGNUP_OK)
    else:
        return HttpResponse(SIGNUP_SERVER_ERROR)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
        except:
            return HttpResponse(PARAMETERS_INCORRECT)
        obj = User.objects.filter(username=username)
        if obj.exists() and obj[0].password == password:
            return HttpResponse(LOGIN_OK)
        elif obj.exists() and obj[0].password != password:
            return HttpResponse(INCORRECT_PASSWORD)
        else:
            return HttpResponse(USERNAME_DOESNT_EXIST)
    else:
        return HttpResponse(LOGIN_SERVER_ERROR)


# curl -H "Content-Type: application/x-www-form-urlencoded" -X POST --data data='{"username":"xyz","password":"xyz"}'
#  http://127.0.0.1:8000/silencio/post/
