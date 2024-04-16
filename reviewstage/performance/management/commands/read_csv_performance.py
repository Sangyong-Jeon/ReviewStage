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
			with open(csv_file, 'r') as file:
				reader = csv.DictReader(file)

				for row in reader:
					try:
						performance = Performance.objects.create(
							performance_num=int(row['performance_num']),
							title=row['title'],
							location=row['location'],
							start_date=row['start_date'],
							end_date=row['end_date'],
							performance_time=row['performance_time'],
							age_requirement=row['age_requirement'],
							performance_type=row['performance_type'],
							image_path=row['image_path']
						)
						# file_instance = File.objects.create(
						# 	performance_id=performance,
						# 	name=row['name'],
						# 	store_path=row['store_path']
						# )
					except Exception as e:
						self.stdout.write(self.style.ERROR(f'Error: {row}'))
						self.stdout.write(self.style.ERROR(f'Error detail: {e}'))
		except FileNotFoundError:
			self.stdout.write(self.style.ERROR('File not found. Please check the file again.'))
		except Exception as e:
			self.stdout.write(self.style.ERROR(f'An unknown error occurred.{e}'))

		self.stdout.write(self.style.SUCCESS('CSV 파일 이전 완료'))