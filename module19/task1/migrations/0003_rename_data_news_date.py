# Generated by Django 5.1.4 on 2024-12-16 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_news_alter_buyer_balance_alter_game_cost_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='data',
            new_name='date',
        ),
    ]