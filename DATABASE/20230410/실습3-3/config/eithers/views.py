from django.shortcuts import render,redirect
from .models import Question, Comment
from .forms import QuestionForm, CommentForm


# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)



def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eithers:index')
        
    form = QuestionForm()
    context = {
        'form' : form,
    }
    return render(request, 'eithers/create.html',context)


def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    comments = question.comments.all()
    comment_form = CommentForm()
    context = {
        'question' : question,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'eithers/detail.html', context)


def comment(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.question = question
        comment.save()
        return redirect('eithers:detail', question_pk)
    
