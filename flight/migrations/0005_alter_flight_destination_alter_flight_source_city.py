# Generated by Django 4.0.4 on 2022-05-08 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_alter_flight_destination_alter_flight_source_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(choices=[('GIZ', 'Gizan'), ('DMM', 'Dammam'), ('AHB', 'Abha'), ('ABT', 'Al-Baha'), ('HOF', 'Alahsa'), ('RAE', 'Arar'), ('BHH', 'Bisha'), ('DMM', 'Dammam'), ('DWD', 'Dawadmi'), ('DHA', 'Dhahran'), ('ELQ', 'Gassim'), ('URY', 'Gurayat'), ('HBT', 'Hafr Albatin'), ('HAS', 'Hail'), ('GIZ', 'Jazan'), ('JED', 'Jeddah'), ('AJF', 'Jouf'), ('KMX', 'Khamis Mushait'), ('MJH', 'Majma'), ('EAM', 'Nejran'), ('AQI', 'Qaisumah'), ('RAH', 'Rafha'), ('RUH', 'Riyadh'), ('SHW', 'Sharurah'), ('SLF', 'Sulayel'), ('TUU', 'Tabuk'), ('TIF', 'Taif'), ('TUI', 'Turaif'), ('UZH', 'Unayzah'), ('WAE', 'Wadi Ad Dawasir'), ('EJH', 'Wedjh'), ('YNB', 'Yanbu'), ('ZUL', 'Zilfi')], max_length=50),
        ),
        migrations.AlterField(
            model_name='flight',
            name='source_city',
            field=models.CharField(choices=[('GIZ', 'Gizan'), ('DMM', 'Dammam'), ('AHB', 'Abha'), ('ABT', 'Al-Baha'), ('HOF', 'Alahsa'), ('RAE', 'Arar'), ('BHH', 'Bisha'), ('DMM', 'Dammam'), ('DWD', 'Dawadmi'), ('DHA', 'Dhahran'), ('ELQ', 'Gassim'), ('URY', 'Gurayat'), ('HBT', 'Hafr Albatin'), ('HAS', 'Hail'), ('GIZ', 'Jazan'), ('JED', 'Jeddah'), ('AJF', 'Jouf'), ('KMX', 'Khamis Mushait'), ('MJH', 'Majma'), ('EAM', 'Nejran'), ('AQI', 'Qaisumah'), ('RAH', 'Rafha'), ('RUH', 'Riyadh'), ('SHW', 'Sharurah'), ('SLF', 'Sulayel'), ('TUU', 'Tabuk'), ('TIF', 'Taif'), ('TUI', 'Turaif'), ('UZH', 'Unayzah'), ('WAE', 'Wadi Ad Dawasir'), ('EJH', 'Wedjh'), ('YNB', 'Yanbu'), ('ZUL', 'Zilfi')], max_length=50),
        ),
    ]