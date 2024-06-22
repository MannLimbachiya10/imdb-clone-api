# Generated by Django 5.0.6 on 2024-06-15 14:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_watchlist_streamingplatform_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='x',
            new_name='watchlist',
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
