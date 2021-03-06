# Generated by Django 4.0.4 on 2022-05-13 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0009_alter_ticket_purchase_date_alter_ticket_qunatity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paid_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='flight.passenger'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='tax',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flight.payment'),
        ),
    ]
