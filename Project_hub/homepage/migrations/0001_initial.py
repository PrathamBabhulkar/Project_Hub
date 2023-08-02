# Generated by Django 2.1 on 2023-07-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('client_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=200)),
                ('client_gender', models.CharField(max_length=200)),
                ('client_mobile', models.CharField(max_length=200)),
                ('client_email', models.CharField(max_length=200)),
                ('client_about', models.CharField(max_length=200)),
                ('client_projectname', models.CharField(max_length=200)),
                ('client_img', models.ImageField(upload_to='')),
                ('client_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='msgbox',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('msg_name', models.CharField(max_length=200)),
                ('msg_email', models.CharField(max_length=200)),
                ('msg_mobile', models.CharField(max_length=200)),
                ('msg_service', models.CharField(max_length=200)),
                ('msg_message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_username', models.CharField(max_length=200)),
                ('project_id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=200)),
                ('project_clientname', models.CharField(max_length=200)),
                ('project_technology', models.CharField(max_length=200)),
                ('project_team', models.CharField(max_length=200)),
                ('project_info', models.CharField(max_length=500)),
                ('project_type', models.CharField(max_length=100)),
                ('project_image', models.ImageField(upload_to='')),
                ('project_link', models.CharField(max_length=200)),
                ('project_startdate', models.CharField(max_length=100)),
                ('project_enddate', models.CharField(max_length=200)),
                ('project_validity', models.CharField(max_length=200)),
                ('project_dcost', models.IntegerField(default=1)),
                ('project_rcost', models.IntegerField(default=1)),
            ],
        ),
    ]