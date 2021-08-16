# Generated by Django 3.2.6 on 2021-08-16 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Treasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('longitude', models.PositiveIntegerField()),
                ('latitude', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='author_id', to=settings.AUTH_USER_MODEL)),
                ('hunters', models.ManyToManyField(related_name='hunter_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
