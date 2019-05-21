from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^cities$', views.cities),
    url(r'^create_city$', views.create_city),
    url(r'^editcity/(?P<city_id>\d+)$', views.editcity),
    url(r'^addcityphotos/(?P<city_id>\d+)$', views.addcityphotos),
    url(r'^signup$', views.signup),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.user_info),
    url(r'^logout$', views.logout),
    url(r'^edit/(?P<city_id>\d+)$', views.edit),
    url(r'^events_feed/(?P<city_id>\d+)$', views.events_feed),
    url(r'^user_profile/(?P<other_user_id>\d+)$', views.profile),
    url(r'^post_an_event/(?P<city_id>\d+)$', views.post_an_event),
    url(r'^post_event$', views.post_event),
    url(r'^filter_city/(?P<city_id>\d+)$', views.filter_city),
    url(r'^apply$', views.apply),
    url(r'^edit_events$', views.edit_events),
    url(r'^apply_event_changes$', views.apply_event_changes),
    url(r'^user_messages$', views.user_messages),
    url(r'^send_message$', views.send_message),
]