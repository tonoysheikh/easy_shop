# Generated by Django 5.1.1 on 2024-09-15 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_services', '0005_exclude_service_include_service'),
        ('shongjog', '0002_registration_area_alter_registration_occupation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=500)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_product', to='all_services.serviceitem')),
            ],
        ),
    ]
