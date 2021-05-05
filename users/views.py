from django.shortcuts import render
from users.models import User
from users.forms import UserForm
from django.views.generic import View, ListView, FormView, DetailView, UpdateView
from django.urls import reverse_lazy


class UsersListView(ListView):

    model = User
    template_name = 'users_list.html'


class AddUserView(FormView):

    form_class = UserForm
    template_name = 'add_user_form.html'
    success_url = reverse_lazy('users-list')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response


class GetUserView(DetailView):
    model = User
    template_name = 'user_detail.html'


class EditUserView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'add_user_form.html'
    success_url = reverse_lazy('users-list')


def delete_user(request, user_id):

    user = User.objects.get(id=user_id)

    user.delete()

    context = {
        'username': user.username,
            }

    return render(
        template_name='deleted.html',
        request=request,
        context=context
    )
