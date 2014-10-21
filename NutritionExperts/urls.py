from django.conf.urls import patterns, include, url
from django.contrib import admin
from mainapp import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Landing Page
    # url(r'^$', views.landing, name="landing"),

    # About pages
    url(r'^$', views.about, name="about"),

    # Login/Signup
    # url(r'^$', views.signup, name="signup"),

)
