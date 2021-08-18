from django.urls import path
from .views import  * 

urlpatterns = [
    path('', all_goods, name='all_goods'),
    path('<int:pk>/', goods_detail, name='goods_detail'),
    path('new/', goods_new, name='goods_new'),
    path('<int:pk>/edit/', goods_edit, name='goods_edit'),
    path('<int:pk>/delete/', goods_delete, name='goods_delete'),
    path('tag/create', create_tag, name='create_tag'),
    path('worker/<int:pk>', workers_detail, name='workers_detail'),
    # path('com/', send_form, name='comment'),
    path('comments/<int:pk>', send_detail, name='send_detail'),
    
]
