from rest_framework import filters, viewsets
from .models import Department, Level, Year, Subject, Note
from .pagination import NotePagination
from .serializers import DepartmentSerializer, LevelSerializer, YearSerializer, SubjectSerializer, NoteSerializer


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
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('subject', 'subject__year', 'subject__level', 'subject__department')
