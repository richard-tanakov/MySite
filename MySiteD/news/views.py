from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-data')
    return render(request, 'news/home_news.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/derail_view.html'
    context_object_name = 'article'


class NewsUpdate(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDelete(DeleteView):
    model = Articles
    success_url='/news/'
    template_name = 'news/news_delete.html'


def create(request):
    eror = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_home')
        else:
            eror = "Неверно заполнена форма."

    form = ArticlesForm()
    data = {
        'form': form,
        'eror': eror,
    }

    return render(request, 'news/create.html', data)
