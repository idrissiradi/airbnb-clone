from django.core.management.base import BaseCommand

from rooms.models import Facility


class Command(BaseCommand):
    help = "Seeds facilities"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for facility in facilities:
            Facility.objects.create(name=facility)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created!"))
