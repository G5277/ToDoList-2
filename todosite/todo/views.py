from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy




# Views

class HomePageView(ListView):
    model = Item
    template_name = "home.html"

class TaskCreateView(CreateView):
    model = Item
    template_name = 'createtask.html'
    fields = ["task", "description", "date"]
    success_url = reverse_lazy('home')

class TaskDetailView(DetailView):
    model = Item
    template_name = 'taskdetail.html'
    # fields = ["task", "description", "date"]

class TaskDeleteView(DeleteView):
    model = Item
    template_name = 'taskdelete.html'
    success_url = reverse_lazy('home')

class TaskSearchView(ListView):
    model = Item
    template_name = 'home.html'
    queryset = Item.objects.all()

    def get_queryset(self):
        result = self.request.GET.get('search_term')
        return Item.objects.filter(task__icontains = result)