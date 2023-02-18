# Generated by Django 4.1.7 on 2023-02-17 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0009_alter_reservation_doctorid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='capacity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reserve.doctor'),
        ),
    ]
