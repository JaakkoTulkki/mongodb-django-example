from django.shortcuts import render

from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from authentication.models import User
from authentication.serializers import UserSerializer
from authentication.forms import UserForm



# Create your views here.

def create_user(request):
    # u = User()
    # u.username = "jaakko1"
    # u.password = "hello kitty"
    # u.save()
    form = UserForm()
    return render(request, "authentication/auth_create.html", locals())


class UserView(views.APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if not pk:
            users = User.objects()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        try:
            user = User.objects.get(pk=pk)
        except:
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        else:
            serializer = UserSerializer(user)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response({})
