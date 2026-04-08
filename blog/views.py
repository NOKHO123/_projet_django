from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article

# créer des views

# LIST
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

# DETAIL
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

# CREATE
class ArticleCreateView(CreateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = 'article_form.html'
    success_url = reverse_lazy('article_list')

# UPDATE
class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['titre', 'contenu', 'auteur', 'image']
    template_name = 'article_form.html'
    success_url = reverse_lazy('article_list')

# DELETE
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('article_list')