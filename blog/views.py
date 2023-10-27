from django.shortcuts import render
from pytils.translit import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Article
from django.urls import reverse_lazy, reverse


# Create your views here.
class BlogCreateView(CreateView):
    model = Article
    fields = ('title','content','preview','create_date')
    success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        if form.is_valid():
            new_article=form.save()
            new_article.slug=slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Article
    
    def get_queryset(self):
        queryset=super().get_queryset()

        queryset=queryset.filter(is_published=True)

        return queryset

class BlogDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object=super().get_object(queryset)

        self.object.views_count +=1
        self.object.save()

        return self.object

class BlogUpdateView(UpdateView):
    model = Article
    fields = ('title','content','preview','create_date')
    #success_url = reverse_lazy("blog:list")

    def form_valid(self, form):
        if form.is_valid():
            new_article=form.save()
            new_article.slug=slugify(new_article.title)
            new_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:list")
