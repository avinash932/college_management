from django.shortcuts import render, redirect, get_object_or_404
from student.models import students_records
from django.db.models import Q, Sum
import traceback

# View Students (with Search + Stats)
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
        'search_query': search_query,
        'total_students': students_records.objects.count(),
        'total_fees': students_records.objects.aggregate(Sum('fee_paid'))['fee_paid__sum'] or 0,
    })

# Add Student
def add_student_view(request):
    if request.method == 'POST':
        try:
            # Get form data
            fullname = request.POST.get('fullname', '')
            rollno = request.POST.get('rollno', '')
            course = request.POST.get('course', '')
            email = request.POST.get('email', '')
            address = request.POST.get('address', '')
            phone = request.POST.get('phone', '')
            branch = request.POST.get('branch', '')
            year_raw = request.POST.get('year')
            fee_paid_raw = request.POST.get('fee_paid', '0')

            fee_paid = int(fee_paid_raw) if fee_paid_raw.isdigit() else 0
            year = int(year_raw) if year_raw and year_raw.isdigit() else 1

            student = students_records(
                stu_id=rollno,
                name=fullname,
                course=course,
                branch=branch,
                year=year,
                address=address,
                contact=phone,
                email=email,
                fee_paid=fee_paid,
                fee_total=80000
            )
            student.save()
            return redirect('student')

        except Exception as e:
            print("Error saving student:", e)
            traceback.print_exc()
            return render(request, 'add_student.html', {
                'student': request.POST,
                'error': 'Failed to save student. Please check your input.'
            })

    return render(request, 'add_student.html', {
        'title': 'Add New Student',
        'button_text': 'Add Student',
        'student': None
    })

# Edit Student
def edit_student(request, student_id):
    student = get_object_or_404(students_records, stu_id=student_id)

    if request.method == 'POST':
        student.name = request.POST.get('fullname')
        student.course = request.POST.get('course')
        student.contact = request.POST.get('phone')
        student.email = request.POST.get('email')
        student.address = request.POST.get('address')
        student.fee_paid = request.POST.get('fee_paid')
        student.save()
        return redirect('student')

    return render(request, 'add_student.html', {
        'title': 'Edit Student',
        'button_text': 'Update Student',
        'student': student
    })

# Delete Student
def delete_student(request, student_id):
    student = get_object_or_404(students_records, stu_id=student_id)
    student.delete()
    return redirect('student')

# Fee View with Filters
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
