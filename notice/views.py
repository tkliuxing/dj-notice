from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Notice
from .forms import NoticeForm


class NoticeListView(ListView):
    model = Notice


class NoticeCreateView(CreateView):
    model = Notice
    form_class = NoticeForm


class NoticeDetailView(DetailView):
    model = Notice


class NoticeUpdateView(UpdateView):
    model = Notice
    form_class = NoticeForm
