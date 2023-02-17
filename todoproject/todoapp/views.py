from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from.models import Task
from . forms import TodoForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'taskk'
class TaskDetailView(DetailView):
    model = Task
    template_name = 'detailview.html'
    context_object_name = 'task'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'updated.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('todoapp:detailsview',kwargs={'pk':self.object.id})  # detailsview is name='detailsview   in views.py
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url= reverse_lazy('todoapp:index')





def index(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        Name=request.POST.get('task')
        Priority=request.POST.get('priority')
        Date=request.POST.get('dat')
        task2=Task(name=Name,priority=Priority,date=Date)   #name=field name    Name=variablename
        task2.save()
    return render(request,'index.html',{'taskk':task1})


def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)    #task is variable name
    frm=TodoForm(request.POST or None,request.FILES,instance=task)   #frm is variable name of TodoForm
    if frm.is_valid():
        frm.save()
        return redirect('/')
    return render(request,'edit.html',{'fm':frm,'taskk':task})




# def details(request):
#     task=Task.objects.all()
#     return render(request,'details.html',{'taskk':task})





