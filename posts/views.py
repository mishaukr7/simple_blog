from django.views.generic import ListView, View
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


class PostListView(ListView):
    model = Post
    paginate_by = 12
    queryset = Post.objects.order_by('-created_date')
    template_name = 'posts/html/post_list.html'

    def get_queryset(self):
        filter = self.request.GET.get('q', '')
        order = self.request.GET.get('sort', '-created_date')
        new_context = Post.objects.filter(Q(title__icontains=filter) | Q(content__icontains=filter)).order_by(order)
        return new_context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['sort'] = self.request.GET.get('sort', '-created_date')
        context['q'] = self.request.GET.get('q', '')
        return context


class PostDetailView(View):
    template_name = 'posts/html/post_detail.html'
    comment_form = CommentForm

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs['post'])
        context = {}
        context.update(csrf(request))
        user = auth.get_user(request)
        context['post'] = post
        context['post_comments'] = post.post_comments.all().order_by('path')
        context['next'] = post.get_absolute_url()
        if user.is_authenticated:
            context['form'] = self.comment_form
        return render(request, template_name=self.template_name, context=context)


@login_required
@require_http_methods(['POST'])
def add_comment(request, post):
    form = CommentForm(request.POST)
    post = get_object_or_404(Post, id=post)

    if form.is_valid():

        author = auth.get_user(request)
        content = form.cleaned_data['comment_area']
        comment = Comment(author=author, path=[], post=post, content=content)
        comment.save()

        try:
            comment.path.extend(Comment.objects.get(id=form.cleaned_data['parent_comment']).path)
            comment.path.append(comment.id)
        except ObjectDoesNotExist:
            comment.path.append(comment.id)

        comment.save()

    return redirect(post.get_absolute_url())
