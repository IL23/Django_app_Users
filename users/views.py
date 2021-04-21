from django.shortcuts import render, get_object_or_404
from users.models import User


def index(request):
    users = User.objects.all()

    context = {
            'users': users
        }

    return render(
        template_name='index.html',
        request=request,
        context=context,
    )


def add_user(request):

    if request.method == 'POST':

        user = User(
            username=request.POST['username'],
            email=request.POST['email'],
        )

        user.save()

        context = {
            'username': user.username,
            'email': user.email,
        }

        return render(
            template_name='user.html',
            request=request,
            context=context
        )

    return render(
        template_name='form.html',
        request=request,
    )


def edit_user(request, user_id):

    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':

        if request.POST['username'] is not '':
            user.username = request.POST['username']

        if request.POST['email'] is not '':
            user.email = request.POST['email']

        user.save()

        context = {
            'username': user.username,
            'email': user.email,
        }

        return render(
            template_name='user.html',
            request=request,
            context=context
        )

    return render(
        template_name='form.html',
        request=request,
    )


def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {
        'username': user.username,
        'email': user.email,
    }
    return render(
        template_name='user.html',
        request=request,
        context=context
    )


def delete_user(request, user_id):

    user = get_object_or_404(User, id=user_id)

    user.delete()

    context = {
        'username': user.username,
            }

    return render(
        template_name='deleted.html',
        request=request,
        context=context
    )
