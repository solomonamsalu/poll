from django.shortcuts import render
from django.http import HttpResponse
 
def detail(request,question_id):
    return HttpResponse("you are looking at."%question_id)
