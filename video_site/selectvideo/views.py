from django.forms import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from selectvideo.form import UserForm
from .models import Title
import logging


@login_required()
def index(request):
    movies = Title.objects.all
    return render(request, 'selectvideo/index.html', {'movies': movies})


def createUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                new_user = form.save()
                login(request, new_user)
                return redirect('selectvideo:index')
            except IntegrityError:
                form.add_error(None, error=ValidationError(
                    _("An account with that email already exists"),
                    code="duplicate"
                ))
            except:
                logging.exception('')

    else:
        form = UserForm()

    return render(request, 'registration/create-user.html', {'form': form})
