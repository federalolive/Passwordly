from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('passwords/', views.vaults_index, name='index'),
    path('vaults/<int:vault_id>/', views.vaults_detail, name='detail'),
    path('vaults/<int:pk>/delete/', views.VaultDelete.as_view(), name='vaults_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('vaults/<int:pk>/update/', views.VaultUpdate.as_view(), name='vaults_update'),
    path('accounts/signup/', views.signup, name='signup'),
    path('password/', views.generate_password, name='password'),
    path('passwords/add_pw/', views.add_passwordgenerator, name='add_gen_pass'),
    
]