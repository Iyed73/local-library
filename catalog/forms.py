from datetime import date, timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from catalog.models import BookInstance


class RenewBookForm(forms.Form):
    """Form for a librarian to renew books."""

    renewal_date = forms.DateField(
        help_text="Enter a date between now and 4 weeks (default 3 weeks).",
        initial=date.today() + timedelta(weeks=3),
    )

    def clean_renewal_date(self):
        data = self.cleaned_data["renewal_date"]

        if data < date.today():
            raise ValidationError(_("Invalid date - renewal in past"))

        if data > date.today() + timedelta(weeks=4):
            raise ValidationError(_("Invalid date - renewal more than 4 weeks ahead"))

        return data


class RenewBookModelForm(ModelForm):
    def clean_due_back(self):
        data = self.cleaned_data["due_back"]
        if data < date.today():
            raise ValidationError(_("Invalid date - renewal in past"))
        if data > date.today() + timedelta(weeks=4):
            raise ValidationError(_("Invalid date - renewal more than 4 weeks ahead"))

        return data

    class Meta:
        model = BookInstance
        fields = ["due_back"]
        labels = {"due_back": _("New renewal date")}
        help_texts = {
            "due_back": _("Enter a date between now and 4 weeks (default 3 weeks).")
        }
