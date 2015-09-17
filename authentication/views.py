from django.shortcuts import render

from authentication.models import User
from authentication.forms import UserForm

# Create your views here.

def create_user(request):
    # u = User()
    # u.username = "jaakko1"
    # u.password = "hello kitty"
    # u.save()
    form = UserForm()
    return render(request, "authentication/auth_create.html", locals())