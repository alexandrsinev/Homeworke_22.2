# Generated by Django 5.0.4 on 2024-05-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('contents', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(upload_to='preview/', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('published_at', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'записи',
            },
        ),
    ]
