from django.shortcuts import render
from .models import ads,contacts


# Create your views here.
def index(request):
    ad1 = ads()
    ad1.name = "Dynamic Ad"
    ad1.desc = "This Ad is Dynamic, Django is doing this shit"
    ad1.img = "https://upload.wikimedia.org/wikipedia/commons/2/2a/New_Logo_AD.jpg"
    return render(request, 'index.html', {'about': 'This About Us is Dynamic',
                                          'ad1': ad1})
def contact(request):
    contact1 = contacts()

    contact1.name = str(request.POST['name'])
    contact1.email = str(request.POST['email'])
    contact1.phone = int(request.POST['phone'])
    contact1.message = str(request.POST['message'])
    return render(request, 'index.html', {'status': True})

def subscribe(request):
    email = str(request.GET['email'])
    return render(request, 'index.html', {'substatus': True})
