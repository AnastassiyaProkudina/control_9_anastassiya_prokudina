from django import forms

from gallery.models import Photo, Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "text",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].widget.attrs.update(
            {"placeholder": "Добавьте комментарий...", "rows": "1", "id": "text"}
        )
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "comment-box"
            visible.label = ""
