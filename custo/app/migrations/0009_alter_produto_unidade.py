# Generated by Django 4.2.7 on 2024-05-23 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_produto_unidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='unidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.unidade'),
        ),
    ]
