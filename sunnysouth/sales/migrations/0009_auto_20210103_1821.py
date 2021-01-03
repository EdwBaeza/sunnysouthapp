# Generated by Django 3.1 on 2021-01-03 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_auto_20201018_0914'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductCategory',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_category',
            new_name='category',
        ),
    ]