# Generated by Django 2.2 on 2021-01-25 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CFP_Portal', '0004_organisation_organisation_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=130, verbose_name='name')),
                ('surname', models.CharField(default='', max_length=130, verbose_name='surname')),
                ('phone_number', models.CharField(default='', max_length=130, verbose_name='phone number')),
                ('email', models.EmailField(default='', max_length=130, verbose_name='email')),
                ('project_title', models.CharField(default='', max_length=130, verbose_name='title')),
                ('summarised_abstract', models.CharField(default='', max_length=2000, verbose_name='summarised abstract')),
                ('full_abstract', models.TextField(default='', verbose_name='full abstract')),
                ('expertiseskills', models.TextField(default='', verbose_name='expertise skills')),
                ('devices', models.TextField(default='', verbose_name='devices')),
                ('project_complexity', models.CharField(choices=[('Scaffolding', 'Scaffolding'), ('Discovery', 'Discovery'), ('Innovation', 'Innovation')], default='', max_length=20, verbose_name='project complexity')),
                ('source_type', models.CharField(choices=[('Open Source', 'Open Source'), ('Closed Source', 'Closed Source')], default='', max_length=20, verbose_name='open source or closed source')),
                ('ethics_form', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='', max_length=20, verbose_name='Have you completed the ethics form?')),
                ('launching_date', models.DateField(default='2021-01-25', verbose_name='launching date:')),
                ('motivations', models.TextField(default='', verbose_name='motivations')),
                ('importance', models.TextField(default='', verbose_name='why is your project important')),
                ('hashtags', models.CharField(default='hashtags', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisation_address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisation_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='overview',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
