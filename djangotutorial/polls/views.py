from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from .models import Question


# Create your views here.
#Vista principal
def index(request):
	latest_question_list = Question.objects.order_by("-pub_date")[:5]
	context = {"latest_question_list": latest_question_list}
	return render(request, "polls/index.html", context)

#vista muestra el detalle de una pregunta
def detail(request, question_id):
	
		question = get_object_or_404(Question, pk=question_id) #me devuelve el objeto o un error 404 si no existe
		return render(request, "polls/detail.html", {"question": question})

#vista de resultados
def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

#vista para votar
def vote(request, question_id):
	return HttpResponse("You're voting on questions %s." % question_id)
