# Create your views here.
from django.shortcuts import render
from .forms import Studentform
from .models import Student
from django.http import HttpResponse

# Create your views here.
def studview(request):
    form=Studentform()
    template_name="app/stud.html"
    context={'form':form}
    if request.method=="POST":
        form=Studentform(request.POST)
        if form.is_valid():
            i=form.cleaned_data['sid']
            n=form.cleaned_data['snm']
            e=form.cleaned_data['sem']
            stud=Student(ids=i,nm=n,em=e)
            stud.save()
            return HttpResponse('<h1>Data saved...</h1>')
    return render(request,template_name,context)
