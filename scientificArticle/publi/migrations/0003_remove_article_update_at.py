# Generated by Django 4.2.1 on 2023-06-02 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publi', '0002_remove_article_video_article_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='update_at',
        ),
    ]
