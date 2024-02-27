from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm


# Create your views here.
def thumbnail_asigner(posts):
    for post in posts:
        # Parse HTML content of post
        soup = BeautifulSoup(post.content, 'html.parser')
        candidate_elements = soup.find_all(['img', 'p', 'div', 'span', 'a'])  # Add more elements if needed
        # Iterate over candidate elements to find the first image
        for element in candidate_elements:
            if element.name == 'img':
                # If element is an img tag, use its src attribute
                post.thumbnail = element['src']
                break  # Stop searching after finding the first image
            elif element.find('img'):
                # If element contains an img tag, use its src attribute
                img_tag = element.find('img')
                post.thumbnail = img_tag['src']
                break  # Stop searching after finding the first image
    

def index(request):
    posts = PostModel.objects.all()
    
    thumbnail_asigner(posts)
    tech_posts = PostModel.objects.filter(category='Technology')
    thumbnail_asigner(tech_posts)
    lifestyle_posts = PostModel.objects.filter(category='Style')
    thumbnail_asigner(lifestyle_posts)
    religion_posts = PostModel.objects.filter(category='Religion')
    thumbnail_asigner(religion_posts)
    

    context = {
        'posts': posts,
        'tech': tech_posts,
        'lifestyle': lifestyle_posts,
        'religion': religion_posts,
         'now': timezone.now(),
    }

    return  render(request, 'blog/index.html', context)

def category(request, cats):
    category_posts = PostModel.objects.filter(category=cats)
    thumbnail_asigner(category_posts)
    context = {
        'cats': cats,
        'category_posts': category_posts,
        'now': timezone.now(),
    }
    return render (request, 'blog/category.html', context)
  
def latest_posts(request):
    posts = PostModel.objects.all()
    
    context = {
        'posts': posts,
        'now': timezone.now(),
    }
    return render(request, 'blog/latest-stories.html', context)

@login_required
def write(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostModelForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('blog-index')
        else:
            form = PostModelForm()
        context = {
        'form': form,
        'is_write_page': True,
        }
        return render(request, 'blog/write.html',  context)
    else:
         return redirect('users-login')


def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        if request.user.is_authenticated:
            c_form = CommentForm(request.POST)
            if c_form.is_valid():
                instance = c_form.save(commit=False)
                instance.user = request.user
                instance.post = post
                instance.save()
                return redirect('blog-post-detail', pk=post.id)
        else:
            return redirect('users-login')
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'c_form': c_form,
    }
    return render(request, 'blog/post-detail.html', context)

@login_required
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post-edit.html', context)

@login_required
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    
    if request.user != post.author:
        return redirect('blog-index')
    
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    
    context = {
        'post': post,
    }
    return render(request, 'blog/post-delete.html', context)

def search(request):
    query = request.GET.get('query', '')
    
    posts = PostModel.objects.filter(Q(title__icontains=query) | Q(category__icontains=query) | Q(content__icontains=query))
    thumbnail_asigner(posts)
    context = {
        'posts': posts,
        'query': query,
        'now': timezone.now(),
        
    }
    return render(request, 'blog/search.html', context)