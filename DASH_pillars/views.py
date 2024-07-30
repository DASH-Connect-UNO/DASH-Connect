from django.shortcuts import render, redirect
from .models import Scholarship, Hardship, BasicNeedSupport


def pillars_home(request):
    return render(request, 'DASH_pillars/pillars_home.html')

def list_scholarships(request):
    scholarships = Scholarship.objects.all()
    return render(request, 'DASH_pillars/list_scholarships.html', {'scholarships': scholarships})

def add_scholarship(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Scholarship.objects.create(name=name)
        return redirect('list_scholarships')
    return render(request, 'DASH_pillars/add_scholarship.html')

def remove_scholarship(request, id):
    Scholarship.objects.get(id=id).delete()
    return redirect('list_scholarships')

def edit_scholarship(request, id):
    scholarship = Scholarship.objects.get(id=id)
    if request.method == 'POST':
        scholarship.name = request.POST.get('name')
        scholarship.save()
        return redirect('list_scholarships')
    return render(request, 'DASH_pillars/edit_scholarship.html', {'scholarship': scholarship})

def list_hardships(request):
    hardships = Hardship.objects.all()
    return render(request, 'DASH_pillars/list_hardships.html', {'hardships': hardships})

def add_hardship(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Hardship.objects.create(name=name)
        return redirect('list_hardships')
    return render(request, 'DASH_pillars/add_hardship.html')

def remove_hardship(request, id):
    Hardship.objects.get(id=id).delete()
    return redirect('list_hardships')

def edit_hardship(request, id):
    hardship = Hardship.objects.get(id=id)
    if request.method == 'POST':
        hardship.name = request.POST.get('name')
        hardship.save()
        return redirect('list_hardships')
    return render(request, 'DASH_pillars/edit_hardship.html', {'hardship': hardship})

def list_basic_need_supports(request):
    basic_need_supports = BasicNeedSupport.objects.all()
    return render(request, 'DASH_pillars/list_basic_need_supports.html', {'basic_need_supports': basic_need_supports})

def add_basic_need_support(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        BasicNeedSupport.objects.create(name=name)
        return redirect('list_basic_need_supports')
    return render(request, 'DASH_pillars/add_basic_need_support.html')

def remove_basic_need_support(request, id):
    BasicNeedSupport.objects.get(id=id).delete()
    return redirect('list_basic_need_supports')

def edit_basic_need_support(request, id):
    basic_need_support = BasicNeedSupport.objects.get(id=id)
    if request.method == 'POST':
        basic_need_support.name = request.POST.get('name')
        basic_need_support.save()
        return redirect('list_basic_need_supports')
    return render(request, 'DASH_pillars/edit_basic_need_support.html', {'basic_need_support': basic_need_support})