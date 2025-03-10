from rest_framework import viewsets
from .models import * 
from .serializers import * 
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status



# Modify EmployeeDetailsViewSet in views.py
class EmployeeDetailsViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer

class EmployeeTerminationViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTermination.objects.all()
    serializer_class = EmployeeTerminationSerializer
    
    def update(self, request, *args, **kwargs):
        # Handle the update logic here if necessary
        return super().update(request, *args, **kwargs)


class TADGroupsViewSet(viewsets.ModelViewSet):
    queryset = TADGroups.objects.all()
    serializer_class = TADGroupsSerializer

# Notifications ViewSet
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class EmailLogViewSet(viewsets.ModelViewSet):
    queryset = EmailLog.objects.all()
    serializer_class = EmailLogSerializer

    # Custom action for deleting all email logs
    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        try:
            # Delete all email logs
            EmailLog.objects.all().delete()
            return Response({'message': 'All email logs have been deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    
class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class CVManagementViewSet(viewsets.ModelViewSet):
    queryset = CVManagement.objects.all()
    serializer_class = CVManagementSerializer
    parser_classes = (MultiPartParser, FormParser)

class CVAddViewSet(viewsets.ModelViewSet):
    queryset = CVAdd.objects.all()
    serializer_class = CVAddSerializer

class ITProvisionViewSet(viewsets.ModelViewSet):
    queryset = ITProvision.objects.all()
    serializer_class = ITProvisionSerializer

class AdminProvisionViewSet(viewsets.ModelViewSet):
    queryset = AdminProvision.objects.all()
    serializer_class = AdminProvisionSerializer

class FinanceProvisionViewSet(viewsets.ModelViewSet):
    queryset = FinanceProvision.objects.all()
    serializer_class = FinanceProvisionSerializer

class EmployeeAttachmentListCreateView(viewsets.ModelViewSet):
    queryset = EmployeeAttachment.objects.all()
    serializer_class = EmployeeAttachmentSerializer

    def get_queryset(self):
        employee_id = self.request.query_params.get("employee_id")
        if employee_id:
            return self.queryset.filter(employee__id=employee_id)
        return self.queryset

    def create(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')  # Get multiple files
        employee_id = request.data.get('employee')  # Get employee ID
        descriptions = request.data.getlist('description')  # Get descriptions for each file

        if not employee_id:
            return Response({"error": "Employee ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        if len(descriptions) != len(files):
            return Response({"error": "Number of descriptions must match number of files"}, status=status.HTTP_400_BAD_REQUEST)

        employee = EmployeeDetails.objects.get(id=employee_id)

        attachments = []
        for i, file in enumerate(files):
            attachment = EmployeeAttachment(employee=employee, file=file, description=descriptions[i])
            attachments.append(attachment)

        EmployeeAttachment.objects.bulk_create(attachments)  # Bulk insert

        return Response({"message": "Files uploaded successfully"}, status=status.HTTP_201_CREATED)


class EmployeeAttachmentDeleteView(generics.DestroyAPIView):
    queryset = EmployeeAttachment.objects.all()
    serializer_class = EmployeeAttachmentSerializer


