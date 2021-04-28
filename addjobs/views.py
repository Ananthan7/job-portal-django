from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.
from addjobs.forms import JobForm
from addjobs.models import Jobs


def home(request):
    li = Jobs.objects.all()
    return render(request, 'home.html', {'job': li})
def addjob(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request, 'addjob.html', {'form': form})

def jobview(request):
    list = Jobs.objects.all()
    return render(request, 'jobview.html', {'job': list})


def signup(request):
    # builtin form
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request, 'signup.html', {'form': form})