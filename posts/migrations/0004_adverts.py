# Generated by Django 2.2 on 2019-05-11 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_posts_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adverts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_title', models.CharField(max_length=200)),
                ('ad_body', models.TextField()),
                ('ad_created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
