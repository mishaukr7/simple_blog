from django.conf.urls import url
from .views import signup, activate, account_activation_sent
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login', auth_views.login, {'template_name': 'accounts/html/login.html'}, name='login'),
    path('logout', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('signup', signup, name='signup'),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),

]