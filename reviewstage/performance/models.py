from django.db import models


# Create your models here.
class Performance(models.Model):
	performance_num = models.IntegerField()
	title = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	start_date = models.DateField()
	end_date = models.DateField()
	performance_time = models.DateTimeField()
	age_requirement = models.IntegerField()
	performance_type = models.CharField(max_length=50)
	image_path = models.CharField(max_length=100)

	def __str__(self):
		return f'제목 : {self.title}, 장소 : {self.location}, 공연 날짜 : {self.start_date} ~ {self.end_date}, 공연 번호: {self.performance_num}'


class Review(models.Model):
	performance_id = models.ForeignKey(Performance, on_delete=models.CASCADE)
	review_num = models.IntegerField()
	title = models.CharField(max_length=50)
	content = models.TextField()
	user_id = models.CharField(max_length=50)
	rating = models.IntegerField()  # 소수점이 필요하면 Float로 변경
	date = models.DateField()
	likes_count = models.IntegerField()
	view_count = models.IntegerField()

	def __str__(self):
		return f'제목 : {self.title}, 후기 번호: {self.review_num}, 내용 : {self.content}, 공연 번호: {self.performance_id}'


class File(models.Model):
	performance_id = models.ForeignKey(Performance, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	store_path = models.CharField(max_length=100)

	def __str__(self):
		return f'파일명 : {self.name}'
