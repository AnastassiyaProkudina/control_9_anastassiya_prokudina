from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, TemplateView, UpdateView, DetailView

from gallery.forms import PhotoForm
from gallery.models import Photo


class PhotoDetail(DetailView):
    template_name = "photo.html"
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = Photo.objects.get(pk=self.object.pk)
        context["photos"] = photos
        return context


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "photo_update.html"
    model = Photo
    form_class = PhotoForm

    def get_success_url(self):
        return reverse("photo_detail", kwargs={"pk": self.object.pk})


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    context_object_name = 'photo'
    success_url = reverse_lazy('index')
