from django.db import models


# Create your models here.
class Info(models.Model):
	# perform_num = models.ForeignKey()
	title_text = models.CharField(max_length=50)
	location_text = models.CharField(max_length=50)
	age = models.IntegerField()
	start_date = models.DateField()
	end_date = models.DateField()
	perform_time = models.DateTimeField()
	perform_type = models.CharField(max_length=50)

	def __str__(self):
		return f'제목 : {self.title_text}, 장소 : {self.location_text}, 공연 날짜 : {self.start_date} ~ {self.end_date}'
