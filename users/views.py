from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForms


class RegisterViews(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForms
    success_url = reverse_lazy('library:books_list')