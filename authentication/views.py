from django.shortcuts import render

from authentication.models import User

# Create your views here.

def create_user(request):
    u = User()
    u.username = "jaakko"
    u.save()
    return render(request, "authentication/auth_create.html")