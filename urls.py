from django.urls import include, path
from .views import ProjetoListView

urlpatterns = [
    path('', ProjetoListView.as_view(), name='projetos'),
]