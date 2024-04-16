import csv
from django.core.management.base import BaseCommand
from performance.models import Review


# 명령어로 사용 -> python manage.py read_csv_review csv파일경로
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
						review = Review.objects.create(
							performance_id=int(row['performance_num']),
							review_num=int(row['review_num']),
							title=row['title'],
							content=row['content'],
							user_id=row['user_id'],
							rating=int(row['rating']),
							date=row['date'],
							likes_count=int(row['likes_count']),
							view_count=int(row['view_count'])
						)
					except Exception as e:
						self.stdout.write(self.style.ERROR(f'Error: {row}'))
						self.stdout.write(self.style.ERROR(f'Error detail: {e}'))
		except FileNotFoundError:
			self.stdout.write(self.style.ERROR('File not found. Please check the file again.'))
		except Exception as e:
			self.stdout.write(self.style.ERROR(f'An unknown error occurred.{e}'))

		self.stdout.write(self.style.SUCCESS('CSV 파일 이전 완료'))