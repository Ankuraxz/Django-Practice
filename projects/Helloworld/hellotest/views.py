from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Ankur'})


def add(request):
    num1 = float(request.GET['num1'])
    num2 = float(request.GET['num2'])
    x = int(request.GET['places'])
    res = str(round((num1 + num2), x))
    return render(request, 'result.html', {'sum': res})
