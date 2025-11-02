from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from links import views as link_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('links.urls')),  # Root URL routes to your app
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', link_views.signup, name='signup'),
]
