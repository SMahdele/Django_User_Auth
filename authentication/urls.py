from django.urls import path
from .views import RegisterView, VerifyEmail,LoginView,ForgotPasswordView,ResetPasswordView,TokenTestingView,ProfileUpdateView


urlpatterns= [
    path('register/', RegisterView.as_view(), name="register"),
    path('email-verify',VerifyEmail.as_view(), name="email-verify"),
    path('login/',LoginView.as_view(),name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/<str:pk>/', ResetPasswordView.as_view(), name='reset-password'),
    path('token-test/',TokenTestingView.as_view(), name = 'TokenTestingView'),
    path('token-test/', TokenTestingView.as_view(), name='TokenTestingView'),
    path('profile-update/<str:pk>/', ProfileUpdateView.as_view(), name='profile-update'),

]