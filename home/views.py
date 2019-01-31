from django.views.generic import TemplateView, DetailView, CreateView, UpdateView,DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from home.forms import HomeForm
from home.models import Post,Friend

class HomeView(TemplateView):
    template_name= 'home/home.html'

    def get(self,request):
        form = HomeForm()
        posts= Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friend.DoesNotExist:
            friends=None
            pass
        ##friends = Friend.objects.get(current_user=request.user)


        args={'form':form,'posts': posts,'users': users, 'friends':friends}
        return render(request,self.template_name, args)

    def post(self,request):
        form= HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text= form.cleaned_data['post']
            form=HomeForm()
            return redirect('home:home')

        args= {'form':form , 'text':text}
        return render(request,self.template_name,args)

def change_friend(request,operation,pk):
    friend=User.objects.get(pk=pk)
    if operation =='add':
        Friend.make_friend(request.user,friend)
    elif operation =='remove':
        Friend.lose_friend(request.user,friend)
    return redirect('home:home')



class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['post']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['post']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/home/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.user:
            return True
        return False

class friends_list(TemplateView):
    template_name= 'home/friends.html'

    def get(self,request):
        users = User.objects.exclude(id=request.user.id)
        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
        except Friend.DoesNotExist:
            friends=None
            pass
        args={'users': users, 'friends':friends}
        return render(request,self.template_name, args)
