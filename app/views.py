from django.shortcuts import render
from .form import TestForm

def index(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            # 获取表单数据
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            # 跳转到结果页
            return render(request, 'app/result.html', context={'name': name, 'age': age})
        else:
            # 表单验证失败，返回表单页
            return render(request, 'index.html', context={'form': form})
    else:
        form = TestForm()
    return render(request, 'index.html', context={'form': form})