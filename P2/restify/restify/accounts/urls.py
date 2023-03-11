from django.urls import path
from . import views


urlpatterns = [ 
    # path('list/', views.stores_list, name='list'),
    # path('manage/', views.StoresManage.as_view(), name='manage'),
    # path('owned/', views.StoresOwned.as_view(), name='owned'),
    # path('detail/<int:pk>/', views.StoreGetSet.as_view(), name='detail'),
    path('create/', views.UserCreate.as_view(), name='create'),
    # path('update/<int:pk>/', views.StoreGetSet.as_view(), name='update'),
    #path('delete/<int:pk>/', views.StoresDelete.as_view(), name='delete'),
]