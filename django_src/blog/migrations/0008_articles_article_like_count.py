# Generated by Django 3.1 on 2020-09-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200901_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='article_like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
