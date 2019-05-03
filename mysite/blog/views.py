from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required #best for function views
from django.contrib.auth.mixins import LoginRequiredMixin #best for CBVs
from django.views.generic import (ListView, CreateView,
                                    UpdateView, DetailView,
                                    DeleteView, TemplateView)
from blog.models import Post, Comment
from django.urls import reverse_lazy

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # filter the post the date_published is <= timenow and the most recent posts come first
        return Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')

class PostDetailView(DetailView):
    model = Post

# only authenticated users can create post
class PostCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/' # if not authenticated, direct to login page
    redirect_field_name = 'blog/post_detail.html' #after creating, redirect to the post detail page
    form_class = PostForm
    model = Post

class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = '/login/' # if not authenticated, direct to login page
    redirect_field_name = 'blog/post_detail.html' #after creating, redirect to the post detail page
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('post_list')
    model = Post

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/account/login/'
    redirect_field_name = 'blog/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date_published__isnull=True).order_by('-date_create')


##############################################################################
##############################################################################
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish_post()
    return redirect('post_detail', pk=post.pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form':form})

@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', post_pk)
