# Generated by Django 2.1.1 on 2018-09-19 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0002_remove_hashtag_bot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='diff_id',
            new_name='rc_id',
        ),
    ]