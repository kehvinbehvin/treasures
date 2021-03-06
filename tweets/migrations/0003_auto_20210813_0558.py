# Generated by Django 3.2.6 on 2021-08-13 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0002_auto_20210812_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweets',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweets',
            name='message',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
