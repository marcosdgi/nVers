from django.db import models


class Mail(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    sender_mail = models.EmailField()

    class Meta:
        verbose_name_plural = "Mails"

    def __str__(self):
        return self.sender_mail
