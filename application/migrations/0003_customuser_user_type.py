# Generated by Django 5.0.1 on 2024-01-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_customuser_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('student', 'student'), ('professor', 'professor'), ('director', 'director')], default='student', max_length=15),
        ),
    ]
