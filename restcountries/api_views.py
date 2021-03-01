from rest_framework import viewsets, generics, renderers, filters
from rest_framework.decorators import action, action
from rest_framework.response import Response
from .models import Country
from .serializers import CountrySerializer

class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(detail=True)
    def neighbours(self, request, *args, **kwargs):
        country = self.get_object()
        return Response(country.neighbouring_countries)

class LanguageList(generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        language = self.kwargs['language']
        return Country.objects.filter(languages__icontains=language)
