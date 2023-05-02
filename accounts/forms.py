from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-field ", "placeholder": "Эл. адрес"}
        ),
    )
    password = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(
            attrs={"class": "form-field ", "placeholder": "Пароль"}
        ),
    )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="",
        strip=False,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-field ", "placeholder": "Пароль"}
        ),
    )
    password_confirm = forms.CharField(
        label="",
        strip=False,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-field ", "placeholder": "Повторите пароль"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "avatar",
            "password",
            "password_confirm",
            "bio",
        )
        username = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"placeholder": "Логин*"})
        self.fields["username"].help_text = None
        self.fields["email"].widget.attrs.update({"placeholder": "Эл.почта"})
        self.fields["bio"].widget.attrs.update(
            {"placeholder": "Напишите немного о себе"}
        )
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-field"
            visible.label = ""

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают!")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user


class AccountChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]
        labels = {"username": "Логин", "email": "Email"}
