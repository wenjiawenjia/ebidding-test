from rest_framework import serializers


class ImageUploadSerializer(serializers.Serializer):
    doc_name = serializers.CharField()
