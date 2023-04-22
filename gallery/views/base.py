from django.views.generic import RedirectView, TemplateView

from accounts.forms import LoginForm
from accounts.models import Account
from gallery.forms import PhotoForm
from gallery.models import Photo


class IndexView(TemplateView):
    template_name = "index.html"
    form_class = LoginForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["photo_form"] = PhotoForm
        context["photos"] = Photo.objects.all().order_by("-created_at")
        context["form"] = self.form_class
        context["accounts"] = Account.objects.all()
        return context


class IndexRedirectView(RedirectView):
    pattern_name = "index"
