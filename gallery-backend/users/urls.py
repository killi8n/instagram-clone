from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^explore/$',
        view=views.ExploreUsers.as_view(),
        name='explore_users'
    ),
    url(
        regex=r'^check/$',
        view=views.CheckLogged.as_view(),
        name='check_logged'
    ),
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='user_search'
    ),
    url(
        regex=r'^(?P<username>\w+)/$',
        view=views.UserProfile.as_view(),
        name='user_profile'
    ),
    url(
        regex=r'^id/(?P<user_id>[0-9]+)/$',
        view=views.UserProfileById.as_view(),
        name='user_profile_by_id'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/follow/$',
        view=views.FollowUser.as_view(),
        name='follow_user'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/unfollow/$',
        view=views.UnfollowUser.as_view(),
        name='unfollow_user'
    ),
    url(
        regex=r'^(?P<username>\w+)/followers/$',
        view=views.UserFollowers.as_view(),
        name='user_followers'
    ),
    url(
        regex=r'^(?P<username>\w+)/following/$',
        view=views.UserFollowing.as_view(),
        name='user_following'
    ),
    url(
        regex=r'^(?P<username>\w+)/following_posts/$',
        view=views.UserFollowingPosts.as_view(),
        name='user_following_posts'
    ),
   
]