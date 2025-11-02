from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Link
from .forms import LinkForm, SignUpForm

@login_required
def link_list(request):
    # Show only links belonging to the logged-in user
    links = Link.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'links/link_list.html', {'links': links})

@login_required
def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            # Tie the link to the logged-in user
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            return redirect('link_list')
    else:
        form = LinkForm()
    return render(request, 'links/add_link.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log them in immediately
            return redirect('link_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
