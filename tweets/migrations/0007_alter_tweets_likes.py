# Generated by Django 3.2.6 on 2021-08-17 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0006_auto_20210817_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='likes',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
