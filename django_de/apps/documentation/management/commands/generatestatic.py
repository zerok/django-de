from django.core.management.base import NoArgsCommand

from django_de.apps.documentation.utils import get_absolute_document_urls
from django_de.apps.documentation.generator import quick_publish, StaticGeneratorException

class Command(NoArgsCommand):
    help = 'Used to autogenerate static files from SVN repository.'

    def handle_noargs(self, **options):
        for path in get_absolute_document_urls() + ('/', '/documentation/'):
            try:
                quick_publish(path)
            except StaticGeneratorException:
                pass
