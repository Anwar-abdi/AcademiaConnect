from django import forms
from .models import Student, ChapterRegistration, Chapter  # Added Chapter import

class StudentRegistrationForm(forms.ModelForm):
    chapter = forms.ModelChoiceField(queryset=Chapter.objects.all())

    class Meta:
        model = Student
        fields = ['full_name', 'registration_number', 'access_number', 
                 'email', 'course', 'student_id_scan']

    def clean_registration_number(self):
        reg_number = self.cleaned_data.get('registration_number')
        if ChapterRegistration.objects.filter(
            student__registration_number=reg_number
        ).exists():
            raise forms.ValidationError('You are already registered for a chapter.')
        return reg_number