from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        User = get_user_model()
        # Delete all data in order: Activity, Leaderboard, Workout, Team, then User
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()
        octo_models.Team.objects.all().delete()
        # Clear user collection directly using Djongo's raw MongoDB access
        User.mongo_collection().delete_many({})

        # Create Teams

        marvel = octo_models.Team.objects.create(name='Team Marvel')
        dc = octo_models.Team.objects.create(name='Team DC')

        # Create Users (assign team as string)
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team='Team Marvel')
        captain = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team='Team Marvel')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team='Team DC')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team='Team DC')


        # Create Activities (user as username string)
        octo_models.Activity.objects.create(user='ironman', type='run', duration=30, calories=300)
        octo_models.Activity.objects.create(user='batman', type='cycle', duration=45, calories=400)

        # Create Workouts
        octo_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        octo_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create Leaderboard (user as username string)
        octo_models.Leaderboard.objects.create(user='ironman', score=1000)
        octo_models.Leaderboard.objects.create(user='batman', score=950)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
