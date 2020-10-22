from django.core.management.base import BaseCommand
import csv
from datetime import datetime, date
from map.models import sighting
class Command(BaseCommand):
    help = 'Get squirrels information'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help = 'file contain squirrel details')
    
    def handle(self, *args, **options):
        file_ = options['squirrel_file']
        with open(file_) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        def convertBool(str_):
            if str(str_) in ['TRUE', 'true', 'True']:
                str_ = True
            elif str(str_) in ['FALSE', 'false', 'False']:
                str_ = False
            else:
                str_ = None
            return str_

        for item in data:
            s = sighting(
                latitude = item['X'],
                longitude = item['Y'],
                shift = item['Shift'],
                date = datetime(int(item['Date'][-4:]),int(item['Date'][:2]), int(item['Date'][2:4]))
                age = item['Age'],
                uniquesid = item['Unique Squirrel ID'],
                Primary_Fur_Color = item['Primary Fur Color'],
                Location = item['Location'],
                Specific_Location = item['Specific Location'],
                Running = convertBool(item['Running']),
                Chasing = convertBool(item['Chasing']),
                Climbing = convertBool(item['Climbing']),
                Eating = convertBool(item['Eating']),
                Foraging = convertBool(item['Foraging']),
                Other_Activities = item['Other Activities'],
                Kuks = convertBool(item['Kuks']),
                Quaas = convertBool(item['Quaas']),
                Moans = convertBool(item['Moans']),
                Tail_Flags = convertBool(item['Tail flags']),
                Tail_Twitches = convertBool(item['Tail twitches']),
                Approaches = convertBool(item['Approaches']),
                Indifferent = convertBool(item['Indifferent']),
                Runs_From = convertBool(item['Runs from']),
                )

            s.save()
        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
    
