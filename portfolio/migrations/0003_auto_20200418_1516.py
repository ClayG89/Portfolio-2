# Generated by Django 3.0.5 on 2020-04-18 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogs',
            new_name='Blog',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='blogs',
            new_name='blog',
        ),
    ]
