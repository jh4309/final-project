from django.core.management.base import BaseCommand
import csv
from map.models import sighting
class Command(BaseCommand):
    help = 'Get squirrels information'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help = 'file contain squirrel details')
    
    def handle(self, *args, **options):
        file_ = options['squirrel_file']
        with open(file_) as fp:
            reader = csv.DictReader(fp)
            for item in reader:
                obj = sighting()
                obj.latitude = item['X']
                obj.longitude = item['Y']
                obj.shift = item['Shift']
                obj.date = item['Date']
                obj.age = item['Age']
                obj.uniquesid = item['Unique Squirrel ID']

                obj.save()
        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
    
