# Generated by Django 5.0.2 on 2024-02-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_rename_author_post_autor_rename_content_post_inhalt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Status',
            field=models.IntegerField(choices=[(0, 'Entwurf'), (1, 'Veröffentlicht')], default=0),
        ),
    ]
