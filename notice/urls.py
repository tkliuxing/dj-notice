from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'notice', api.NoticeViewSet)
router.register(r'view-my-notice', api.ViewMyNoticeViewSet)
router.register(r'mailbox', api.MailBoxViewSet)
router.register(r'mailbox-mark-all-read', api.MailBoxMarkAllReadView)
router.register(r'mailbox-unread-count', api.MailBoxUnreadCountView)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Notice
    path('notice/', views.NoticeListView.as_view(), name='notice_list'),
    path('notice/create/', views.NoticeCreateView.as_view(), name='notice_create'),
    path('notice/detail/<int:pk>/', views.NoticeDetailView.as_view(), name='notice_detail'),
    path('notice/update/<int:pk>/', views.NoticeUpdateView.as_view(), name='notice_update'),
)
