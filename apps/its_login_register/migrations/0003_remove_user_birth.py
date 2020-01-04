

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('its_login_register', '0002_user_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth',
        ),
    ]
