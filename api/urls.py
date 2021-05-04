from django.contrib import admin
from django.urls import path, include

from .import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("aluno",views.AlunoViewSet)
router.register("matricula",views.MatriculaViewSet)
router.register("suspender",views.SuspenderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
