from django.shortcuts import render
from django.shortcuts import render, redirect # 追記
from .forms import InputForm # 追記


def index(request):
    return render(request, 'inputform/index.html')

# お問い合わせフォーム画面
def input_form(request):
    return render(request, 'inputform/input_form.html')

# 送信完了画面
def complete(request):
    return render(request, 'inputform/complete.html')

def input_form(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            return redirect('inputform:complete')
    else:
        form = InputForm()
    return render(request, 'inputform/input_form.html', {'form': form})
