# Generated by Django 4.0.5 on 2022-07-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_about_description_alter_blog_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='caption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
