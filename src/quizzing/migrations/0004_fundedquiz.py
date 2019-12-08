# Generated by Django 2.2.1 on 2019-12-07 23:49

from django.db import migrations, models
import django.db.models.deletion
import quizzing.models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzing', '0003_auto_20191207_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundedQuiz',
            fields=[
                ('id', models.CharField(default=quizzing.models.create_secret_id, editable=False, max_length=255, primary_key=True, serialize=False)),
                ('complete', models.BooleanField(default=False)),
                ('percent_correct', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('amount', models.IntegerField(default=0)),
                ('redeemed', models.BooleanField(default=False)),
                ('lightning_gift_order_id', models.CharField(max_length=255, null=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quizzing.Quiz')),
            ],
        ),
    ]