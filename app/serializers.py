from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import Report, Author, Post


# class ReportSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author_id = serializers.IntegerField(required=True)
#     readings = serializers.JSONField(required=True)
#     text = serializers.CharField(required=True)
#     date_created = serializers.DateTimeField(read_only=True)
#     last_updated = serializers.DateTimeField(read_only=True)
#
#     def validate(self, attrs):
#         if Author.objects.filter(pk=attrs.get('author_id')).exists():
#             return attrs
#         else:
#             raise ValidationError(detail='Object not found')
#
#     def create(self, validated_data):
#         validated_data['author'] = Author.objects.get(pk=validated_data['author_id'])
#         return Report.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.readings = validated_data.get('readings')
#         instance.text = validated_data.get('text')
#         Report.objects.filter(pk=instance.pk).update(**validated_data)
#         return Report.objects.get(pk=instance.pk)
#
#
# class ReportGetSerializer(serializers.Serializer):
#     pk = serializers.IntegerField()
#
#     def validate(self, attrs):
#         if Report.objects.filter(pk=attrs.get('pk')).exists():
#             return attrs
#         else:
#             raise ValidationError(detail='Object not found')


class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    position = serializers.CharField(required=True)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)


class AuthorGetSerializer(serializers.Serializer):
    pk = serializers.IntegerField()

    def validate(self, attrs):
        if Author.objects.filter(pk=attrs.get('pk')).exists():
            return attrs
        else:
            raise ValidationError(detail='Object not found')


# class ReportNestedSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     readings = serializers.JSONField(required=True)
#     text = serializers.CharField(required=True)
#     date_created = serializers.DateTimeField(read_only=True)
#     last_updated = serializers.DateTimeField(read_only=True)
#     author_data = serializers.JSONField(required=True)
#
#     def validate(self, attrs):
#         author_serializer = AuthorSerializer(data=attrs['author_data'])
#         author_serializer.is_valid(raise_exception=True)
#         attrs.update({"author": author_serializer})
#         return attrs
#
#     def create(self, validated_data):
#         author = validated_data['author'].save()
#         validated_data['author'] = author
#
#         return Report.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.readings = validated_data.get('readings')
#         instance.text = validated_data.get('text')
#         Report.objects.filter(pk=instance.pk).update(**validated_data)
#         return Report.objects.get(pk=instance.pk)


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author_id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=True)
    text = serializers.CharField(required=True)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def validate(self, attrs):
        if Author.objects.filter(pk=attrs.get('author_id')).exists():
            return attrs
        else:
            raise ValidationError(detail='Author not found')

    def create(self, validated_data):
        validated_data['author'] = Author.objects.get(pk=validated_data['author_id'])
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Post.objects.filter(pk=instance.pk).update(**validated_data)
        return Post.objects.get(pk=instance.pk)


class PostGetSerializer(serializers.Serializer):
    pk = serializers.IntegerField()

    def validate(self, attrs):
        if Post.objects.filter(pk=attrs.get('pk')).exists():
            return attrs
        else:
            raise ValidationError(detail='Post not found')

