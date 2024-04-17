import csv
from django.core.management.base import BaseCommand
from performance.models import Performance


# 명령어로 사용 -> python manage.py read_csv_performance csv파일경로
class Command(BaseCommand):
    help = 'CSV 파일을 DB로 이전합니다.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        try:
            self.import_data(csv_file)
            self.stdout.write(self.style.SUCCESS('Performance_CSV 파일 이전 완료'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found. Please check the file again.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An unknown error occurred: {e}'))

    def import_data(self, csv_file):
        with open(csv_file, 'r', encoding='UTF8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.create_performance(row)

    def create_performance(self, data):
        try:
            Performance.objects.create(
                performance_num=data['performance_num'],
                title=data['title'],
                location=data['location'],
                start_date=data['start_date'],
                end_date=data['end_date'],
                performance_time=data['performance_time'],
                age_requirement=data['age_requirement'],
                performance_type=data['performance_type'],
            )
        except Exception as e:
            self.handle_error(data, e)

    def handle_error(self, data, exception):
        self.stdout.write(self.style.ERROR(f'Error: {data}'))
        self.stdout.write(self.style.ERROR(f'Error detail: {exception}'))
