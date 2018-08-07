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
        url(r'^single_neighbourhood/(?P<neighbourhood_id>\d+)', views.single_neighbourhood, name='single_neighbourhood'),
        url(r'^new/business', views.new_business, name='new-business'),
        url(r'^new/department', views.new_department, name='new-department'),
        url(r'^occupants_and_location/(?P<neighbourhood_id>\d+)', views.occupants_and_location, name='occupants_and_location'),
        url(r'^new/location', views.new_location, name='new-location'),
        url(r'^single_post/(?P<id>\d+)', views.single_post, name='single_post'),
        url(r'^new/comment', views.new_comment, name='new-comment'),
        url(r'^comments_for_posts/(?P<post_id>\d+)', views.comments_for_posts, name='comments_for_posts'),
        url(r'^search/', views.search_results, name='search_results'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)