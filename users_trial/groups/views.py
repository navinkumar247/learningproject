from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Group,GroupMember
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages

class CreateGroup(CreateView,LoginRequiredMixin):
    model = Group
    fields = ['name','description']

    class Meta:
        order_by = ['-created_at']

class GroupDetail(DetailView,LoginRequiredMixin):
    model = Group


class GroupList(ListView):
    model = Group
    template_name = 'group_list.html'
#
class JoinGroup(RedirectView,LoginRequiredMixin):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:groupdetail',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)
            # owner = group.member.all()[0]
            # owner_group = GroupMember.objects.filter(user=owner.user,group=group)
            # GroupOwner.objects.create(user=owner.user,owner_group=owner_group)
        except:
            messages.warning(self.request,"Already a member")
        else:
            messages.success(self.request,"Membership created")

        return super().get(request,*args,**kwargs)

class LeaveGroup(RedirectView,LoginRequiredMixin):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:groupdetail',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            member = GroupMember.objects.filter(user=self.request.user,group=group)
        
        except:
            messages.warning(self.request,"Not a member")
        else:
            messages.success(self.request,"Left the group")
            member.delete()
        return super().get(request,*args,**kwargs)
