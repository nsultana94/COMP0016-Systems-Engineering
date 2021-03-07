# Generated by Django 3.1.5 on 2021-03-05 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CFP_Portal', '0014_auto_20210305_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rejectedprojects',
            name='id',
        ),
        migrations.AlterField(
            model_name='rejectedprojects',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='CFP_Portal.person'),
        ),
    ]
