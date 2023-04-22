from django import forms

from gallery.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["photo", "caption"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["caption"].widget.attrs.update({"placeholder": "Добавьте подпись..."})
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "comment-box"
            visible.label = ""
