import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from django.conf import settings
from django.core.management.base import (
    BaseCommand,
    CommandError
)


class Command(BaseCommand):
    """
    Management command to create new databse
    """
    help = 'Create new database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            host = settings.DATABASES['default']['HOST']
            name = settings.DATABASES['default']['NAME']
            user = settings.DATABASES['default']['USER']
            password = settings.DATABASES['default']['PASSWORD']

            con = psycopg2.connect(dbname='postgres', user=user,
                                   host=host, password=password)

            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = con.cursor()
            cur.execute("CREATE DATABASE {0}  ;".format(name))
            print("Database {0} created successfully".format(name))

        except Exception as e:
            raise CommandError(e)
