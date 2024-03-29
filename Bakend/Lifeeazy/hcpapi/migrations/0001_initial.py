# Generated by Django 4.0.3 on 2022-04-20 05:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HcpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='firstname must string and should not be less than 3 and greater than 12', regex='^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$')])),
                ('Lastname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='lastname must string and should not be less than 3 and greater than 12', regex='^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$')])),
                ('Email', models.EmailField(max_length=50)),
                ('Username', models.CharField(max_length=60, unique=True)),
                ('Password', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='password must contain 8 letters and a captail letter and a special character ', regex='^.*(?=.{8,})(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')])),
                ('MobileNumber', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('DeviceToken', models.CharField(default=None, max_length=255)),
            ],
            options={
                'db_table': 'HCP_Data',
            },
        ),
        migrations.CreateModel(
            name='HcpEducational',
            fields=[
                ('Degree', models.CharField(max_length=255)),
                ('CollegeUniversity', models.CharField(max_length=255)),
                ('YearOfEducation', models.IntegerField()),
                ('EducationalLocation', models.CharField(max_length=255)),
                ('HcpId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Education', serialize=False, to='hcpapi.hcpmodel')),
            ],
            options={
                'db_table': 'Hcp_Educational',
            },
        ),
        migrations.CreateModel(
            name='HcpProfessional',
            fields=[
                ('ProfessionalId', models.CharField(max_length=255)),
                ('ProfessionalExperienceInYears', models.IntegerField()),
                ('CurrentStatus', models.BooleanField()),
                ('MciNumber', models.IntegerField()),
                ('MciStateCouncil', models.CharField(max_length=50)),
                ('Specialization', models.CharField(max_length=250)),
                ('AreaFocusOn', models.CharField(max_length=50)),
                ('PatientsHandledPerDay', models.IntegerField()),
                ('PatientsHandledPerSlot', models.IntegerField()),
                ('AppointmentType', multiselectfield.db.fields.MultiSelectField(choices=[('Teleconsultation', 'Teleconsultation'), ('Home', 'Home'), ('In-clinic', 'In-clinic')], max_length=200)),
                ('Signature', models.TextField(default=None, null=True)),
                ('HcpId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Professional', serialize=False, to='hcpapi.hcpmodel')),
            ],
            options={
                'db_table': 'Hcp_Professional',
            },
        ),
        migrations.CreateModel(
            name='HcpProfile',
            fields=[
                ('ProfilePicture', models.TextField()),
                ('State', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=500)),
                ('Pincode', models.CharField(max_length=255)),
                ('Timezone', models.CharField(max_length=255)),
                ('HcpId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Profile', serialize=False, to='hcpapi.hcpmodel')),
            ],
            options={
                'db_table': 'HCP_Profile',
            },
        ),
        migrations.CreateModel(
            name='HcpOtpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('verified', models.BooleanField(default=False)),
                ('HcpId', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='hcpotp', to='hcpapi.hcpmodel')),
            ],
            options={
                'db_table': 'HcpOtpTable',
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClinicName', models.CharField(max_length=250)),
                ('Address', models.CharField(max_length=200)),
                ('FromDate', models.DateField()),
                ('ToDate', models.DateField()),
                ('FromTime', models.TimeField()),
                ('ToTime', models.TimeField()),
                ('Fee', models.IntegerField()),
                ('HcpId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Clinicdetails', to='hcpapi.hcpmodel')),
            ],
            options={
                'db_table': 'Hcp_Clinic',
            },
        ),
        migrations.CreateModel(
            name='Addbankdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BankAccountNumber', models.CharField(max_length=200)),
                ('BankName', models.CharField(max_length=200)),
                ('IFSCCode', models.CharField(max_length=200)),
                ('BankBranch', models.CharField(max_length=50)),
                ('AccountNumber', models.CharField(max_length=200)),
                ('PanNumber', models.CharField(max_length=200)),
                ('UploadPancard', models.TextField()),
                ('UploadDocuments', models.TextField()),
                ('Remarks', models.CharField(max_length=200)),
                ('HcpId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hcpbankdetails', to='hcpapi.hcpmodel')),
            ],
            options={
                'db_table': 'Hcp_Addbankdetails',
            },
        ),
    ]
