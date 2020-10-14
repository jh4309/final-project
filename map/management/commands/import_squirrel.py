
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Get squirrels information'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help = 'file contain squirrel details')
    
    def handle(self, *args, **options):
        file_ = options['squirrel_file']
        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
    
