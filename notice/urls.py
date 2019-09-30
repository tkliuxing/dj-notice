from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'notice', api.NoticeViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Notice
    path('app_name/notice/', views.NoticeListView.as_view(), name='app_name_notice_list'),
    path('app_name/notice/create/', views.NoticeCreateView.as_view(), name='app_name_notice_create'),
    path('app_name/notice/detail/<int:pk>/', views.NoticeDetailView.as_view(), name='app_name_notice_detail'),
    path('app_name/notice/update/<int:pk>/', views.NoticeUpdateView.as_view(), name='app_name_notice_update'),
)
