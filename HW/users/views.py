from django.shortcuts import render
from django.views import View
from .forms import RegisterForm
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
class RegisterView(View):
    template_name = 'users/register.html'
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Greetings {username}, your account successfully registered')
            return redirect(to='users:signin')
        return render(request, self.template_name, context={'form': form})