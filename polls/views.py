from re import S
from this import s
from django.shortcuts import render
from django.http import HttpResponse
 

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
    
