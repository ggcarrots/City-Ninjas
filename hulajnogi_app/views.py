from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator

from .models import HulajnogaPost

# Create your views here.
class PostListView(ListView):
    model = HulajnogaPost
    template_name = 'post_list.html'
    context_object_name = "post_list"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        post_list = []
        for post in HulajnogaPost.objects.all():
            post_list.append(post.review_body[:50])
        context['post_list'] = post_list
        return context

    def get_queryset(self):
        return HulajnogaPost.objects.order_by("-creation_date")