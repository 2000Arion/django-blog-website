# Generated by Django 5.0.2 on 2024-02-27 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_rename_autor_post_autor_rename_inhalt_post_inhalt_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-erstellt']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_on',
            new_name='aktualisiert',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='erstellt',
        ),
    ]
