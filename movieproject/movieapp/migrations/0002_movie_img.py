# Generated by Django 4.1.6 on 2023-02-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='hai', upload_to=''),
            preserve_default=False,
        ),
    ]
