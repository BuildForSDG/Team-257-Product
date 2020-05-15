from django.shortcuts import render

# homepage
def welcome(request):
    return render(request, 'website/welcome.html')

def about(request):
    return render(request, 'website/about.html')

