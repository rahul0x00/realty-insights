
from django.core.management.base import BaseCommand
import json
import pandas as pd

class Command(BaseCommand):
    help = 'Load data from JSON file into a Pandas DataFrame'

    def handle(self, *args, **options):
        file_path = 'data.json'  
        with open(file_path, 'r') as file:
            data = json.load(file)
        df = pd.DataFrame(data)

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))

