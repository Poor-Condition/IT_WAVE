# Generated by Django 3.1 on 2020-09-01 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(db_column='제목', max_length=400)),
                ('news_url', models.URLField(db_column='링크', max_length=400)),
                ('image_link', models.CharField(db_column='이미지', max_length=400)),
                ('published_date', models.CharField(db_column='등록날짜', max_length=400)),
                ('field', models.CharField(db_column='분류', max_length=50)),
                ('news_text', models.CharField(db_column='내용', max_length=500)),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_title', models.CharField(db_column='공모이름', max_length=400)),
                ('contest_image', models.CharField(db_column='이미지', max_length=400)),
                ('contest_category', models.CharField(db_column='분야', max_length=400)),
                ('contest_participant', models.CharField(db_column='응모대상', max_length=400)),
                ('contest_organizer', models.CharField(db_column='주최/주관', max_length=400)),
                ('contest_sponsor', models.CharField(db_column='후원/협찬', max_length=400)),
                ('contest_period', models.CharField(db_column='접수기간', max_length=400)),
                ('contest_money', models.CharField(db_column='총 상금', max_length=400)),
                ('contest_firstmoney', models.CharField(db_column='1등 상금', max_length=400)),
                ('contest_homepage', models.CharField(db_column='홈페이지', max_length=400)),
                ('contest_file', models.CharField(db_column='첨부파일', max_length=400)),
                ('contest_views', models.IntegerField(db_column='조회수')),
                ('field', models.CharField(db_column='분류', max_length=50)),
            ],
            options={
                'db_table': 'contest',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(db_column='기업명', max_length=100)),
                ('job_title', models.CharField(db_column='직무', max_length=300)),
                ('experience', models.CharField(db_column='경력사항', max_length=300)),
                ('edu_level', models.CharField(db_column='학력', max_length=50)),
                ('type', models.CharField(db_column='근무형태', max_length=50)),
                ('location', models.CharField(db_column='근무지', max_length=50)),
                ('category', models.CharField(db_column='분류', max_length=300)),
                ('link', models.CharField(db_column='상세링크', max_length=300)),
                ('field', models.CharField(db_column='분류필터', max_length=50)),
            ],
            options={
                'db_table': 'job_list',
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('max_member', models.IntegerField(default=4)),
                ('members', models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'study',
            },
        ),
    ]
