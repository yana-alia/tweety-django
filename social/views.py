from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .models import Post, UserProfile, User
from .forms import PostForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView

class ExploreView(View):
    def get(self, request, *args, **kwargs):
    
        posts = Post.objects.all().order_by('-created_on')
        
        context = {
            'posts': posts,
        }
        
        return render(request, 'social/explore.html', context)

class PostListView(View):
    def get(self, request, *args, **kwargs):
        
        following_ids = list(request.user.profile.following.values_list('id', flat=True))
        following_ids.append(request.user.id)

        posts = Post.objects.filter(author__id__in=following_ids).order_by('-created_on')

        # posts = Post.objects.all().order_by('-created_on')
        form = PostForm()
        
        context = {
            'post_list': posts,
            'form': form,
        }
        
        return render(request, 'social/post_list.html', context)
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
        
        return redirect('post-list')

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')
        
        followers = profile.followers.all()
        
        if followers:
            for follower in followers:
                if follower == request.user:
                    is_following = True
                else:
                    is_following = False
        else:
            is_following = False
        
        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'is_following': is_following
        }

        return render(request, 'social/profile.html', context)
    
class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'bio', 'avatar', 'header']
    template_name = 'social/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user
    
class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)
        request.user.profile.following.add(profile.user)
        
        return redirect('profile', pk=profile.pk)
    
class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)
        request.user.profile.following.remove(profile.user)
        
        return redirect('profile', pk=profile.pk)