# Generated by Django 3.1 on 2020-08-19 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
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
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='user',
            table='auth_user',
        ),
    ]