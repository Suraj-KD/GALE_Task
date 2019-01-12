from __future__ import with_statement
import logging
import urllib


from django.core.management.base import BaseCommand
from crawlapp.models import Crawl, Url
from crawlapp.worker import Worker

logging.basicConfig(level=logging.DEBUG)

class Command(BaseCommand):
    help = """"Launch Crawler worker process"""

    def handle(self, *args, **options):
        print("This is worker Process")
        worker = Worker()
        worker.process()

    def _get_lines(self, location):
        """Return a list of location  that can be path of file or url.
        If Path/Url is not found, return empty list"""

        try:
            if location.startswith(('http://', 'https://')):
                fp = urllib.urlopen(location)
                return [e.strip() for e in fp.read().split('\n')
                        if e and not e.isspace()]
            else:
                fp = open(location)
                return [e.strip() for e in fp.read().split('\n')
                        if e and not e.isspace()]
        except IOError:
            print("couldn't load %s " % location)
            return []
