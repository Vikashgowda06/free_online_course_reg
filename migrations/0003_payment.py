# Generated by Django 4.2.2 on 2023-06-30 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships2023', '0002_remove_registration_usn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('card', 'Card Payment'), ('upi', 'UPI Payment')], max_length=10)),
                ('card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('cardholder_name', models.CharField(blank=True, max_length=255, null=True)),
                ('expiry_date', models.CharField(blank=True, max_length=10, null=True)),
                ('cvv', models.CharField(blank=True, max_length=4, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
