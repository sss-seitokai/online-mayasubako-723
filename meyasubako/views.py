from django.shortcuts import render
from .models import Opinion,TimeLine
from django.shortcuts import get_object_or_404, render,redirect
from .forms import Form,AnswerForm,StatusForm

# Create your views here.
def index(request):
  opinions = Opinion.objects.order_by('date_added').reverse()
  context = {'opinions':opinions}
  return render(request,"meyasubako/meyasubako.html",context)

def detail(request,opinion_id):
  opinions = Opinion.objects.get(id=opinion_id)
  timelines = TimeLine.objects.filter(opinion=opinions).all()
  context={'opinions':opinions ,'timelines':timelines}
  return render(request,"meyasubako/detail.html",context)

def form(request):
  if request.method != 'POST':
    form = Form()
  else:
    form = Form(data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('meyasubako:index')
  context = {'form':form}
  return render(request,'meyasubako/form.html',context)

def owner(request):
  opinions = Opinion.objects.order_by('date_added').reverse()
  context = {'opinions':opinions}
  return render(request,'meyasubako/owner/owner.html',context)

def answer(request,opinion_id):
  opinion = Opinion.objects.get(id=opinion_id)
  if request.method != 'POST':
    form = AnswerForm()
    status_form = StatusForm(instance=opinion)
  else:
    form = AnswerForm(data=request.POST)
    status_form = StatusForm(instance=opinion,data=request.POST)
    if form.is_valid():
      form.save(commit=False).opinion = Opinion.objects.get(id=opinion_id)
      form.save()
      if status_form.is_valid():
        status_form.save()
        return redirect('meyasubako:owner')
  context = {'form':form,'opinion':opinion,'status_form':status_form}
  return render(request,'meyasubako/owner/answer_form.html',context)

def owner_detail(request,opinion_id):
  opinions = Opinion.objects.get(id=opinion_id)
  timelines = TimeLine.objects.filter(opinion=opinions).all()
  context={'opinions':opinions ,'timelines':timelines}
  return render(request,"meyasubako/owner/owner_detail.html",context)

def edit(request,timeline_id):
  timeline = TimeLine.objects.get(id=timeline_id)
  if request.method != 'POST':
    form = AnswerForm(instance=timeline)
    status_form = StatusForm(instance=timeline.opinion)
  else:
    form = AnswerForm(instance=timeline,data=request.POST)
    status_form = StatusForm(instance=timeline.opinion,data=request.POST)
    if form.is_valid():
      form.save()
      if status_form.is_valid():
        status_form.save()
        return redirect('meyasubako:owner')
  context = {'form':form,'timeline_id':timeline_id,'status_form':status_form}
  return render(request,'meyasubako/owner/edit_form.html',context)

def delete(request,timeline_id):
  time = get_object_or_404(TimeLine,id=timeline_id)
  time.delete()
  return redirect('meyasubako:owner')

from django.http import HttpResponseRedirect

def LoginView(request):
    return HttpResponseRedirect('social:begin', dict(backend='google-oauth2'))
