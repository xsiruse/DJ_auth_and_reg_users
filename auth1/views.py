from django.shortcuts import render
# from auth1.forms import UserFormPost
# from django.contrib.auth1.forms import UserCreationForm
from .forms import UserCreateForm
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    return render(
        request,
        'home.html'
    )


class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    # class Meta:



# def signup(request):
#     context = {}
#     form = UserFormPost(request.POST or None)
#     context['form'] = form
#     return render(
#         request,
#         'registration/signup.html', {'form': form, 'context': context, }
#     )
