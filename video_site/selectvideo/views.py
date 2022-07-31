from django.db import IntegrityError
from django.forms import ValidationError
from django.utils.translation import gettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .form import UserForm

def index(request):
    return HttpResponse("Hello, world.")

def createUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            new_user = User(username=email, password=password)
            
            try:
                new_user.save()
                return HttpResponseRedirect(reverse('selectvideo:index'))
            except:
                form.add_error(None, error=ValidationError(
                    _("An account with that email already exists"),
                    code="duplicate"
                ))
            
    
    else:
        form = UserForm()
    
    return render(request, 'registration/create-user.html', {'form': form})