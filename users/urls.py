from django.urls import path
from .views import RegisterView, VerifyEmailView, ResendOTPView, LoginView, LogoutView, ForgotPasswordView, ResetPasswordView, ProfileCreateView, ProfileView, ProfileUpdateView, ReferralView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('resend-otp/', ResendOTPView.as_view(), name='resend-otp'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('profile/create/', ProfileCreateView.as_view(), name='profile-create'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('referral/', ReferralView.as_view(), name='referral'),
    

    # FOR ADMIN USER
    # path('admin/create-user/', AdminCreateUserView.as_view(), name='admin-create-user'),
    # path('admin/delete-user/<int:pk>/', AdminDeleteUserView.as_view(), name='admin-delete-user'),
]

