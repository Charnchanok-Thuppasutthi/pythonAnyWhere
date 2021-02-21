from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Word ,Mean
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'vocab/index.html'
    context_object_name = 'word_list'
    def get_queryset(self):
        return Word.objects.all()

class DetailView(generic.DetailView):
    model = Word
    template_name = 'vocab/detail.html'
    def get_queryset(self):
        return Word.objects.all()

def addWordView(request):
    return render(request, 'vocab/addWord.html')

def submit(request):
    word = request.POST.get("word")
    mean = request.POST.get("mean")
    text = request.POST.get("type")
    newWord = Word(word_text = word)
    newWord.save()
    newWord.mean_set.create( mean_text = mean , type_text = text)
    newWord.save()

    return render(request , 'vocab/addWord.html' )