"""View to show the vote for Cat or Dog"""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

# Create your views here.
from .models import Question, Choice

def home(request):
    """Only look at the last 10 questions"""
    questions = Question.objects.order_by('-pub_date')[:10]
    context = {'questions': questions}
    return render(request, 'vote/home.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        vote_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        """redirect to the page"""
        return render(request, 'vote/vote.html', {
        'question': question,
        })
    else:
        vote_choice.votes += 1
        vote_choice.save()
        return redirect('vote:results', question.id)


def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'vote/results.html', context)

def resultsData(request, obj):
    vote_info = []
    question = Question.objects.get(id=obj)
    choice = question.choice_set.all()

    for i in choice:
        vote_info.append({i.choice_text:i.votes})

    return JsonResponse(vote_info, safe=False)
