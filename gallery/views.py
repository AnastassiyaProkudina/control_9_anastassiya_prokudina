from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, CreateView

from gallery.models import Photo


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IndexRedirectView(RedirectView):
    pattern_name = "posts:index"

def json_like(request, id, *args, **kwargs):
    like = get_object_or_404(Like, post_id=id)
    if like:
        like.delete()
        return JsonResponse({'success': True, 'message': 'true', 'id': id})
    like.get_or_crete(Like(post_id=id))
    return JsonResponse({'success': True, 'message': 'false', 'id': id})
