from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth import login
from utils import auth_view
from .forms import RegisterForm, MyPasswordChangeForm, MySetPasswordForm


def profile_view(request):
    return render(request, 'account/profile.jinja2')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.create()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.jinja2', {'form': form})


def my_password_change(request):
    return auth_view.password_change(request, template_name='account/security.jinja2',
                                     post_change_redirect=reverse('account:profile'),
                                     password_change_form=MyPasswordChangeForm,
                                     message="Your password was changed successfully")


def my_login(request):
    return auth_view.login(request, template_name='login.jinja2')


def my_password_reset(request):
    return auth_view.password_reset(request,
                                    from_email="noreply@zerol.me",
                                    template_name='account/password_reset.jinja2',
                                    post_reset_redirect='account:password_reset_done',
                                    email_template_name='account/password_reset_email.jinja2')


def my_password_reset_done(request):
    return auth_view.password_reset_done(request, template_name='account/password_reset_done.jinja2')


def my_password_reset_confirm(request, **kwargs):
    return auth_view.password_reset_confirm(request,
                                            template_name='account/password_reset_confirm.jinja2',
                                            post_reset_redirect=reverse('login'),
                                            set_password_form=MySetPasswordForm,
                                            **kwargs)
