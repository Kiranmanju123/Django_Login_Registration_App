from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
url('signup/',views.signup_contr,name="signup"),
url('login/',views.login_contr, name="login")
]