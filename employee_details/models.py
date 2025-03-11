from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
import logging
from django.core.exceptions import ValidationError
import mimetypes
from datetime import time
from .models import *
logger = logging.getLogger(__name__)
# Email Log Model
class EmailLog(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email to {self.recipient} at {self.sent_at}"


from django.db import models

class TADGroups(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.company_name   

# Employee Details Model
class EmployeeDetails(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    joining_date = models.DateField()
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    mail_address = models.TextField()
    personal_phone = models.CharField(max_length=20)
    office_phone = models.CharField(max_length=20)
    reference_phone = models.CharField(max_length=20, blank=True, null=True)
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    company = models.ForeignKey(TADGroups, on_delete=models.CASCADE, related_name='employees', null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    reporting_leader = models.CharField(max_length=255)
    special_skills = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to="employee_images/")
    permanent_address = models.TextField()

    def __str__(self):
        return self.name

class EmployeeTermination(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    company = models.ForeignKey(TADGroups, on_delete=models.CASCADE, related_name='terminated_employees', null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class TerminationAttachment(models.Model):
    employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    file = models.FileField(upload_to="termination_attachments/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)  # Add description field

    def __str__(self):
        return f"{self.employee.name} - {self.file.name}" 
# Attendance Model
class Attendance(models.Model):
    employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in = models.TimeField()
    check_out = models.TimeField(null=True, blank=True)
    office_start_time = models.TimeField(default=time(9, 30))  # New field for office start time

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

    # Method to check if check-in is after office start time
    def is_late_check_in(self):
        return self.check_in > self.office_start_time  # Compare check-in with dynamic office start time

class EmployeeAttachment(models.Model):
    employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE, related_name="attachments")
    file = models.FileField(upload_to="employee_attachments/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)  # Add description field

    def __str__(self):
        return f"{self.employee.name} - {self.file.name}"


# Notification Model
class Notification(models.Model):
    employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)  # Fixed ForeignKey
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# Interview Model
class Interview(models.Model):
    candidate = models.CharField(max_length=255)  # Changed from ForeignKey to CharField
    interview_date = models.DateTimeField()
    interview_result = models.TextField()
    interview_notes = models.TextField(blank=True, null=True)
    interview_pdf = models.FileField(upload_to="interviews/", blank=True, null=True)

    def __str__(self):
        return f"Interview - {self.candidate}"


# CV Management Model
from django.db import models

class CVManagement(models.Model):
    OFFER_LETTER = "Offer Letter"
    APPOINTMENT_LETTER = "Appointment Letter"
    JOINING_REPORT = "Joining Report"

    LETTER_CHOICES = [
    ("offer_letter", "Offer Letter"),
    ("appointment_letter", "Appointment Letter"),
    ("joining_report", "Joining Report"),
]
    name = models.CharField(max_length=255)
    email = models.EmailField()
    letter_file = models.FileField(upload_to="cv_letters/")
    letter_type = models.CharField(choices=LETTER_CHOICES, max_length=50)
    def __str__(self):
        return f"CV - {self.name}"


class CVAdd(models.Model):
    name = models.CharField(max_length=255)
    cv_file = models.FileField(upload_to='cv_adds/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ITProvision(models.Model):
    employee = models.CharField(max_length=255)
    id_card = models.BooleanField(default=False)
    laptop = models.BooleanField(default=False)

class AdminProvision(models.Model):
    employee = models.CharField(max_length=255)
    bank_account_paper = models.BooleanField(default=False)
    sim_card = models.BooleanField(default=False)
    visiting_card = models.BooleanField(default=False)
    placement = models.BooleanField(default=False)

# Finance Provision Model
class FinanceProvision(models.Model):
    employee = models.CharField(max_length=255)
    email = models.EmailField()
    payroll_pdf = models.FileField(upload_to='payroll_pdfs/')

    def __str__(self):
        return f"Provision for {self.employee}"



# Function to Send Email for CV Management and Create Notification

@receiver(post_save, sender=CVManagement)
def send_cv_email(sender, instance, **kwargs):
    logger.info(f"Handling CV email for {instance.name}")
    subject = f"{instance.letter_type} for {instance.name}"
    message = f"Dear {instance.name},\n\nPlease find your {instance.letter_type} attached.\n\nBest Regards,\nHR Team"

    # Create an EmailMessage instance
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[instance.email]
    )

    # Check if the file is provided and attach it
    if instance.letter_file:
        try:
            # Log the file path
            logger.info(f"Attaching file from {instance.letter_file.path}")

            # Get the MIME type (content type) based on the file extension
            mime_type, encoding = mimetypes.guess_type(instance.letter_file.name)
            if mime_type is None:
                mime_type = 'application/octet-stream'  # Fallback to a generic MIME type

            # Read the file as binary
            with instance.letter_file.open('rb') as file:
                email.attach(instance.letter_file.name, file.read(), mime_type)
            
            logger.info(f"Successfully attached file: {instance.letter_file.name}")
        except Exception as e:
            logger.error(f"Error attaching file {instance.letter_file.name}: {str(e)}")
            raise ValidationError(f"Error attaching file: {str(e)}")

    # Send the email
    try:
        email_sent = email.send(fail_silently=False)  # Set fail_silently=False for debugging
        if email_sent:
            logger.info(f"Email sent successfully to {instance.email}")
            
            # Log the email
            EmailLog.objects.create(
                recipient=instance.email,
                subject=subject,
                message=message
            )

            # Create a notification for sending the email
            try:
                employee = EmployeeDetails.objects.get(email=instance.email)
                Notification.objects.create(
                    employee=employee,
                    message=f"Email sent to {instance.name} regarding {instance.letter_type}."
                )
            except EmployeeDetails.DoesNotExist:
                logger.error(f"Employee with email {instance.email} not found for notification creation.")
        else:
            logger.error("Email sending failed, but no exception was raised.")
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")


# Auto-generate notification and send email when attendance_delay is True
@receiver(post_save, sender=Attendance)
def create_notification(sender, instance, **kwargs):
    # Check if the employee's check-in time is late
    if instance.is_late_check_in():
        message = f"Attendance delay recorded for {instance.employee.name} on {instance.date} at {instance.check_in}."

        # Send Email
        email_sent = send_mail(
            subject="Attendance Delay Alert",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.employee.email],
            fail_silently=True
        )

        if email_sent > 0:
            # Log Email
            EmailLog.objects.create(
                recipient=instance.employee.email,
                subject="Attendance Delay Alert",
                message=message
            )

        # Create Notification
        Notification.objects.create(
            employee=instance.employee, 
            message=message
        )


# Auto-generate notification when employee details are updated
@receiver(post_save, sender=EmployeeDetails)
def create_employee_notification(sender, instance, **kwargs):
    message = f"Employee details updated for {instance.name}."

    # Create Notification
    Notification.objects.create(
        employee=instance, 
        message=message
    )
@receiver(post_save, sender=FinanceProvision)
def payroll_email(sender, instance, **kwargs):
    if instance.payroll_pdf and instance.email:
        subject = "Your Payroll Document"
        
        # Use the 'employee' field directly as it's a CharField storing the employee name or identifier
        employee_name = instance.employee  # Directly access the 'employee' field
        
        message = f"Dear {employee_name},\n\nPlease find attached your payroll document."

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.email],
        )
        email.attach_file(instance.payroll_pdf.path)
        email.send(fail_silently=True)

        # Log Email
        EmailLog.objects.create(
            recipient=instance.email,
            subject=subject,
            message=message
        )
