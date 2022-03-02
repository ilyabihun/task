# Generated by Django 4.0.2 on 2022-03-02 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_ticket', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
    ]