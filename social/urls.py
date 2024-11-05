from django.urls import path
from .views import PostListView, ProfileView, ProfileEditView, AddFollower, RemoveFollower, ExploreView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('explore', ExploreView.as_view(), name='explore'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path("profile/<int:pk>/edit", ProfileEditView.as_view(), name="profile-edit"),
    path("profile/<int:pk>/followers/add", AddFollower.as_view(), name="add-follower"),
    path("profile/<int:pk>/followers/remove", RemoveFollower.as_view(), name="remove-follower")
]