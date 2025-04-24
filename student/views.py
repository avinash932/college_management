from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from student.models import students_records
from django.db.models import Q

# Create your views here.

def student(request):

    return render(request, 'student.html',
    
    context={
        'students':students_records.objects.all()
    }
    )

def add_student_view(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        rollno = request.POST.get('rollno')
        email = request.POST.get('email')  # not stored yet
        course = request.POST.get('course')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Create and save the new student record
        student = students_records(
            stu_id=rollno,
            name=name,
            course=course,
            address=address,
            contact=phone
        )
        student.save()
        return redirect('student')  # or wherever you want to redirect after submission

    return render(request, 'add_student.html')





#search students


def student(request):
    search_query = request.GET.get('search', '')

    if search_query:
        students = students_records.objects.filter(
            Q(name__icontains=search_query) |
            Q(course__icontains=search_query) |
            Q(stu_id__icontains=search_query)
        )
    else:
        students = students_records.objects.all()

    return render(request, 'student.html', {
        'students': students,
        'search_query': search_query
    })



# Delete student
def delete_student(request, student_id):
    student = get_object_or_404(students_records, stu_id=student_id)
    student.delete()
    return redirect('student')

# Edit student
def edit_student(request, student_id):
    student = get_object_or_404(students_records, stu_id=student_id)

    if request.method == 'POST':
        student.name = request.POST.get('fullname')
        student.course = request.POST.get('course')
        student.contact = request.POST.get('phone')
        student.address = request.POST.get('address')
        student.save()
        return redirect('student')

    return render(request, 'edit_student.html', {'student': student})




def add_student_view(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('fullname')
        rollno = request.POST.get('rollno')
        course = request.POST.get('course')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')

        student = students_records(
            stu_id=rollno,
            name=name,
            course=course,
            contact=phone,
            email=email,
            address=address
        )
        student.save()
        return redirect('student')

    return render(request, 'add_student.html', {
        'title': 'Add New Student',
        'button_text': 'Add Student',
        'student': None  # No student for add
    })


def edit_student(request, student_id):
    student = get_object_or_404(students_records, stu_id=student_id)

    if request.method == 'POST':
        # Update the student's details
        student.name = request.POST.get('fullname')
        student.course = request.POST.get('course')
        student.contact = request.POST.get('phone')
        student.email = request.POST.get('email')
        student.address = request.POST.get('address')
        student.save()
        return redirect('student')

    return render(request, 'add_student.html', {
        'title': 'Edit Student',
        'button_text': 'Update Student',
        'student': student  # Pre-fill data for editing
    })




def fee_view(request):
    queryset = students_records.objects.all()

    course = request.GET.get('course', '').strip()
    branch = request.GET.get('branch', '').strip()
    year = request.GET.get('year', '').strip()
    status = request.GET.get('status', '').strip()

    if course:
        queryset = queryset.filter(course__iexact=course)
    if branch:
        queryset = queryset.filter(branch__iexact=branch)
    if year:
        queryset = queryset.filter(year=year)
    if status:
        queryset = queryset.filter(fee_status__iexact=status)

    return render(request, 'fee.html', {
        'fees': queryset
    })

