from django.urls import path
from . import views
from .views import DoadoresCreate, DoacaoCreate, FormCadastro
from .views import DoadoresUpdate
from .views import DoadoresList


app_name = "cadastros"


urlpatterns = [

    path("", FormCadastro.as_view(), name='cadastrar'),
    # path("DescarteZap_Beta", HomeView.as_view(), name='home'),
    path('cadastros/Doadores/', DoadoresCreate.as_view(), name="cadastrar-doadores"),
    path('cadastrar/doacao/', DoacaoCreate.as_view(), name="cadastrar-doacao"),
    path('editar/doadores/<int:pk>/', DoadoresUpdate.as_view(), name='editar-doadores'),
    path('listar/doadores/', DoadoresList.as_view(), name='listar-doadores'),
    # path("", views.SobreView.as_view(), name="home"),

]