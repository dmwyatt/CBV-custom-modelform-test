from django.conf.urls import patterns, include, url

from django.contrib import admin
from test_app.views import ClassBCreateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cbv_cv_mf.views.home', name='home'),
    # url(r'^cbv_cv_mf/', include('cbv_cv_mf.foo.urls')),
    url(r'class_b/add/(?P<the_foreignkey>\d+)/$', ClassBCreateView.as_view(), name='class_b_create'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
