# Generated by Django 5.1.1 on 2024-09-10 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='all_service',
        ),
        migrations.CreateModel(
            name='ServiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_items', to='all_services.services')),
            ],
        ),
    ]
