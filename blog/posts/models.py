from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def summary(self):
        self.size = 200
        summary_text = self.body[:self.size]
        if summary_text[-1] == " ":
            return summary_text[:-1]
        else:
            return summary_text
