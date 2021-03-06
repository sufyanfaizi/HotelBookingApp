# Generated by Django 2.2.4 on 2019-09-21 04:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RealTodo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewTodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(default=datetime.datetime(2019, 9, 21, 4, 44, 36, 521175))),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HotelBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('booking_details', models.TextField()),
                ('booked_on', models.DateTimeField(default=datetime.datetime(2019, 9, 21, 4, 44, 36, 521830))),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
