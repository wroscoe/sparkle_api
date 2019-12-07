from django.db import models

class Quiz(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()


    def get_questions(self):
        return self.question_set.all()


    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    youtube_url = models.CharField(max_length=255)
    question_text = models.TextField()
    order = models.IntegerField()

    def get_answers(self):
        return self.question_set.all()

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question,  on_delete=models.CASCADE)

    content = models.CharField(max_length=1000,
                               blank=False)

    correct = models.BooleanField(blank=False,
                                  default=False)

    def __str__(self):
        return self.content
