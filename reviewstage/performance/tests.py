from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import Performance, Review, File
from django.core.management import call_command
from rest_framework.exceptions import ValidationError


class ReadCsvTestCase(TestCase):
	def test_read_csv_command(self):
		csv_path = 'performance/management/commands/test_data.csv'

		call_command('read_csv_performance', csv_path)
		call_command('read_csv_review', csv_path)

		self.assertEqual(Performance.objects.count(), 20)
		self.assertEqual(Review.objects.count(), 20)


class PerformanceTestCase(TestCase):
	def setUp(self):
		self.performance = Performance.objects.create(
			performance_num='23001653213',
			title='영웅',
			location='블루스퀘어 신한카드홀',
			start_date='2023.03.17',
			end_date='2023.05.21',
			performance_time='160분(인터미션 20분 포함)',
			age_requirement='8세이상 관람가능',
			performance_type='뮤지컬',
		)

	def test_valid(self):
		self.performance.save()
		self.assertEqual(Performance.objects.count(), 1)

	def test_performance_title(self):
		self.assertEqual(self.performance.title, '영웅')

	def test_performance_title_max_length(self):
		max_length = Performance._meta.get_field('title').max_length
		self.assertLessEqual(len(self.performance.title), max_length)

	def test_performance_str_method(self):
		expected_str = f'제목 : {self.performance.title}, 장소 : {self.performance.location}, 공연 날짜 : {self.performance.start_date} ~ {self.performance.end_date}, 공연 번호: {self.performance.performance_num}'
		self.assertEqual(str(self.performance), expected_str)


class ReviewTestCase(TestCase):
	def setUp(self):
		self.performance = Performance.objects.create(
			performance_num='23001653213',
			title='영웅',
			location='블루스퀘어 신한카드홀',
			start_date='2023.03.17',
			end_date='2023.05.21',
			performance_time='160분(인터미션 20분 포함)',
			age_requirement='8세이상 관람가능',
			performance_type='뮤지컬'
		)

		self.review = Review.objects.create(
			performance_id=self.performance,
			review_num='20240417',
			title='추천합니다',
			content='ReviewContent, ReviewContent, ReviewContent, ReviewContent, ReviewContent, ReviewContent',
			user_id='user',
			rating=4,
			date='2024.04.17',
			likes_count=4,
			view_count=17
		)

	def test_review_title(self):
		self.assertEqual(self.review.title, '추천합니다')
