# Generated by Django 4.0.5 on 2022-07-22 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rate', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skill',
            },
        ),
    ]
