from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('top/', TemplateView.as_view(template_name='accounts/top.html'), name='top'),
    path('login/', views.loginView.as_view(), name="login"),
    path('logout/', views.logoutView.as_view(), name="logout"),
    path('index/',views.indexView.as_view(), name="index"),
    path('create/', views.Create_account.as_view(), name ="create"),
]
