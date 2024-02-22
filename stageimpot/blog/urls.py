from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.views import * 
urlpatterns = [
    path('',loginStage,name="loginstage"),
    path('inscriptionStage/',inscriptionStage,name="inscriptionstage"),
    path('superAdmin/',superAdmin, name="superadmin"),
    path('compteStagiaire/',compteStagiaire, name="comptestagiaire"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
