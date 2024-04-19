from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy

from performance.models import Performance, File
from reviewstage.common.Enum import FileType


def index(request):
    return HttpResponse("Hello, world.")


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('performance:login')


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('performance:index')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('performance:index')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        performances = Performance.objects.all()
        files = File.objects.filter(type=FileType.POSTER.name)
        performance_files = {}

        for performance in performances:
            performance_files[performance] = files.get(performance_id=performance)

        context['performance_files'] = performance_files
        return context
