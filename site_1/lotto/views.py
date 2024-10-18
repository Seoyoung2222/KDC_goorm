from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm


# Create your views here.
def index(request):

    # <input name='name' type='text'></input>
    # <input name='text' type='text'></input>
    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html', {'lottos':lottos})

def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, "lotto/form.html", {"form":form})
    
    form = PostForm()
    return render(request, "lotto/form.html", {"form":form})

def hello(request):
    data = GuessNumbers.objects.all()
    data = GuessNumbers.objects.get()
    return render(request, 'lotto/default.html',{})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(id = lottokey)
    return render(request, "lotto/detail.html", {"lotto": lotto})
