import os
import unittest
from app import create_app, db
from app.models import Profile
from app.services import ProfileService

profile_service = ProfileService()

class ProfileTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.NAME = "Client"

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_profile_save(self):
        profile = Profile(name = self.NAME)
        profile_service.save(profile)
        self.assertGreaterEqual(profile.id, 1)
        self.assertEqual(profile.name, self.NAME)

    def test_profile_delete(self):
        profile = Profile(name = self.NAME)
        profile_service.save(profile)
        profile_service.delete(profile)
        self.assertIsNone(profile_service.find(profile))

    def test_profile_update(self):
        profile = Profile(name = self.NAME)
        profile_service.save(profile)
        profile.name = "Client Updated"
        profile_service.update(profile, profile.id)
        self.assertEqual(profile.name, "Client Updated")

    def test_profile_find(self):
        profile = Profile(name = self.NAME)
        profile_service.save(profile)
        profile = profile_service.find(profile.id)
        self.assertIsNotNone(profile)

    def test_all(self):
        profile = Profile(name=self.NAME)
        profile_service.save(profile)
        profiles = profile_service.all()
        self.assertGreaterEqual(len(profiles), 1)        