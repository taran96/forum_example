from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect

from threads.models import Thread, Comment
from threads.forms import ThreadForm, CommentForm
# Create your views here.


class CreateThreadView(generic.CreateView):
    '''View to create new threads'''
    model = Thread
    form_class = ThreadForm
    template_name = "threads/create.html"

    def get_success_url(self):
        return reverse("threads:listall")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())


class CreateCommentView(generic.CreateView):
    model = Comment
    template_name = "threads/detail.html"
    form_class = CommentForm
    obj = None

    def get_success_url(self):
        return reverse("threads:detail", kwargs={'pk': self.obj.pk})

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.thread = self.obj
        obj.save()
        return HttpResponseRedirect(self.get_success_url())


class DetailThreadView(generic.DetailView):
    '''View to display a Thread with its comments'''
    model = Thread
    template_name = "threads/detail.html"
    form_class = CommentForm

    def get_form(self):
        return self.form_class(self.request.POST)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = self.request.user
            comment.thread = self.get_object()
            comment.save()
            return HttpResponseRedirect(
                reverse('threads:detail',
                        kwargs={'pk': self.get_object().pk}))

    def get_context_data(self, **kwargs):
        context = super(DetailThreadView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class ListThreadView(generic.ListView):
    '''View to display all threads'''
    model = Thread
    template_name = "threads/list.html"

    def get_queryset(self):
        if self.kwargs.get('author'):
            return Thread.objects.filter(author=self.request.user)
        else:
            return Thread.objects.all()
