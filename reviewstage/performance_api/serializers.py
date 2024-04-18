from rest_framework import serializers
from performance.models import *
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class PerformanceSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        errors = {}
        if 'performance_id' in attrs and not attrs['performance_id']:
            errors['performance_id'] = "Performance_num cannot be a null value."
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


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "비밀번호를 다시 확인하세요."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']


class BookmarkSerializer(serializers.ModelSerializer):
    performance_title = serializers.ReadOnlyField(source='performance.title')

    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'performance_title']


class UserSerializer(serializers.ModelSerializer):
    bookmark = BookmarkSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'bookmark']