from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Ankur'})


def add(request): #GET REQUEST
    num1 = float(request.POST['num1'])
    num2 = float(request.POST['num2'])
    x = int(request.POST['places'])
    res = str(round((num1 + num2), x))
    return render(request, 'result.html', {'sum': res})
