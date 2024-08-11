from django.conf import settings
from django.urls import path
from django.conf.urls.static import static


from .views import *

urlpatterns = [
                  path('', index, name='home'),
                  path('siat/', siat, name='siat'),
                  path('siat/<int:siat_id>', view_siat, name='view_siat'),
                  path('siat/api/<int:siat_api_id>', view_siat_api, name='view_siat_api'),
                  path('about/', about, name='about'),
                  path('services/', services, name='services'),
                  path('contact/', contact, name='contact'),
                  path('accounts/email/', email_view, name='email_view'),
                  # path('xodimlar', xodimlar, name='xodimlar'),
                  # path('news', news, name='news'),
                  # path('category/<int:category_id>/', get_category),
                  # path('news/<int:news_id>/', view_news, name='view_news'),
                  # path('news/add_news/', add_news, name='add_news'),
                  # path('login/', login_user, name='login'),
                  # path('logout/', logout_user, name='logout'),
                  # path('register/', register_user, name='register'),
                  # path('reg', registr, name='registr'),
                  # path('xodimlar', xodimlar, name='xodimlar'),
                  # path('boshqarma/', uploadder, name='uploadder'),
                  # path('ishlar/', ishlar, name='ishlar'),
                  # path('topshiriq/', topshiriq, name='topshiriq'),
                  # path('delete_item/<int:myid>', delete_item, name='delete_item'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)