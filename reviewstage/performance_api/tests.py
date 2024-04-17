from django.test import TestCase
from .serializers import PerformanceSerializer


class PerformanceSerializerTestCase(TestCase):

	def test_performance_serializer_validation(self):
		data = {
			'performance_num': '23001653213',
			'title': '영웅',
			'location': '블루스퀘어 신한카드홀',
			'start_date': '2023.03.17',
			'end_date': '2023.05.21',
			'performance_time': '160분(인터미션 20분 포함)',
			'age_requirement': '8세이상 관람가능',
			'performance_type': '뮤지컬'
		}

		serializer = PerformanceSerializer(data=data)
		self.assertTrue(serializer.is_valid())

	def test_performance_serializer_id_invalidation(self):
		data = {
			'performance_num': '',
			'title': '영웅',
			'location': '블루스퀘어 신한카드홀',
			'start_date': '2023.03.17',
			'end_date': '2023.05.21',
			'performance_time': '160분(인터미션 20분 포함)',
			'age_requirement': '8세이상 관람가능',
			'performance_type': '뮤지컬'
		}

		serializer = PerformanceSerializer(data=data)
		self.assertFalse(serializer.is_valid())
		print(serializer.errors)

	def test_performance_serializer_title_invalidation(self):
		data = {
			'performance_num': '23001653213',
			'title': '',
			'location': '블루스퀘어 신한카드홀',
			'start_date': '2023.03.17',
			'end_date': '2023.05.21',
			'performance_time': '160분(인터미션 20분 포함)',
			'age_requirement': '8세이상 관람가능',
			'performance_type': '뮤지컬'
		}

		serializer = PerformanceSerializer(data=data)
		self.assertFalse(serializer.is_valid())
		print(serializer.errors)

