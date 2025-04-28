from django.shortcuts import render, redirect
from student.models import students_records 
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')

def courses_offered(request):
    return render(request, 'courses.html')

def cultural_events(request):
    return render(request, 'events.html')

def placement_view(request):
    return render(request, "placement.html")

def fee_structure_view(request):
    return render(request, 'fee_structure.html')

def tour(request):
    return render(request, 'tour.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('index')
        
        
        else:             # login error
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')



def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password == cpassword:
            user = User(username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect('login')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('index')