# Generated by Django 4.2.3 on 2023-08-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('najot', '0002_doktor_tajriba'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_link', models.CharField(max_length=3000)),
                ('phone', models.CharField(max_length=21)),
                ('email', models.EmailField(max_length=254)),
                ('address_uz', models.CharField(max_length=589)),
                ('address_ru', models.CharField(max_length=589)),
                ('address_en', models.CharField(max_length=589)),
                ('telegram', models.CharField(max_length=589)),
                ('insagram', models.CharField(max_length=589)),
                ('facebook', models.CharField(max_length=589)),
                ('twetter', models.CharField(max_length=589)),
                ('tiktok', models.CharField(max_length=589)),
                ('youtube', models.CharField(max_length=589)),
            ],
        ),
    ]