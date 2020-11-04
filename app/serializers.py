from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import Report


class ReportSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    readings = serializers.JSONField(required=True)
    text = serializers.CharField(required=True)
    date_created = serializers.DateTimeField(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print('or here')
        return Report.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print('i might be here')
        instance.readings = validated_data.get('readings')
        instance.text = validated_data.get('text')
        Report.objects.filter(pk=instance.pk).update(**validated_data)
        return Report.objects.filter(pk=instance.pk)


class ReportGetSerializer(serializers.Serializer):
    pk = serializers.IntegerField()

    def validate(self, attrs):
        if Report.objects.filter(pk=attrs.get('pk')).exists():
            return attrs
        else:
            raise ValidationError(detail='Object not found')
