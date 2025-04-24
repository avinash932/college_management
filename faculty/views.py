from .models import faculty
from django.shortcuts import render



def faculty_view(request):

    return render(request, 'faculty.html',
    
    context={
        'Faculty':faculty.objects.all()
    }
    )