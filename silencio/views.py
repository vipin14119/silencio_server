from django.shortcuts import render
from django.http import HttpResponse
import json

def get_data(request):
    obj1 = {
    "name" : "Vipin Chaudhary",
    "roll_no" : 2014119,
    "college" : "IIIT Delhi",
    "weight" : float(61.8)
    }
    obj2 = {
    "name" : "Monu Chaudhary",
    "roll_no" : 2014120,
    "college" : "IIIT Delhi",
    "weight" : float(64.8)
    }
    obj3 = {
    "name" : "Shrishtee Gupta",
    "roll_no" : 2014118,
    "college" : "IIIT Delhi",
    "weight" : float(49.8)
    }
    return HttpResponse(json.dumps([obj1, obj2, obj3]))
