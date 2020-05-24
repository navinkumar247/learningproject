from django.urls import path,include
from . import views


app_name= 'groups'

urlpatterns = [

    path('grouplist/',views.GroupList.as_view(),name='grouplist'),
    path('group/<slug>/',views.GroupDetail.as_view(),name='groupdetail'),
    path('creategroup/',views.CreateGroup.as_view(),name='creategroup'),
    path('joingroup/<slug>/',views.JoinGroup.as_view(),name='joingroup'),
    path('deletegroup/<slug>',views.DeleteGroup.as_view(),name='deletegroup'),
    # path('deleterequest/<slug>',views.DeleteRequest.as_view(),name='deleterequest'),
    path('leavegroup/<slug>/',views.LeaveGroup.as_view(),name='leavegroup'),
]
