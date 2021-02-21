import django_filters
from django.shortcuts import render
from django.views import generic
from .models import Projeto, Autor, Tema
from .forms import ProjetoForm
from django_filters.filters import ModelChoiceFilter

class ProjetoFilterset(django_filters.FilterSet):
    autor = ModelChoiceFilter(queryset=Autor.objects.all())
    tema = ModelChoiceFilter(queryset=Tema.objects.all())

    class Meta:
        model = Projeto
        fields = ['tema', 'autor']
        form_class = ProjetoForm

class FilteredListView(generic.ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context

class ProjetoListView(FilteredListView):
    model = Projeto
    filterset_class = ProjetoFilterset
    paginate_by = 10
        