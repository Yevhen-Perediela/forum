from django.shortcuts import render,  get_object_or_404, redirect
from django.http import request
from .models import Articles, Comments
# from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate
from .forms import addPost, addComment

# from django.http import HttpResponse


# Create your views here.
def home(request):
    art = Articles.objects.all()

    return render(request,  'main/main.html', {'art': art})
def privacy(request):
    return render(request, 'main/privacy.html')

    # if request.method == 'POST':
    #     form = addComment(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.post_id = post_id
    #         comment.save()
    #         return redirect('post_detail', post_id=post_id)
    # else:
    #     form = addComment(initial={'post_id': post_id})


def article_details(request, id):
    try:
        post = get_object_or_404(Articles, pk=id)
        if request.method == 'POST':
            form = addComment(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.article = post  # Оновлено назву поля
                comment.author = request.user if request.user.is_authenticated else None
                comment.save()
                return redirect('article_details', id=id)
        else:
            form = addComment()
    except Articles.DoesNotExist:
        raise print('No')
    
    return render(request, 'main/Post_detail.html', {'article': post, 'form': form})

from .forms import CustomUserCreationForm, CustomUserAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Замініть 'home' на ваш URL шляху
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/reg.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Замініть 'home' на ваш URL шляху
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def add_post(request):
    if request.method == 'POST':
        form = addPost(data=request.POST)
        if form.is_valid():
            aut = form.save(commit=False)
            aut.author = request.user
            form.save()
            return redirect(home)
    else:
        form = addPost()
    return render(request, 'main/addPost.html', {'form': form})    

