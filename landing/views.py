from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from .models import Landing, Workers, Feedback
from .forms import NewForm, NewFormTag, FeedbackForm

def all_goods(request):
    all_goods = Landing.objects.all()
    workers = Workers.objects.all()
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('send_detail', pk=news.pk)
    else:
        form = FeedbackForm()
    return render(request, 'landing/goods.html', {'all_goods': all_goods, 'workers': workers, 'form': form})



def goods_new(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('goods_detail', pk=news.pk)
    else:
        form = NewForm()
    return render(request, 'landing/goods_edit.html', {'form': form})


def goods_edit(request, pk):
    news = get_object_or_404(Landing, pk=pk)
    if request.method == "POST":
        form = NewForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('goods_detail', pk=news.pk)
    else:
        form = NewForm(instance=news)
    return render(request, 'landing/goods_edit.html', {'form': form})


def goods_detail(request, pk):
    goods_detail = get_object_or_404(Landing, pk=pk)
    return render(request,
                  'landing/goods_detail.html',
                  {'goods_detail': goods_detail})


def goods_delete(request, pk):
    try:
        news = Landing.objects.get(id=pk)
        news.delete()
        return redirect('all_goods')

    except:
        return HttpResponseNotFound("<h2>Такой страницы нет</h2>")

def create_tag(request):
    if request.method == "POST":
        form = NewFormTag(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('workers_detail', pk=news.pk)
    else:
        form = NewFormTag()
    return render(request, 'landing/create_tag.html', {'form': form})


def workers_detail(request, pk):
    workers_detail = get_object_or_404(Workers, pk=pk)
    return render(request,
                  'landing/workers_detail.html',
                  {'workers_detail': workers_detail})


def send_detail(request, pk):
    send_detail = get_object_or_404(Feedback, pk=pk)
    return render(request,
                  'landing/send_detail.html',
                  {'send_detail': send_detail})