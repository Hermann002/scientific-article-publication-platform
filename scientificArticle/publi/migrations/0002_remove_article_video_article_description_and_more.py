# Generated by Django 4.2.1 on 2023-06-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='video',
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default='Entrer du texte'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='scientific'),
        ),
    ]