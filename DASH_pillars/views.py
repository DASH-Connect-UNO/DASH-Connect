from django.shortcuts import render, get_object_or_404, redirect
from .models import Scholarship, Hardship, BasicNeedSupport
from .forms import ScholarshipForm, HardshipForm, BasicNeedSupportForm
from accounts.models import Student
from accounts.forms import StudentForm

def pillars_home(request):
    return render(request, 'DASH_pillars/pillars_home.html')

def student_information(request):
    students = Student.objects.all()
    return render(request, 'student/student_information.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_information')
    else:
        form = StudentForm()
    return render(request, 'student/add_student.html', {'form': form})

def list_scholarships(request):
    scholarships = Scholarship.objects.all()
    return render(request, 'DASH_pillars/list_scholarships.html', {'scholarships': scholarships})

def add_scholarship(request):
    if request.method == 'POST':
        form = ScholarshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_scholarships')
    else:
        form = ScholarshipForm()
    return render(request, 'DASH_pillars/add_scholarship.html', {'form': form})

def edit_scholarship(request, id):
    scholarship = get_object_or_404(Scholarship, id=id)
    if request.method == 'POST':
        form = ScholarshipForm(request.POST, instance=scholarship)
        if form.is_valid():
            form.save()
            return redirect('list_scholarships')
    else:
        form = ScholarshipForm(instance=scholarship)
    return render(request, 'DASH_pillars/edit_scholarship.html', {'form': form})

def remove_scholarship(request, id):
    Scholarship.objects.get(id=id).delete()
    return redirect('list_scholarships')

def list_hardships(request):
    hardships = Hardship.objects.all()
    return render(request, 'DASH_pillars/list_hardships.html', {'hardships': hardships})

def add_hardship(request):
    if request.method == 'POST':
        form = HardshipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_hardships')
    else:
        form = HardshipForm()
    return render(request, 'DASH_pillars/add_hardship.html', {'form': form})

def edit_hardship(request, id):
    hardship = get_object_or_404(Hardship, id=id)
    if request.method == 'POST':
        form = HardshipForm(request.POST, instance=hardship)
        if form.is_valid():
            form.save()
            return redirect('list_hardships')
    else:
        form = HardshipForm(instance=hardship)
    return render(request, 'DASH_pillars/edit_hardship.html', {'form': form})

def remove_hardship(request, id):
    Hardship.objects.get(id=id).delete()
    return redirect('list_hardships')

def list_basic_need_supports(request):
    basic_need_supports = BasicNeedSupport.objects.all()
    return render(request, 'DASH_pillars/list_basic_need_supports.html', {'basic_need_supports': basic_need_supports})

def add_basic_need_support(request):
    if request.method == 'POST':
        form = BasicNeedSupportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_basic_need_supports')
    else:
        form = BasicNeedSupportForm()
    return render(request, 'DASH_pillars/add_basic_need_support.html', {'form': form})

def edit_basic_need_support(request, id):
    basic_need_support = get_object_or_404(BasicNeedSupport, id=id)
    if request.method == 'POST':
        form = BasicNeedSupportForm(request.POST, instance=basic_need_support)
        if form.is_valid():
            form.save()
            return redirect('list_basic_need_supports')
    else:
        form = BasicNeedSupportForm(instance=basic_need_support)
    return render(request, 'DASH_pillars/edit_basic_need_support.html', {'form': form})

def remove_basic_need_support(request, id):
    BasicNeedSupport.objects.get(id=id).delete()
    return redirect('list_basic_need_supports')
