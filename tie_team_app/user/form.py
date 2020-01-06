from django.forms import ModelForm

from .models import stats

class ChangeStatForm(ModelForm):
    class Meta:
        model = stats
        exclude = ['created_time','last_modified','user']

