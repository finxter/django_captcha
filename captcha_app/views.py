from django.shortcuts import render
from .forms import CaptchaForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = CaptchaForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Success!')
        else:
            messages.error(request, 'Wrong Captcha!')
    form = CaptchaForm()
    return render(request, 'index.html', {'form': form})
