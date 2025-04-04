# Generated by Django 4.2 on 2025-04-04 16:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('CS', 'Cyber Security'), ('AR', 'AI & Robotics'), ('SE', 'Software Engineering'), ('GM', 'Gaming')], max_length=2, unique=True)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='Registration number must be in format UCU/YYYY/XXX', regex='^UCU/\\d{4}/\\d{3}$')])),
                ('access_number', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('course', models.CharField(choices=[('BCS', 'Bachelor of Computer Science'), ('BIT', 'Bachelor of Information Technology'), ('BSE', 'Bachelor of Software Engineering'), ('BIS', 'Bachelor of Information Systems')], max_length=3)),
                ('student_id_scan', models.ImageField(upload_to='student_ids/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChapterRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=10)),
                ('rejection_reason', models.TextField(blank=True, null=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapters.chapter')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chapters.student')),
            ],
            options={
                'unique_together': {('student', 'chapter')},
            },
        ),
    ]
