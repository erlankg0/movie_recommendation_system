from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),  # админка
                  path('', include('account.urls')),
                  # приложение для управления пользователями (регистрация,удаления,восстановления,вход)
                  path('movie/', include('movie.urls')), # приложение где будут храниться и выводится фильмы
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
