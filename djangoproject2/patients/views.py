from django.shortcuts import render,redirect
from .forms import EmployeeForm
from . forms import StudentForm
from students.models import Student

# Create your views here.
def employee_form(request):
    form =EmployeeForm()
    return render(request,'employee_form.html',{'form':form})
def employee_list(request):
    if request.method == 'GET':
        if id==0:
           form = StudentForm()
    else:
        employee = Student.objects.get(pk=id)
        form = StudentForm(instance=employee)
    return render(request,'employee_list.html',{'form':form})
else:
      if id ==0:
        form = StudentForm(request.POST)
        else:
          employee = Student.objects.get(pk=id)
          form = StudentForm(request.POST, instance=employee)
        if form.is_valid():
          form.save()
        return redirect('/students/show/')
