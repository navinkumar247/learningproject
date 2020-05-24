from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.
from .models import Group,GroupMember
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView,RedirectView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect


class CreateGroup(CreateView,LoginRequiredMixin):
    model = Group
    fields = ['name','description']


    class Meta:
        order_by = ['-created_at']

class DeleteGroup(DeleteView,LoginRequiredMixin):
    model = Group
    success_url = reverse_lazy('groups:grouplist')

# class DeleteRequest(TemplateView):
#     # model = Group
#     template_name = 'groups/group_delete.html'

class GroupDetail(DetailView,LoginRequiredMixin):
    model = Group


    def get_context_data(self,*args, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(*args,**kwargs)
        # Add in a QuerySet of all the books
        group_object = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        members = group_object.member.all()
        owner = []
        member_queryset = [x for x in GroupMember.objects.all() if x.group == group_object]

        # try:
        if member_queryset:
            owner = member_queryset[0].user
        else:
            owner = None
        # except:
            # if member_queryset != []:

            # HttpResponseRedirect(reverse('groups:deletegroup',kwargs={'slug':self.kwargs.get('slug')}))
        # for member in members:
        #     GroupMember.objects.filter(GroupMember.objects and group_object)
        #     groupmembers = [users for users in GroupMember.objects.all()]
        #     for groupmember in groupmembers:
        #         if member == groupmember.user:
        #             owner.append(member)
        #             break

        context['owner'] = owner
        return context


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
            if group.member.count == 0:
                ownership == True
                # owner = get_object_or_404(User,id=self.kwargs.get('pk'))
                GroupMember.objects.create(user=self.request.user,group=group,ownership=True)
            else:
                GroupMember.objects.create(user=self.request.user,group=group,ownership=False)
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
            # counter = group.member.count()
            # if counter > 1:
            member.delete()
        return super().get(request,*args,**kwargs)
            # else:
            #     return HttpResponseRedirect(reverse('groups:deleterequest',kwargs={'slug':group.slug}))
