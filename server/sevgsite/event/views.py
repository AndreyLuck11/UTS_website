from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from event.serializers import *
from .models import Event
from rest_framework import generics, mixins, views
import datetime

end_date = datetime.date(2055, 1, 1)


class EventListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class EventViewSet(mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # pagination_class = EventListPagination

    def list(self, request, *args, **kwargs):
        start_date = datetime.date.today() - datetime.timedelta(days=1)

        queryset = Event.objects.all().order_by('date_of_event_start')

        df = self.request.query_params.get("df", None)

        if df != 'false':
            queryset = queryset.filter(date_of_event_start__range=(start_date, end_date))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EventListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = EventRetrieveSerializer(instance)
        return Response(serializer.data)
