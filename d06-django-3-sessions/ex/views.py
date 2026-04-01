from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from ex.forms import SignupForm, LoginForm, TipsForm
from ex.models import Tip, User


def index_view(request):
    form = None
    tips = Tip.objects.select_related('author').order_by('-date')

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TipsForm(request.POST)
            if form.is_valid():
                tip = form.save(commit=False)
                tip.author = request.user
                tip.save()
                return redirect('home')
        else:
            form = TipsForm()
    return render(request, 'home.html', {'tips': tips, 'form': form, 'can_delete': request.user.has_perm('ex.delete_tip'), 'can_downvote': request.user.has_perm('ex.downvote_tip')})


def login_view(request):
    next_url = request.GET.get('next', 'home')

    if request.user.is_authenticated:
        return redirect(next_url)

    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        login(request, form.user)
        return redirect(next_url)

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def signup_view(request):
    next_url = request.GET.get('next', 'home')

    if request.user.is_authenticated:
        return redirect(next_url)

    form = SignupForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(request, user)
        return redirect(next_url)

    return render(request, 'signup.html', {'form': form})


@login_required
def upvote_downvote_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    user = request.user

    action = 'upvotes' if request.resolver_match.url_name is 'upvote_tip' else 'downvotes'
    if action == 'upvotes' or user == tip.author or user.has_perm('ex.downvote_tip'):
        a = getattr(tip, action)
        if user in a.all():
            a.remove(user)
        else:
            oposite_action = 'downvotes' if action is 'upvotes' else 'upvotes'
            o = getattr(tip, oposite_action)
            if user in o.all():
                o.remove(user)
            a.add(user)
        tip.author.update_reputation()
        return redirect('home')

    raise PermissionDenied


@login_required
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, id=tip_id)
    user = request.user

    if user == tip.author or user.has_perm('ex.delete_tip'):
        author = tip.author
        tip.delete()
        author.update_reputation()
        return redirect('home')

    raise PermissionDenied
