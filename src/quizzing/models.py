from django.db import models
import uuid, secrets

def create_secret_id():
    return secrets.token_urlsafe(24)


class Quiz(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()


    def get_questions(self):
        return self.question_set.all()


    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    youtube_url = models.CharField(max_length=255)
    question_text = models.TextField()
    order = models.IntegerField()

    def get_answers(self):
        return self.question_set.all()

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question,  related_name='answers', on_delete=models.CASCADE)

    content = models.CharField(max_length=1000,
                               blank=False)

    correct = models.BooleanField(blank=False,
                                  default=False)

    def __str__(self):
        return self.content


class FundedQuiz(models.Model):
    """
    Record which quizzes are funded.
    """
    id = models.CharField(primary_key=True, default=create_secret_id, editable=False, max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    complete = models.BooleanField(default=False)
    percent_correct = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    amount = models.IntegerField(default=0)
    redeemed = models.BooleanField(default=False)
    opennode_withdraw_id = models.CharField(max_length=255, null=True, blank=True)
    opennode_charge_id = models.CharField(max_length=255, null=True, blank=True)
    lightning_gift_order_id = models.CharField(max_length=255, null=True, blank=True) # leaving as option to use lightning node

