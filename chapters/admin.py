from django.contrib import admin
from django.utils.html import format_html
from django.urls import path
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Student, Chapter, ChapterRegistration

@admin.register(ChapterRegistration)
class ChapterRegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'chapter', 'status', 'registration_date', 'approval_actions')
    list_filter = ('status', 'chapter', 'registration_date')
    search_fields = ('student__full_name', 'student__registration_number')
    
    def approval_actions(self, obj):
        if obj.status == 'PENDING':
            return format_html(
                '<a class="button" href="/admin/chapters/chapterregistration/{}/approve/">Approve</a> &nbsp;'
                '<a class="button" style="background: red; color: white;" href="/admin/chapters/chapterregistration/{}/reject/">Reject</a>',
                obj.id, obj.id
            )
        return obj.get_status_display()
    
    approval_actions.short_description = 'Actions'
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:object_id>/approve/', self.approve_registration, name='chapter_registration_approve'),
            path('<int:object_id>/reject/', self.reject_registration, name='chapter_registration_reject'),
        ]
        return custom_urls + urls
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<path:object_id>/approve/', self.approve_registration, name='chapter_registration_approve'),
            path('<path:object_id>/reject/', self.reject_registration, name='chapter_registration_reject'),
        ]
        return custom_urls + urls
    
    def approve_registration(self, request, object_id):
        try:
            registration = self.get_object(request, object_id)
            if registration and registration.status == 'PENDING':
                registration.status = 'APPROVED'
                registration.save()
                
                # Send approval email
                send_mail(
                    'Chapter Registration Approved',
                    f'Dear {registration.student.full_name},\n\n'
                    f'Your registration for the {registration.chapter.get_name_display()} chapter has been approved.\n\n'
                    'Welcome to the chapter!\n\n'
                    'Best regards,\nUCU Chapters Team',
                    settings.EMAIL_HOST_USER,
                    [registration.student.email],
                    fail_silently=False,
                )
                
                messages.success(request, f'Successfully approved registration for {registration.student}')
            else:
                messages.error(request, 'Registration not found or already processed.')
        except Exception as e:
            messages.error(request, f'Error approving registration: {str(e)}')
        
        return HttpResponseRedirect('../../')
    
    def reject_registration(self, request, object_id):
        try:
            registration = self.get_object(request, object_id)
            if registration and registration.status == 'PENDING':
                registration.status = 'REJECTED'
                registration.rejection_reason = 'Application rejected by administrator.'
                registration.save()
                
                # Send rejection email
                send_mail(
                    'Chapter Registration Status Update',
                    f'Dear {registration.student.full_name},\n\n'
                    f'Your registration for the {registration.chapter.get_name_display()} chapter has been reviewed.\n\n'
                    f'Unfortunately, we cannot approve your registration at this time.\n\n'
                    'Best regards,\nUCU Chapters Team',
                    settings.EMAIL_HOST_USER,
                    [registration.student.email],
                    fail_silently=False,
                )
                
                messages.success(request, f'Successfully rejected registration for {registration.student}')
            else:
                messages.error(request, 'Registration not found or already processed.')
        except Exception as e:
            messages.error(request, f'Error rejecting registration: {str(e)}')
        
        return HttpResponseRedirect('../../')

# Keep existing admin classes unchanged
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_name_display')
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'registration_number', 'course', 'email')
    search_fields = ('full_name', 'registration_number', 'email')
    list_filter = ('course',)
