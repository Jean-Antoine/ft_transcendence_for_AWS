from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from users.views import CookieTokenRefreshView
from health.views import health_check

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    path('admin/', admin.site.urls),
    
    path('token/refresh/', CookieTokenRefreshView.as_view()),
    
    path('api/user/', include("users.urls")),
    path('api/profile/', include("userprofile.urls")),
    path('api/dashboards/', include("dashboards.urls")),
    path('api/friends/', include("friendship.urls")),
	path("api/tournament/", include("tournament.urls")), 
    path('health/', health_check, name='health_check'),
]
