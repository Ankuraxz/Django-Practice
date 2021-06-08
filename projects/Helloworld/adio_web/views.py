from django.shortcuts import render
from .models import ads


# Create your views here.
def index(request):
    ad1 = ads()
    ad1.name = "Dynamic Ad"
    ad1.desc = "This Ad is Dynamic, Django is doing this shit"
    ad1.img = "https://upload.wikimedia.org/wikipedia/commons/2/2a/New_Logo_AD.jpg"
    return render(request, 'index.html', {'about': 'This About Us is Dynamic',
                                          'ad1': ad1})
