from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone

class IndexView(generic.ListView):#เมื่อมีการ request path polls/ จะทำการเรียกหน้า index.html
    template_name = 'polls/index.html'
    context_object_name = 'sorted_question_list'

    def get_Vote(self,index):#นับจำนวน vote ของ question ตัวนั้น
        q = Question.objects.get(pk=index+1)
        choice_all = q.choice_set.all()
        sumVote=0
        for j in range( choice_all.count() ):
            sumVote += choice_all[j].votes
        return sumVote

    def get_ListVote(self):
        sumList = []
        for i in range(Question.objects.count()): 
            sumList.append(self.get_Vote(i)) 
        return sumList
        
    def sort_Qusetion(self):
        Sorted_Question = []
        sumList = self.get_ListVote()
        temp = list(sumList)
        temp.sort(reverse=True)
        for i in range(len(temp)): #ตรวจสอบเทียบหาตัวเท่ากันและใส่indexเก่ามาเรียงใหม่
            for j in range(len(temp)):
                if temp[i] == sumList[j]:
                    print(sumList[j])
                    Sorted_Question.append(Question.objects.get(pk=j+1))
                    print(Sorted_Question)
                    break
        return Sorted_Question
            
    def get_queryset(self):
        try:
            QuestionList = self.sort_Qusetion()
        except:Question.objects.count()==0
            
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return QuestionList
        #return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):#เมื่อมีการ request จากการกด Question จากหน้า index.html จะทำการเปิด detail.html
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):#ไปเรียกหน้า result.html ใน templates/polls มาแสดง
    model = Question
    template_name = 'polls/results.html'


def menu(request):
    return render(request, 'polls/homepage.html')

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote_set.create(vote_date=timezone.now())
        '''
            add new one voted time to vote table
        '''
        selected_choice.votes += 1  #increase number of that vote
        selected_choice.save()  #save modified attribute 
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))