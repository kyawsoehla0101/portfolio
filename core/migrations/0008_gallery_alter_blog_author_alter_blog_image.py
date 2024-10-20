# Generated by Django 4.0.5 on 2022-07-22 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_remove_hero_typing_hero_typing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Kyaw Soe Hla', max_length=100, null=True)),
                ('image', models.ImageField(upload_to='static/%Y/%m/%d/images')),
                ('caption', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
                'ordering': ('-created',),
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(default='Kyaw Soe Hla', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, default='static/assets/img/hero-bg.jpg', null=True, upload_to='static/%Y/%m/%d/blogimages'),
        ),
    ]
