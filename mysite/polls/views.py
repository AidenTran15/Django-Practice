from django.shortcuts import HttpResponse

# Create your views here.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." & question_id)

def result(request, question_id):
   response = "You're looking at the results of question %s."
   return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)