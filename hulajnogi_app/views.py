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
            post_list.append(post.review_body[:20])
        context['post_list'] = post_list
        return context

    def get_queryset(self):
        return HulajnogaPost.objects.order_by("-creation_date")


class PostDetailView(DetailView):
    model = HulajnogaPost
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        # post_list = []
        # for post in HulajnogaPost.objects.all():
        #     post_list.append(post.review_body[:50])
        # context['post_list'] = post_list
        return context


def PostCreateView(request):
# if this is a POST request we need to process the form data

    # user = request.user
    # employee = user.employee

    if request.method == 'POST':
        # dostaniesz dane z forma i stworz obiekt

        # sprobuj na sztywno tu stworzyc obiekt i zapisac do bazy danych na razie a potem do danych z htmla dopasuj
            #wyszukaj jak stworzyc obiekt i go zapisac


        #tutaj jest jak z posta dane wyciagnac
        # form = CreatePostForm(request.POST)
        # Blog(id=3, name='Cheddar Talk', tagline='Thoughts on cheese.')
        post = HulajnogaPost(review_body=request.POST['post_name'], ideas_category=request.POST['category'],
                             coordinateX=request.POST['coordinateX'], coordinateY=request.POST['coordinateY'])
        # post = HulajnogaPost.objects.create(request.POST['coordinateX'], request.POST['coordinateY'], request.POST['post_name'])
        post.save()




        #z powrotem do listy postow
        return HttpResponseRedirect(reverse('index'))

    # if a GET (or any other method)
    # zwroc strone z pusta forma

    return render(request, 'post_new.html')
