from django.contrib.auth.models import User
from django.views.generic.edit import CreateView




class SignUp(CreateView):
    model = User
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'
