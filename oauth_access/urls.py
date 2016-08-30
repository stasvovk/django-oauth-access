from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns("",
    url(r"^login/(?P<service>\w+)/$", views.oauth_login, name="oauth_access_login"),
    url(r"^callback/(?P<service>\w+)/$", views.oauth_callback, name="oauth_access_callback"),
    url(r"^finish_signup/(?P<service>\w+)/$", views.finish_signup, name="oauth_access_finish_signup")
)

