from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='homeView'),
    path('post/<int:pk>', views.postView.as_view(), name='postView'),
    path('login/', views.login_admin, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post/edit/<int:pk>', views.blogEdit.as_view(), name='blog_edit'),
    path('post/new/', views.blogCreate, name='blogCreate'),
    path('post/del/<int:pk>', views.blogDelete.as_view(), name='blog_delete'),
    path('about', views.aboutView, name='aboutView'),
    path('search', views.postsView, name='postsView')
]

