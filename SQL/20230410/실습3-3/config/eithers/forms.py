from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        labels = {
            'issue_a' : 'RED TEAM',
            'issue_b' : 'BLUE TEAM',
        }

class CommentForm(forms.ModelForm):
    pick = forms.ChoiceField(choices=[('0','RED TEAM'),('1','BLUE TEAM')])
    class Meta:
        model = Comment
        exclude = ('question',)