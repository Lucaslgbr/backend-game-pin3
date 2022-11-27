from django.core.management import BaseCommand
from backend.game.models import *
import random

class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(50):
            direction = random.randint(1, 4)
            lines = random.randint(1, 8)
            moves_amount = random.randint(1, 8)
            Card.objects.get_or_create(direction=direction,lines=lines, moves_amount=moves_amount)
        print('ok')