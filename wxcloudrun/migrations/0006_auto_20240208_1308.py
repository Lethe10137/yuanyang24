# Generated by Django 3.2.8 on 2024-02-08 13:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wxcloudrun', '0005_auto_20240203_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counters',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 13, 8, 16, 755118)),
        ),
        migrations.AlterField(
            model_name='counters',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 13, 8, 16, 755129)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 8, 13, 8, 16, 755991)),
        ),
        migrations.CreateModel(
            name='Skip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2024, 2, 8, 13, 8, 16, 756154))),
                ('question_id', models.IntegerField(default=0)),
                ('cost', models.PositiveIntegerField()),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wxcloudrun.group')),
            ],
            options={
                'db_table': 'Skip',
            },
        ),
    ]
