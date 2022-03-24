from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='base_login'),
    path('logout/',LogoutView.as_view(next_page="base_login"),name='base_logout'),
    path('register/',RegisterPage.as_view(),name='base_register'),
    path('',TaskList.as_view(),name='base_tasklist'),
    path('task/<int:pk>',TaskDetail.as_view(),name='base_taskdetail'),
    path('task-create',TaskCreate.as_view(),name='base_taskcreate'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name='base_taskupdate'),
    path('task-delete/<int:pk>',TaskDelete.as_view(),name='base_taskdelete'),   
]
