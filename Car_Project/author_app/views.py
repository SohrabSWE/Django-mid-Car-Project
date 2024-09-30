from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post_app.models import Post
from django.contrib.auth.views import LoginView, LogoutView
from payment_app.models import PaymentModel
from django.views.generic.edit import FormView
from django.contrib import messages 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from .forms import ChangeUserForm
from django.contrib.auth.models import User


#user register
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('register')  

    def form_valid(self, form):
        form.save()  
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)
    

# add class views user login
class UserLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged In Successfull!!!')
        return super().form_valid(form) 
    
    def form_invalid(self, form):
        messages.success(self.request, 'LoggedIn Information Incorect!!!')
        return super().form_invalid(form) 

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['type'] = 'Login'
        return contex


#profile views
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Post.objects.filter(author=self.request.user)
        context['historie'] = PaymentModel.objects.all()
        return context
    
#editprofile
class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ChangeUserForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Profile Update Successfully')
        return super().form_valid(form)    

#password change
class PassChangeView(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    template_name = 'pass_change.html'
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, 'Password Updated Successfully')
        return super().form_valid(form)
    

#user logout
def user_logout(request):
    logout(request)
    return redirect('user_login')