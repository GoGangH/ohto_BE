# Generated by Django 4.0 on 2022-11-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_demo', '0010_alter_playlist_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album_cover',
            field=models.URLField(blank=True),
        ),
    ]
