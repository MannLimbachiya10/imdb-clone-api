# Generated by Django 5.0.6 on 2024-06-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_user_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='number_Of_Ratings',
            field=models.IntegerField(default=0),
        ),
    ]
