from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import HomePageView, SignUpView

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'survivalguide.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^accounts/register/$', SignUpView.as_view, name='signup'),
    url(r'^admin/', include(admin.site.urls)),
)
