from rest_framework import serializers
from .models import Department, Level, Year, Subject, Note


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'name', 'years')


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ('id', 'name')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name', 'year', 'level', 'department', 'others')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'file', 'title', 'subject', 'author', 'uploader', 'description', 'time')
