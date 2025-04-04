from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Chapter, Student, ChapterRegistration
from .forms import StudentRegistrationForm
from django.db import transaction

def home(request):
    chapters = Chapter.objects.all()
    return render(request, 'chapters/home.html', {'chapters': chapters})

def chapter_detail(request, chapter_code):
    chapter = get_object_or_404(Chapter, name=chapter_code)
    return render(request, 'chapters/chapter_detail.html', {'chapter': chapter})

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Save the student
                    student = form.save()
                    
                    # Create chapter registration
                    chapter = form.cleaned_data['chapter']
                    ChapterRegistration.objects.create(
                        student=student,
                        chapter=chapter,
                        status='PENDING'
                    )
                    
                    messages.success(request, 'Registration submitted successfully!')
                    return redirect('chapters:registration_status')
            except Exception as e:
                messages.error(request, 'An error occurred during registration. Please try again.')
    else:
        form = StudentRegistrationForm()
        
    return render(request, 'chapters/register.html', {'form': form})

def registration_status(request):
    if 'registration_number' in request.GET:
        reg_number = request.GET['registration_number']
        try:
            registration = ChapterRegistration.objects.get(
                student__registration_number=reg_number
            )
            return render(request, 'chapters/registration_status.html', 
                        {'registration': registration})
        except ChapterRegistration.DoesNotExist:
            messages.error(request, 'Registration not found.')
    return render(request, 'chapters/registration_status.html')
