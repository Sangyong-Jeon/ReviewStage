from rest_framework import serializers
from performance.models import Performance, Review, File


class PerformanceSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        errors = {}
        if 'performance_num' in attrs and not attrs['performance_num']:
            errors['performance_num'] = "Performance_num cannot be a null value."
        if 'title' in attrs and not attrs['title']:
            errors['title'] = "Title cannot be a null value."
        if errors:
            raise serializers.ValidationError(errors)

        return attrs

    class Meta:
        model = Performance
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
