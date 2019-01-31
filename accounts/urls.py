from django.conf.urls import url
from django.urls import path, reverse_lazy, include
from . import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

app_name = 'accounts'

urlpatterns= [

    url( r'^login/$', LoginView.as_view(template_name="accounts/login.html"), name="login"),
    url( r'^logout/$', LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    url(r'^register/$',views.register, name='register'),
    url(r'^profile/(?P<pk>\d+)/$',views.view_profile , name='view_profile_with_pk'),
    url(r'^profile/$',views.view_profile , name='view_profile'),
    url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
    url(r'^change-password/$',views.change_password,name='change_password'),
    url(r'^reset-password/$',PasswordResetView.as_view( template_name='accounts/reset_password.html',
        email_template_name='accounts/reset_password_email.html', success_url=reverse_lazy('accounts:password_reset_done')
    ),name="reset_password"),
    url(r'^reset-password/done/$',PasswordResetDoneView.as_view(template_name="accounts/reset_password_done.html"),name="password_reset_done"),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',PasswordResetConfirmView.as_view(template_name="accounts/reset_password_confirm.html",success_url=reverse_lazy('accounts:password_reset_complete')), name="password_reset_confirm"),
    url(r'^reset-password/complete/$',PasswordResetCompleteView.as_view(template_name="accounts/reset_password_complete.html"),name="password_reset_complete"),

    ]
