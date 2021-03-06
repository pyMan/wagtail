from __future__ import absolute_import, unicode_literals

from django import VERSION as DJANGO_VERSION

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns

from wagtail.api.v2.endpoints import PagesAPIEndpoint
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.contrib.wagtailapi import urls as wagtailapi_urls
from wagtail.contrib.wagtailsitemaps.views import sitemap
from wagtail.tests.testapp import urls as testapp_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtaildocs.api.v2.endpoints import DocumentsAPIEndpoint
from wagtail.wagtailimages import urls as wagtailimages_urls
from wagtail.wagtailimages.api.v2.endpoints import ImagesAPIEndpoint
from wagtail.wagtailimages.tests import urls as wagtailimages_test_urls
from wagtail.wagtailsearch import urls as wagtailsearch_urls


api_router = WagtailAPIRouter('wagtailapi_v2')
api_router.register_endpoint('pages', PagesAPIEndpoint)
api_router.register_endpoint('images', ImagesAPIEndpoint)
api_router.register_endpoint('documents', DocumentsAPIEndpoint)


urlpatterns = [
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^testimages/', include(wagtailimages_test_urls)),
    url(r'^images/', include(wagtailimages_urls)),

    url(r'^api/', include(wagtailapi_urls)),
    url(r'^api/v2beta/', api_router.urls),
    url(r'^sitemap\.xml$', sitemap),

    url(r'^testapp/', include(testapp_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'', include(wagtail_urls)),
]

if DJANGO_VERSION < (1, 10):
    urlpatterns += i18n_patterns('', url(r'', include(wagtail_urls)))
else:
    urlpatterns += i18n_patterns(url(r'', include(wagtail_urls)))
