from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.
def index(request):
    # order_by('-pub_date')[:5] : 등록 날짜 기준 내림차순 정렬 후 앞에서 5개까지만
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    # 지난 실습에서 render() 함수의 {~:~} 로 html 파일에게 넘겨주던 dict를 context라고 부릅니다.
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) 



def detail(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'question':q})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})
 

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice_select'])
    except:
        context = {'question':question, 'error_message':"You didn't select a choice"}
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question_id=question.id)
