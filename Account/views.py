from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib import auth

# Create your views here.
class Login(APIView):
    def get(self, request):
        return render(request, 'Account/login.html')
    def post(self, request):
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        error = "Login details error"
        print(error)
        return redirect('login')

class Home(APIView):
    def get(self, request):
        return render(request, 'Account/home.html')

class Logout(APIView):
    def get(self, request):
        auth.logout(request)
        return redirect('login')
