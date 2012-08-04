from django.forms import ModelForm

from sc2clan.core.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
