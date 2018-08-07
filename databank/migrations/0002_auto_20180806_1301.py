# Generated by Django 2.1 on 2018-08-06 12:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('databank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_name', models.CharField(max_length=100)),
                ('identifier', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameModel(
            old_name='Results',
            new_name='Result',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='participant_visit_id',
            new_name='participant',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='participant_id',
        ),
        migrations.DeleteModel(
            name='Studies',
        ),
        migrations.AddField(
            model_name='participant',
            name='study',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='databank.Study'),
            preserve_default=False,
        ),
    ]