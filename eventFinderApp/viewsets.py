from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
