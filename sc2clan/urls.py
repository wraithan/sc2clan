from django.conf.urls import patterns, url
from django.views.generic import DetailView

from sc2clan.core.models import Profile


urlpatterns = patterns(
    '', # PREFIX
    url(r'^profile/(?P<pk>\d+)$',
        DetailView.as_view(
            model=Profile,
            context_object_name='profile',
            template_name='core/profile.html',
        )),
)