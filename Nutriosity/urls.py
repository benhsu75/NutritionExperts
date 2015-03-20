from django.conf.urls import patterns, include, url
from django.contrib import admin
from mainapp import views
from mainapp import endpoints

urlpatterns = patterns('',
    
    # App pages
    url(r'^feed/(?P<state>\d+)/(?P<current_page>\d+)/$', views.feed, name="feed"),
    url(r'^feed/', views.feed, name="feed"),


    # Favicon
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),

    # About pages
    url(r'^$', views.feed, name="feed"),
    url(r'^landing/', views.landing, name="landing"),
    url(r'^about/', views.about, name="about"),
    url(r'^mission/', views.mission2, name="mission"),
    url(r'^experts/', views.experts, name="experts"),
    url(r'^faq/', views.faq, name="faq"),
    url(r'^terms/', views.terms, name="terms"),
    url(r'^privacy/', views.privacy, name="privacy"),
    url(r'^disclaimer/', views.disclaimer, name="disclaimer"),
    url(r'^expert_contact/', views.expert_contact, name="expert_contact"),
    url(r'^arabic/', views.arabic, name="arabic"),

    # App pages
    url(r'^sign_in/', views.sign_in, name="sign_in"),
    url(r'^sign_up/', views.sign_up, name="sign_up"),
    url(r'^sign_up_profile/', views.sign_up_profile, name="sign_up_profile"),
    url(r'^profile/(?P<user_profile_pk>\d+)/$', views.profile, name="profile"),
    url(r'^discussion/(?P<pk>\d+)/', views.discussion, name="discussion"),
    url(r'^ask/', views.ask, name="ask"),
    url(r'^my_account/', views.my_account, name="my_account"),

    url(r'^expert_update/', views.expert_update, name="expert_update"),
    url(r'^user_update/', views.user_update, name="user_update"),
    url(r'^answer_questions/', views.answer_questions, name="answer_questions"),
    url(r'^update_password/', views.update_password, name="update_password"),

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
    url(r'^api/star_answer/', endpoints.star_answer, name="star_answer"),
    url(r'^api/unstar_answer/', endpoints.unstar_answer, name="unstar_answer"),
    url(r'^api/upvote_question/', endpoints.upvote_question, name="upvote_question"),
    url(r'^api/remove_upvote_question/', endpoints.remove_upvote_question, name="remove_upvote_question"),
    url(r'^api/comment/', endpoints.comment, name="comment"),
    url(r'^api/change_password/', endpoints.change_password, name="change_password"),
    url(r'^api/update_member_profile/', endpoints.update_member_profile, name="update_member_profile"),
    url(r'^api/update_expert_profile/', endpoints.update_expert_profile, name="update_expert_profile"),

    # url(r'^api/get_feed_items/(?P<current_page>\d+)/$', endpoints.get_feed_items, name="get_feed_items"),
    url(r'^api/get_feed_items/', endpoints.get_feed_items, name="get_feed_items"),
    url(r'^api/get_scores/', endpoints.get_scores, name="get_scores"),
    url(r'^api/forgot_password/', endpoints.forgot_password, name="forgot_password"),
    url(r'^api/translate/', endpoints.translate, name="translate"),

)
