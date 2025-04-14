from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	context = {"latest_question_list": latest_question_list}
	return render(request, "polls/index.html", context)
		# render(solicitud HTTP del usuario, ruta del template que va a renderizar, diccionario con los datos)

def detail(request, question_id):
	return HttpResponse("You're looking at questions %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on questions %s." % question_id)
