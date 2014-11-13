from django.conf.urls import patterns, include, url
from django.contrib import admin
from mainapp import views
from mainapp import endpoints

urlpatterns = patterns('',
    
    # App pages
    url(r'^feed/', views.feed, name="feed"),

    # Favicon
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),

    # About pages
    url(r'^$', views.landing, name="landing"),
    url(r'^about/', views.about, name="about"),
    url(r'^mission/', views.mission2, name="mission"),
    url(r'^experts/', views.experts, name="experts"),
    url(r'^faq/', views.faq, name="faq"),
    url(r'^expert_contact/(?P<from_page>\d+)/$', views.expert_contact, name="expert_contact"),
    url(r'^expert_contact/', views.expert_contact, name="expert_contact"),

    # App pages
    url(r'^signup_form/', views.signup_form, name="signup_form"),
    url(r'^expert_profile/', views.expert_profile, name="expert_profile"),
    url(r'^user_profile/', views.user_profile, name="user_profile"),
    url(r'^expert_update/', views.expert_update, name="expert_update"),
    url(r'^user_update/', views.user_update, name="user_update"),
    url(r'^discussion/', views.discussion, name="discussion"),
    url(r'^answer_questions/', views.answer_questions, name="answer_questions"),

    # API Endpoints
    url(r'^api/email_signup/', endpoints.email_signup, name="email_signup"),
    url(r'^api/expert_interest_signup/', endpoints.expert_interest_signup, name="expert_interest_signup"),
)
