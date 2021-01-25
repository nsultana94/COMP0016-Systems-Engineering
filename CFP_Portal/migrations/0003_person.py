# Generated by Django 3.1.5 on 2021-01-24 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CFP_Portal', '0002_auto_20210124_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('job_title', models.CharField(blank=True, max_length=30)),
                ('surname', models.TextField(blank=True)),
            ],
        ),
    ]
