from django.shortcuts import render
from .form import TestForm

def index(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid:
            pass
    else:
        form = TestForm()
        render(request, 'index.html', context={'form': form})
        
