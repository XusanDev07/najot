# Generated by Django 4.2.3 on 2023-08-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('najot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doktor',
            name='tajriba',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
