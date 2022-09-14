from django import forms
from .models import Opinion,TimeLine

class Form(forms.ModelForm):
  class Meta:
    model = Opinion
    fields = ['title','content','who','student_email']
    labels = {'title':'タイトル(〇〇の改善要求など)','content':'本文','who':'お名前(匿名希望の場合は「匿名希望」)','student_number':'生徒番号'}
    widgets = {
      'title':forms.TextInput(attrs={'placeholder':'例)〇〇の修理について'}),
      'content':forms.Textarea(attrs={'placeholder':'ここに本文をお書きください'}),
      'who':forms.TextInput(attrs={'placeholder':'◯年◯組中等太郎'}),
      'student_number':forms.NumberInput(attrs={'placeholder':'00000'}),
    }

class AnswerForm(forms.ModelForm):
  class Meta:
    model = TimeLine
    fields = ['title','content']
    labels = {'title':'タイトル','content':'本文'}
    widgets = {
      'title':forms.TextInput(attrs={'placeholder':'タイトル'}),
      'content':forms.Textarea(attrs={'placeholder':'本文'}),
    }

class StatusForm(forms.ModelForm):
  class Meta:
    model = Opinion
    fields = ['status']
    widgets = {'status':forms.NumberInput(attrs={'placeholder':'number'})}