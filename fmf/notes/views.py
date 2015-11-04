from django.http import Http404
from rest_framework import filters, mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Department, Level, Year, Subject, Note, File
from .pagination import NotePagination
from .serializers import DepartmentSerializer, LevelSerializer, YearSerializer, SubjectSerializer, NoteSerializer, FileSerializer
from .files import *


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class LevelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class YearViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all().order_by('name')
    serializer_class = SubjectSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-pk')
    serializer_class = NoteSerializer
    pagination_class = NotePagination
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('subject', 'subject__year', 'subject__level', 'subject__department', 'subject__others')
    search_fields = ('title', 'description', 'subject__name')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.data['file'] = move_registered_file_name(serializer.data['file'], serializer.data['title'])

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class FileViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FileSerializer

    def get_queryset(self):
        files = list_uploaded_notes()
        data = []
        for f in files:
            data.append({
                'pk': int(f[:-4]),
                'id': int(f[:-4]),
                'name': f
            })
        data.sort(key=lambda f: f['id'], reverse=True)
        return data

    def get_object(self):
        queryset = self.get_queryset()

        for f in queryset:
            if f['id'] == int(self.kwargs['pk']):
                return f;

        raise Http404

    def create(self, request, *args, **kwargs):
        data = handle_uploaded_note(request.FILES.get('file'))

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
