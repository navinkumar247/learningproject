from django.contrib import admin
from .models import Group,GroupMember
# Register your models here.

admin.site.register(Group)


class GroupMemberInline(admin.TabularInline):
    model = GroupMember

# class GroupOwnerInline(admin.TabularInline):
#     model = GroupOwner
