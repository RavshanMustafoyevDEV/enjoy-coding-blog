# Generated by Django 4.0.6 on 2022-07-29 21:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
