# Generated by Django 4.0.4 on 2022-05-04 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('model', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'aircraft',
                'verbose_name_plural': 'aircrafts',
            },
        ),
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('E', 'Economy'), ('B', 'Business'), ('F', 'First')], max_length=30)),
                ('total_seats', models.IntegerField()),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': 'class info',
                'verbose_name_plural': 'classes info',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('delay', models.DurationField()),
                ('destination', models.CharField(max_length=50)),
                ('source_city', models.CharField(max_length=50)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('pssn', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=50)),
                ('special_need', models.BooleanField()),
            ],
            options={
                'verbose_name': 'passenger',
                'verbose_name_plural': 'passengers',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.FloatField()),
            ],
            options={
                'verbose_name': 'payment method',
                'verbose_name_plural': 'payment methods',
            },
        ),
        migrations.CreateModel(
            name='ApplePayMethod',
            fields=[
                ('apple_id', models.IntegerField()),
                ('device', models.CharField(max_length=50)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='flight.payment')),
            ],
        ),
        migrations.CreateModel(
            name='CashMethod',
            fields=[
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='flight.payment')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCardMethod',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('expire_date', models.DateField()),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='flight.payment')),
            ],
        ),
        migrations.CreateModel(
            name='PaypalMethod',
            fields=[
                ('account_id', models.CharField(max_length=100)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='flight.payment')),
            ],
        ),
        migrations.CreateModel(
            name='WaitingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_type', models.CharField(choices=[('E', 'Economy'), ('B', 'Business'), ('F', 'First')], max_length=30)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.passenger')),
            ],
            options={
                'verbose_name': 'waiting list',
                'verbose_name_plural': 'waiting lists',
            },
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_flight', models.DateField()),
                ('total_seats', models.IntegerField()),
                ('last_maintenance', models.DateField()),
                ('next_maintenance', models.DateField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.aircraft')),
            ],
            options={
                'verbose_name': 'plane',
                'verbose_name_plural': 'planes',
            },
        ),
        migrations.CreateModel(
            name='HasClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.aircraft')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.classinfo')),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='plane',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.plane'),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='class_info',
            field=models.ManyToManyField(through='flight.HasClass', to='flight.classinfo'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_in', models.BooleanField(default=False)),
                ('seat_number', models.CharField(max_length=3)),
                ('gate', models.CharField(max_length=50)),
                ('class_type', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('volume', models.FloatField()),
                ('qunatity', models.IntegerField()),
                ('successful', models.BooleanField()),
                ('purchase_date', models.DateField(auto_now_add=True)),
                ('cost', models.FloatField()),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.passenger')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.payment')),
            ],
            options={
                'verbose_name': 'ticket',
                'verbose_name_plural': 'tickets',
                'unique_together': {('seat_number', 'flight')},
            },
        ),
    ]