from django.core.management.base import BaseCommand
from chapters.models import Chapter

class Command(BaseCommand):
    help = 'Creates initial chapters'

    def handle(self, *args, **kwargs):
        chapters_data = [
            {
                'name': 'CS',
                'description': 'Join the Cyber Security chapter to learn about digital security, ethical hacking, and network protection.',
                'requirements': 'Open to all Computing and Technology students with interest in cyber security.'
            },
            {
                'name': 'AR',
                'description': 'Explore the world of AI & Robotics through hands-on projects and research.',
                'requirements': 'Basic programming knowledge required. Open to all Computing and Technology students.'
            },
            {
                'name': 'SE',
                'description': 'Learn software development best practices, project management, and modern development tools.',
                'requirements': 'Open to all Computing and Technology students interested in software development.'
            },
            {
                'name': 'GM',
                'description': 'Create exciting games and learn about game development technologies.',
                'requirements': 'Basic programming knowledge required. Open to all Computing and Technology students.'
            },
        ]

        for chapter_data in chapters_data:
            Chapter.objects.get_or_create(
                name=chapter_data['name'],
                defaults={
                    'description': chapter_data['description'],
                    'requirements': chapter_data['requirements']
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully created initial chapters'))