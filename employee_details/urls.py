from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import * 

router = DefaultRouter()
router.register('employees', EmployeeDetailsViewSet)
router.register('notifications', NotificationViewSet)
router.register('email_logs', EmailLogViewSet)  # New Email Log API
router.register('attendance', AttendanceViewSet)
router.register("interviews", InterviewViewSet)
router.register("cv_management", CVManagementViewSet)
router.register("CVAdd", CVAddViewSet) 
router.register("it_provisions", ITProvisionViewSet)
router.register("admin_provisions", AdminProvisionViewSet)
router.register("finance_provisions", FinanceProvisionViewSet)
router.register("employee_attachments", EmployeeAttachmentListCreateView)
router.register("tad_groups", TADGroupsViewSet)
router.register("employee_termination", EmployeeTerminationViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
]
