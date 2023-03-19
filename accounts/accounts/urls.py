from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name='home'),
    path('',views.landing_page, name='landing_page'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.log_in, name='login'),
    path('logout/',views.log_out, name='logout'),
]
