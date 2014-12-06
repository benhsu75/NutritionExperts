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
    url(r'^terms/', views.terms, name="terms"),
    url(r'^privacy/', views.privacy, name="privacy"),
    url(r'^disclaimer/', views.disclaimer, name="disclaimer"),
    url(r'^expert_contact/', views.expert_contact, name="expert_contact"),

    # App pages
    url(r'^sign_in/', views.sign_in, name="sign_in"),
    url(r'^sign_up/', views.sign_up, name="sign_up"),
    url(r'^sign_up_profile/', views.sign_up_profile, name="sign_up_profile"),
    url(r'^profile/(?P<user_profile_pk>\d+)/$', views.profile, name="profile"),
    url(r'^discussion/(?P<pk>\d+)/', views.discussion, name="discussion"),
    url(r'^ask/', views.ask, name="ask"),

    url(r'^expert_update/', views.expert_update, name="expert_update"),
    url(r'^user_update/', views.user_update, name="user_update"),
    url(r'^answer_questions/', views.answer_questions, name="answer_questions"),

    # API Endpoints
    url(r'^api/email_signup/', endpoints.email_signup, name="email_signup"),
    url(r'^api/expert_interest_signup/', endpoints.expert_interest_signup, name="expert_interest_signup"),
    url(r'^api/sign_up_user/', endpoints.sign_up_user, name="sign_up_user"),
    url(r'^api/authenticate_signin/', endpoints.authenticate_signin, name="authenticate_signin"),
    url(r'^api/log_out/', endpoints.log_out, name="log_out"),
    url(r'^api/upload_profile_picture/', endpoints.upload_profile_picture, name="upload_profile_picture"),
    url(r'^api/populate_expert_profile/', endpoints.populate_expert_profile, name="populate_expert_profile"),
    url(r'^api/populate_member_profile/', endpoints.populate_member_profile, name="populate_member_profile"),
    url(r'^api/post_question/', endpoints.post_question, name="post_question"),
    url(r'^api/answer_question/', endpoints.answer_question, name="answer_question"),
    
    
)
