# Generated by Django 5.0.6 on 2024-06-15 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_watchlist_streamingplatform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='StreamingPlatform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='api.streamplatfrom'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('x', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.watchlist')),
            ],
        ),
    ]
