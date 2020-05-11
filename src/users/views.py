from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# sign in/login
def registerPage(request):
    form = UserCreationForm

    #validation code
    if request.method == 'POST':
        form = UserCreationForm(request)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'users/login.html', context)