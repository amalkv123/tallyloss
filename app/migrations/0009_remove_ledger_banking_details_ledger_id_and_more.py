# Generated by Django 4.0.5 on 2022-09-03 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_ledger_ledger_cr_db'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger_banking_details',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_mailing_address',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_rounding',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_satutory',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_sundry',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_tax',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_tax_register',
            name='ledger_id',
        ),
        migrations.DeleteModel(
            name='Ledger',
        ),
        migrations.DeleteModel(
            name='Ledger_Banking_Details',
        ),
        migrations.DeleteModel(
            name='Ledger_Mailing_Address',
        ),
        migrations.DeleteModel(
            name='Ledger_Rounding',
        ),
        migrations.DeleteModel(
            name='Ledger_Satutory',
        ),
        migrations.DeleteModel(
            name='Ledger_sundry',
        ),
        migrations.DeleteModel(
            name='ledger_tax',
        ),
        migrations.DeleteModel(
            name='Ledger_Tax_Register',
        ),
    ]
