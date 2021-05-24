from django.db import models


# Create your models here.


class Board(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=128,
                             verbose_name='Title')
    contents = models.TextField(verbose_name='Contents')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE,
                               verbose_name='Uploader')
    registered_dtm = models.DateTimeField(auto_now_add=True,
                                          verbose_name='등록시간')

    # models.SET_NULL, models.SET_DEFAULT

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시물'
        verbose_name_plural = '패스트캠퍼스 게시물'
