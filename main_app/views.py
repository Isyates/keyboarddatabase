from multiprocessing import context
from .models import Keyboard
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

class KeyboardCreate(CreateView):
  model = Keyboard
  fields = '__all__'
  success_url = '/keyboards/'


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def keyboards_index(request):


# Case Color Filter

  if request.GET.get('Case_Color'):
    featured_filter = request.GET.get('Case_Color')
    keyboards = Keyboard.objects.filter(Case_Color=featured_filter)
  elif request.GET.get('Case_Color') == '':
    keyboards = Keyboard.objects.all()
    
# Case Material Filter 
  if request.GET.get('Case_Material'):
    featured_filter2 = request.GET.get('Case_Material')
    keyboards = Keyboard.objects.filter(Case_Material=featured_filter2)
  elif request.GET.get('Case_Material') == '':
    keyboards = Keyboard.objects.all()

    # Case Size Filter 
  if request.GET.get('Case_Size'):
    featured_filter3 = request.GET.get('Case_Size')
    keyboards = Keyboard.objects.filter(Case_Size=featured_filter3)
  elif request.GET.get('Case_Size') == '':
    keyboards = Keyboard.objects.all()

    # Case Layout Filter 
  if request.GET.get('Case_Layout'):
    featured_filter4 = request.GET.get('Case_Layout')
    keyboards = Keyboard.objects.filter(Case_Layout=featured_filter4)
  elif request.GET.get('Case_Layout') == '':
    keyboards = Keyboard.objects.all()


# Plate Material Filter 
  if request.GET.get('Plate_Material'):
    featured_filter5 = request.GET.get('Plate_Material')
    keyboards = Keyboard.objects.filter(Plate_Material=featured_filter5)
  elif request.GET.get('Plate_Material') == '':
    keyboards = Keyboard.objects.all()

  if request.GET.get('Plate_Color'):
    featured_filter8 = request.GET.get('Plate_Color')
    keyboards = Keyboard.objects.filter(Plate_Color=featured_filter8)
  elif request.GET.get('Plate_Color') == '':
    keyboards = Keyboard.objects.all()

  # Switch Style Filter 
  if request.GET.get('Switch_Style'):
    featured_filter7 = request.GET.get('Switch_Style')
    keyboards = Keyboard.objects.filter(Switch_Style=featured_filter7)
  elif request.GET.get('Switch_Style') == '':
    keyboards = Keyboard.objects.all()

  # Switch Style Filter 
  if request.GET.get('Keycap_Color'):
    featured_filter9 = request.GET.get('Keycap_Color')
    keyboards = Keyboard.objects.filter(Keycap_Color=featured_filter9)
  elif request.GET.get('Keycap_Color') == '':
    keyboards = Keyboard.objects.all()

  return render(request, 'keyboards/index.html', {'keyboards': keyboards})
  

  

def keyboards_detail(request,keyboard_id):
  keyboard = Keyboard.objects.get(id = keyboard_id)
  return render(request,'keyboards/detail.html', {'keyboard': keyboard})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      return redirect('keyboards_index')
    else:
      error_message = "invalid sign-up, please try again."
  form = UserCreationForm()
  context = {"form": form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)





class KeyboardDelete(DeleteView):
  model = Keyboard
  success_url = '/keyboards/'

class KeyboardUpdate(UpdateView):
  model = Keyboard
  fields = '__all__'