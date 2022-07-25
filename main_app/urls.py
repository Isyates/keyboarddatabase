from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name = 'home'),
path('about/', views.about, name = 'about'),
path('keyboards/', views.keyboards_index, name = 'keyboards_index'),
path('keyboards/create/', views.KeyboardCreate.as_view(), name = 'keyboards_create'),
path('keyboard/<int:keyboard_id>/', views.keyboards_detail, name='detail'),
path('keyboard/<int:pk>/delete/', views.KeyboardDelete.as_view(), name='keyboards_delete'),
path('keyboards/<int:pk>/update/', views.KeyboardUpdate.as_view(), name = 'keyboards_update'),
path('accounts/signup/', views.signup, name='signup'),
]