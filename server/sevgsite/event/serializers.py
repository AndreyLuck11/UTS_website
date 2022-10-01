from rest_framework import serializers

from .models import Event, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = "__all__"


class EventListSerializer(serializers.ModelSerializer):
    cat = CategorySerializer()
    date_of_event_start = serializers.DateField(format="%d.%m.%Y")
    date_of_event_end = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Event
        fields = "__all__"
        # fields = ("id", "title", "date_of_event_start", "image_url", "cat", "date_of_event_end", "location", "url")


# cat = serializers.CharField(source='cat.name')

class EventRetrieveSerializer(serializers.ModelSerializer):
    cat = CategorySerializer()
    date_of_event_start = serializers.DateField(format="%d.%m.%Y")
    date_of_event_end = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Event
        fields = '__all__'
