
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import post
from django.contrib.auth import logout

from django.http import HttpResponseRedirect

from .forms import new_post_form
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def homeView(request):
    posts = post.objects.all()

    return render(request,
    'home/home.html',
    {
        'posts':posts
    }
    )

class postView(DetailView):
    model = post
    template_name = 'post/post_detail.html'


def login_admin(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
            messages.success(request, ("Login yoki parolni tekshirib qayta urinib ko'ring"))
            return redirect('login')

    else:
        return render(request, 'login/login.html', {})



def blogCreate(request):

    if request.method == "POST":
        form = new_post_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = new_post_form

    return render(request, 'post/post_new.html', {
        'form':form,
    })



def logout_view(request):
    logout(request)
    return redirect('/')



class blogEdit(UpdateView):
    model = post
    template_name = 'post/post_edit.html'
    fields = ['post_img','post_title', 'post_text'] 




class blogDelete(DeleteView):
    model = post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('homeView')



def aboutView(request):
    return render(request, 'about/about.html')


def postsView(request):

    word = request.GET.get('q', '')

    search_word = "None"

    if search_word and search_word != '':
        search_word = post.objects.filter(post_title__contains=word).all()
    else:
        search_word = None

    
    # return render(request, 'index.html', {'q':word, 'result':search_word})

    return render(request, 'post/post_search.html', {'q':word, 'result':search_word})



