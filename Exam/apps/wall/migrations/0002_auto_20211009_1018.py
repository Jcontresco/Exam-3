# Generated by Django 2.2.4 on 2021-10-09 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=40)),
                ('created_at', models.DateField(auto_now=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('join', models.ManyToManyField(related_name='joined_user', to='user.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Travel',
        ),
    ]
