from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login




from .models import *
from .forms import *
from .utils import *



class CarsList(DataMixin, ListView):
    paginate_by = 1
    model = Car
    template_name = 'blog/index.html'
    context_object_name = 'cars'
    extra_context = {'title': 'главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class CarBrands(DataMixin, ListView):
    model = Car
    template_name = 'blog/index.html'
    context_object_name = 'cars'
    allow_empty = False

    def get_queryset(self):
        return Car.objects.filter(brd__slug=self.kwargs['brands_slug'])
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['cars'][0].brd),
                                      brands_selected=context['cars'][0].brd_id)
        return dict(list(context.items()) + list(c_def.items()))


class ShowCar(DataMixin, DetailView):
    model = Car
    template_name = 'blog/car.html'
    slug_url_kwarg = 'car_slug'
    context_object_name = 'car'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['car'])
        return dict(list(context.items()) + list(c_def.items()))



class AddCar(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddCarForm
    template_name = 'blog/addcar.html'
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('main')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить автомобиль')
        return dict(list(context.items()) + list(c_def.items()))




class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')

    
class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('main')
    

def logout_user(request):
    logout(request)
    return redirect('login')



def about(request):
    return HttpResponse('О нас')


def contact(request):
    return HttpResponse('Контакты')