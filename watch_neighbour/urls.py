from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from watch_neighbour import views

urlpatterns=[
        url(r'^$', views.all_neighbourhoods, name='neighbourhood'),
        url(r'^new/profile$', views.new_profile, name='new-profile'),
        url(r'^new/neighbourhood$', views.new_neighbourhood, name='new-neighbourhood'),
        url(r'^new/post$', views.new_post, name='new-post'),
        url(r'^current_user_profile/(?P<profile_id>\d+)', views.current_user_profile, name='current_user_profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)