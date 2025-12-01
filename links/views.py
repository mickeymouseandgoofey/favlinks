from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Link
from .forms import LinkForm, SignUpForm

@login_required # Ensure user is logged in to view their links
def link_list(request): #
    # Show only links belonging to the logged-in user
    links = Link.objects.filter(user=request.user).order_by('-created_at') # Fetch links for the user, ordered by creation date
    return render(request, 'links/link_list.html', {'links': links}) # Render the link list template with the user's links

@login_required # Ensure user is logged in to add a link
def add_link(request):
    if request.method == 'POST': # Handle form submission
        form = LinkForm(request.POST) # Create form instance with POST data
        if form.is_valid():  # Validate the form
            # Tie the link to the logged-in user
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            return redirect('link_list')  # Redirect to link list after adding
    else:
        form = LinkForm()  # Create an empty form for GET request
    return render(request, 'links/add_link.html', {'form': form})  # Render the add link template with the form

def signup(request):  # User signup view
    if request.method == 'POST':  # Handle form submission
        form = SignUpForm(request.POST)  # Create form instance with POST data
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log them in immediately
            return redirect('link_list')  # Redirect to link list after signup
    else:
        form = SignUpForm()  # Create an empty signup form for GET request
    return render(request, 'registration/signup.html', {'form': form})  # Render the signup template with the form
