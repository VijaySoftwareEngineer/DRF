from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication and permission
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]  #IsAdminUser is only work when staff status is True of user.
    # we can also do that globally for many classes in setting.py file