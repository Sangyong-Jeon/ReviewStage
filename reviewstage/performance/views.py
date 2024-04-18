from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.views.generic import TemplateView




from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy


def index(request):
	return HttpResponse("Hello, world.")


class SignupView(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('performance:login')
	template_name = 'registration\signup.html'


class CustomLoginView(LoginView):
	form_class = AuthenticationForm
	template_name = 'registration/login.html'

	def get_success_url(self):
		return reverse_lazy('performance:index')

class HomeView(TemplateView):
    template_name = 'home.html'
