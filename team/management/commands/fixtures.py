from django.core import management
from django.core.management.commands import loaddata
from django.core.management.base import (
    BaseCommand,
    CommandError
)


class Command(BaseCommand):
    """
    Management command to apply provided fixtures to database
    """
    help = 'Apply fixtures to database'

    def add_arguments(self, parser):
        parser.add_argument('names', nargs='+',
                            help='Comma seperated fixture names',)

    def handle(self, *args, **options):
        try:
            fixtures = options['names']
            verbosity = options['verbosity']

            for nm in fixtures:
                management.call_command(
                    loaddata.Command(), nm,
                    verbosity=verbosity)

        except Exception as e:
            raise CommandError(e)
