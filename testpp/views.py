from django.shortcuts import render
from .forms import Form
from django.http import HttpResponse
from .models import FormModel 
# Create your views here.
def FormView(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your review has been taken')
  
    else:
        form = Form()
        context = {'form':form,}
    return render(request, 'index.html', context)
