from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from django.contrib.auth.mixins import LoginRequiredMixin
import string, random
from .models import Vault
from .forms import PasswordGeneratorForm, VaultForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid credentials - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class VaultCreate(LoginRequiredMixin, CreateView):
    model = Vault
    fields = ['name', 'site', 'description', 'pw']

class VaultUpdate(LoginRequiredMixin, UpdateView):
    model = Vault
    fields = ['name', 'site', 'description', 'pw']

class VaultDelete(LoginRequiredMixin, DeleteView):
    model = Vault
    success_url = '/passwords/'

def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

SIMILARS = {'o', 'O', '0', 'I', 'l', '1', '|'}

def generate_password(request):
    form = PasswordGeneratorForm(request.POST or None)
    if not form.is_valid():
        context = {'password' : 'Your password will show here', 'length': 12, 'form': form}
    else:
        data = form.cleaned_data
        charset = ''
        if data['use_lower']:
            charset += string.ascii_lowercase
        if data['use_upper']:
            charset += string.ascii_uppercase
        if data['use_digits']:
            charset += string.digits
        if data['use_special']:
            charset += string.punctuation

        if data['avoid_similar']:
            charset = [c for c in charset if c not in SIMILARS]

        length = data['length']
        password = get_random_string(length, charset)
        print(generate_password)
        context = {'password': password, 'length': length, 'form': form}

    return render(request, 'password/gen_pw.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def vaults_index(request):
    vaults = Vault.objects.filter(user = request.user)
    return render(request, 'password/index.html', { 'vaults': vaults })

def vaults_detail(request, vault_id):
    vault = Vault.objects.get(id=vault_id)
    gen_pass_form = PasswordGeneratorForm()
    return render(request, 'password/detail.html', {
    'vault': vault, 'gen_pass_form': gen_pass_form,
  })

def add_passwordgenerator(request):
  form = VaultForm(request.POST) 
  if form.is_valid():
    new_passwordgenerator = form.save(commit=False)
    new_passwordgenerator.user = request.user
    new_passwordgenerator.save()
  return redirect('index')


