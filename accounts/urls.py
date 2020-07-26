from django.urls import paths
from .views import SignUpView

urlpatterns = [
path('signup/', SignUpView.as_view(), name='signup'),




]
