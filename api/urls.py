from django.urls import include, path
from rest_framework import routers
from api import views

# router = routers.DefaultRouter()
# router.register(r"users", views.UserViewSet)
# router.register(r"groups", views.GroupViewSet)
# router.register(r"countries", views.CountryViewSet)
# router.register(r"persons", views.PersonViewSet)


urlpatterns = [
    # path("", include(router.urls)),
    path("users/", views.UserList.as_view()),
    path("users/<pk>/", views.UserDetails.as_view()),
    path("groups/", views.GroupList.as_view()),
    # path("login/", views.LoginView),
]
