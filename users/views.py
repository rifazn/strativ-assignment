from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            newuser = form.save()
            login(request, newuser)
            return redirect('restcountries:index')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
