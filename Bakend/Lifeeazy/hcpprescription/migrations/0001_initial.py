# Generated by Django 4.0.3 on 2022-04-20 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('hcpapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPrescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DrugName', models.CharField(max_length=155)),
                ('Quantity', models.IntegerField()),
                ('Dosages', models.CharField(default=None, max_length=100)),
                ('Route', models.CharField(max_length=155)),
                ('Frequency', models.IntegerField()),
                ('Instructions', models.TextField(default=None)),
                ('NextFollowUp_Date', models.DateField()),
                ('HcpId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hcpprescription', to='hcpapi.hcpmodel')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserPrescription', to='user.usermodel')),
            ],
            options={
                'db_table': 'Prescriptions',
            },
        ),
        migrations.CreateModel(
            name='UserlabRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LabInvestigation', models.CharField(default=None, max_length=255)),
                ('ImageInvestigation', models.CharField(default=None, max_length=255)),
                ('Others', models.CharField(default=None, max_length=255)),
                ('HcpId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LabDetails', to='hcpapi.hcpmodel')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserlabDetails', to='user.usermodel')),
            ],
            options={
                'db_table': 'labRecords',
            },
        ),
    ]
