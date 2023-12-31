# Generated by Django 4.2.6 on 2023-11-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0006_social_media_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='social_media_links',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='is_freelance',
            field=models.CharField(blank=True, default='available', max_length=50),
        ),
    ]
