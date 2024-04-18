from django.db import models
from django.contrib.auth.models import User


class Performance(models.Model):
    performance_num = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    performance_time = models.CharField(max_length=50)
    age_requirement = models.CharField(max_length=50)
    performance_type = models.CharField(max_length=50)

    def __str__(self):
        return f'제목 : {self.title}, 장소 : {self.location}, 공연 날짜 : {self.start_date} ~ {self.end_date}, 공연 번호: {self.performance_num}'


class Review(models.Model):
    performance_id = models.ForeignKey(Performance, on_delete=models.CASCADE)
    review_num = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField()
    user_id = models.CharField(max_length=50)
    rating = models.IntegerField()
    date = models.CharField(max_length=50)
    likes_count = models.IntegerField()
    view_count = models.IntegerField()

    def __str__(self):
        return f'제목 : {self.title}, 후기 번호: {self.review_num}, 내용 : {self.content}, 공연 번호: {self.performance_id}'


class File(models.Model):
    performance_id = models.ForeignKey(Performance, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='visual/', default='default_visual.png')


    def __str__(self):
        return f'파일명 : {self.name}'


# class Member(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     member_id = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    performance = models.ForeignKey('Performance', on_delete=models.CASCADE)

    def __str__(self):
        return f'사용자: {self.user}, 제목: {self.performance.title}'