# Generated by Django 5.1.2 on 2024-11-13 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(max_length=100)),
                ('Customer_Age', models.IntegerField()),
                ('Loan_Amount', models.IntegerField()),
                ('Loan_Type', models.CharField(max_length=100)),
                ('Loan_Duration', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Loan',
        ),
    ]
