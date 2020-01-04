

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('its_login_register', '0004_user_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth',
            field=models.CharField(max_length=10),
        ),
    ]
