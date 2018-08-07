# Generated by Django 2.1 on 2018-08-03 08:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_number', models.CharField(max_length=10)),
                ('visit_date', models.DateTimeField(verbose_name='date of visit')),
                ('raw_neutrophils', models.CharField(max_length=3)),
                ('raw_macrophages', models.CharField(max_length=3)),
                ('raw_eosinophils', models.CharField(max_length=3)),
                ('raw_epithelium', models.CharField(max_length=3)),
                ('raw_lymphocytes', models.CharField(max_length=3)),
                ('participant_visit_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='databank.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='Studies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_name', models.TextField()),
                ('study_id', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='participant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='databank.Studies'),
        ),
    ]