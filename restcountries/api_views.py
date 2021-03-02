from rest_framework import viewsets, generics, filters, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Country
from .serializers import CountrySerializer
from .filters import CustomSearchFilter

class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = (CustomSearchFilter,)
    permission_classes = (permissions.IsAuthenticated,)

    # Get neighbours of a country instance
    @action(detail=True)
    def neighbours(self, request, *args, **kwargs):
        country = self.get_object()
        return Response(country.neighbouring_countries)

class LanguageList(generics.ListAPIView):
    """
    Get the list of countries who speak the language specified
    """
    serializer_class = CountrySerializer

    def get_queryset(self):
        language = self.kwargs['language']
        return Country.objects.filter(languages__icontains=language)

