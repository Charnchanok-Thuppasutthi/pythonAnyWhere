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

class DetailView(generic.DetailView):#เมื่อมีการ request จากการกด Question จากหน้า index.html จะทำการเปิด detail.html
    model = Word
    template_name = 'vocab/detail.html'
    def get_queryset(self):
        return Word.objects.all()