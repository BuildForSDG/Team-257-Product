from django.shortcuts import render

# homepage
def welcome(request):
    return render(request, 'website/welcome.html')

