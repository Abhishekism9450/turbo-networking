from django.conf.urls import url
from django.urls import path
from home.views import HomeView,PostDetailView,PostCreateView, PostUpdateView , PostDeleteView ,friends_list

from . import views

urlpatterns= [
    url(r'^$',HomeView.as_view() , name='home'),
    url(r'^friends/$', friends_list.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view() ,name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() ,name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() ,name='post-delete'),
    path('post/new/', PostCreateView.as_view() ,name='post-create'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',views.change_friend,name='change_friend'),
]
