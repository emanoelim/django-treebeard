# Generated by Django 3.0.6 on 2021-10-20 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_auto_20211020_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresaal',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children_set', to='empresa.EmpresaAL'),
        ),
    ]