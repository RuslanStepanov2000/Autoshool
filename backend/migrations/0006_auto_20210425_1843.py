# Generated by Django 3.2 on 2021-04-25 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_schedule_isactive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='isActive',
        ),
        migrations.RemoveField(
            model_name='student',
            name='drive',
        ),
        migrations.AddField(
            model_name='schedule',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.student', verbose_name='Ученик'),
        ),
    ]