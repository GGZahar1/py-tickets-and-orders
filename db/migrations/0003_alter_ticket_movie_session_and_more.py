# Generated by Django 4.0.2 on 2025-04-12 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_alter_ticket_movie_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='movie_session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='db.moviesession'),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name='movie',
            index=models.Index(fields=['title'], name='db_movie_title_5d0841_idx'),
        ),
    ]
