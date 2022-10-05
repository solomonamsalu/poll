from multiprocessing import context
from re import S
from this import s
from django.shortcuts import render
from django.http import HttpResponse,Http404
from polls.models import Questions
from django.template import loader

def index(request):
    latest_question_list=Questions.objects.order_by('pub_date')[:5]
    # template=loader.get_template("polls/index.html")
    context={
        "latest_question_list":latest_question_list,
    }
    # return HttpResponse(template.render(context,request))
    return  render (request, 'polls/index.html', context)
def detail(request, question_id):
        try:
            question=Questions.objects.get(pk=question_id)
        except Questions.DoesNotExist:
                raise Http404("Question does not exist" )
        context={
            "question":question
        }
        return render(request,'polls/detail.html',context)
def results(request,question_id):
    response="you are looking at the result of %s." 
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("you are votig on question %s"%question_id)
