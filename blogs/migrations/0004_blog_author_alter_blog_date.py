# Generated by Django 5.1.4 on 2025-01-08 03:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blog_blog_image_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='Anonymous', max_length=122),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
