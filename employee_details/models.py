# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
import mimetypes
from datetime import time
from django.core.exceptions import ValidationError
from django.http import JsonResponse
import json
import logging


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
    name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)  
    interview_date = models.DateTimeField()
    interviewee_confirmed = models.BooleanField(default=False) 
    feedback_provided = models.BooleanField(default=False) 
    english_proficiency = models.BooleanField(default=False)  
    good_behaviour = models.BooleanField(default=False)  
    relevant_skills = models.BooleanField(default=False)  
    cultural_fit = models.BooleanField(default=False)  
    clarity_of_communication = models.BooleanField(default=False)  
    interview_questions = models.TextField(blank=True, null=True)  
    interview_mark = models.IntegerField(blank=True, null=True)
    interview_result = models.CharField(max_length=255, blank=True, null=True)
    interview_notes = models.TextField(blank=True, null=True)



    def __str__(self):
        return f"Interview - {self.name}"



# CV Management Model
from django.db import models

class LetterSend(models.Model):
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
    age = models.IntegerField(blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True,blank=True, null=True)
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


class Mdsir(models.Model):
    email = models.EmailField()
    interview_details = models.JSONField(null=True, blank=True)  # Add this field to store interview details as JSON

    def __str__(self):
        return f"Mdsir - {self.email}"
    
class InviteMail(models.Model):
    description = models.TextField(blank=True, null=True)
    interview_details = models.JSONField(null=True, blank=True)  # Add this field to store interview details as JSON
    
    def __str__(self):
        return f"InviteMail - {self.description}"

# Function to Send Email for CV Management and Create Notification

@receiver(post_save, sender=LetterSend)
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


# @receiver(post_save, sender=Mdsir)
# def payroll_email(sender, instance, **kwargs):
#     if  instance.email:
#         subject = ""
        
#         message = f"Dear ankon."

#         email = EmailMessage(
#             subject=subject,
#             body=message,
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             to=[instance.email],
#         )
#         email.send(fail_silently=True)

#         # Log Email
#         EmailLog.objects.create(
#             recipient=instance.email,
#             subject=subject,
#             message=message
#         )



def save_mdsir_details(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            interview_details = data.get('interview_details')

            # Create or update the Mdsir instance
            mdsir_instance, created = Mdsir.objects.update_or_create(
                email=email, defaults={'interview_details': interview_details}
            )

            return JsonResponse({'message': 'Mdsir instance created/updated successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@receiver(post_save, sender=Mdsir)
def email(sender, instance, **kwargs):
    # Now interview_details will be available in the instance
    interview_details = instance.interview_details or {}
    # Generate a link for the Interview Update Page
    frontend_url = "http://localhost:5173/interviews"  # Update this with your actual frontend URL
    interview_id = interview_details.get('id', '')  # Assuming each interview has an 'id'
    update_link = f"{frontend_url}?interview_id={interview_id}"

    if instance.email:
        subject = "Interview Details"

        message = f"""
        Dear MD Sir,

        Here are the interview details:

        Name: {interview_details.get('name', 'N/A')}
        Age: {interview_details.get('age', 'N/A')}
        Reference: {interview_details.get('reference', 'N/A')}
        Email: {interview_details.get('email', 'N/A')}
        Phone: {interview_details.get('phone', 'N/A')}
        Interview Date: {interview_details.get('interview_date', 'N/A')}
        Interview Mark: {interview_details.get('interview_mark', 'N/A')}
        Interview Result: {interview_details.get('interview_result', 'N/A')}
        Interview Notes: {interview_details.get('interview_notes', 'No notes available')}
        Feedback Provided: {"Yes" if interview_details.get('feedback_provided') else "No"}
        English Proficiency: {"Yes" if interview_details.get('english_proficiency') else "No"}
        Good Behavior: {"Yes" if interview_details.get('good_behaviour') else "No"}
        Relevant Skills: {"Yes" if interview_details.get('relevant_skills') else "No"}
        Cultural Fit: {"Yes" if interview_details.get('cultural_fit') else "No"}
        Clarity of Communication: {"Yes" if interview_details.get('clarity_of_communication') else "No"}
        Interview Questions: {interview_details.get('interview_questions', 'No questions recorded')}

        Click the link below to update the interview details:
        {update_link}

        Best Regards,
        HR Team
        """

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.email],
        )
        email.send(fail_silently=True)

        # Log Email
        EmailLog.objects.create(
            recipient=instance.email,
            subject=subject,
            message=message
        )

def save_invite_details(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            description = data.get('description')
            interview_details = data.get('interview_details')

            # Create or update the Mdsir instance
            mdsir_instance, created = InviteMail.objects.update_or_create(
                description=description, defaults={'interview_details': interview_details}
            )

            return JsonResponse({'message': 'Mdsir instance created/updated successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@receiver(post_save, sender=InviteMail)
def send_invitation_email(sender, instance, **kwargs):
    interview_details = instance.interview_details or {}

    if instance.description:
        subject = "Invitation Mail"

        message = f"""
        Dear {interview_details.get('name', 'N/A')},

        Here are the interview details:

        Name: {interview_details.get('name', 'N/A')}
        Reference: {interview_details.get('reference', 'N/A')}
        Email: {interview_details.get('email', 'N/A')}
        Phone: {interview_details.get('phone', 'N/A')}
        Interview Date: {interview_details.get('interview_date', 'N/A')}

        Message from HR:
        {instance.description}

        Best Regards,
        HR Team
        """

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[interview_details.get('email')],
        )
        email.send(fail_silently=True)

        # Log Email
        EmailLog.objects.create(
            recipient=interview_details.get('email'),
            subject=subject,
            message=message
        )