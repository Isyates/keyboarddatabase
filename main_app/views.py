from multiprocessing import context
from django.shortcuts import render
from .models import Keyboard
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm

class KeyboardCreate(CreateView):
  model = Keyboard
  fields = '__all__'


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def keyboards_index(request):

  if request.GET.get('Case_Color'):
    featured_filter = request.GET.get('Case_Color')
    keyboards = Keyboard.objects.filter(Case_Color=featured_filter)
  else:
    keyboards = Keyboard.objects.all()
    
  if request.GET.get('Case_Material'):
    featured_filter2 = request.GET.get('Case_Material')
    keyboards = Keyboard.objects.filter(Case_Material=featured_filter2)
  elif request.GET.get('Case_Material') == '':
    keyboards = Keyboard.objects.all()
  return render(request, 'keyboards/index.html', {'keyboards': keyboards})
  

def keyboards_detail(request,keyboard_id):
  keyboard = Keyboard.objects.get(id = keyboard_id)
  return render(request,'keyboards/detail.html', {'keyboard': keyboard})

class KeyboardDelete(DeleteView):
  model = Keyboard
  success_url = '/keyboards/'

class KeyboardUpdate(UpdateView):
  model = Keyboard
  fields = '__all__'