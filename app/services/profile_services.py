from typing import List
from app.models import Profile
from app.repositories import ProfileRepository

repository = ProfileRepository()

class ProfileService:
    """
    ProfileService class
    """
    def __init__(self):
        pass

    def save(self, profile: Profile) -> Profile:
        """
        Save a profile
        :param profile: Profile
        :return: Profile
        """
        repository.save(profile)
        return profile

    def update(self, profile: Profile, id: int) -> Profile:
        """
        Update a profile
        :param profile: Profile
        :param id: int
        :return: Profile
        """
        repository.update(profile, id)
        return profile

    def delete(self, profile: Profile) -> None:
        """
        Delete a profile
        :param profile: Profile
        """
        repository.delete(profile)

    def all(self) -> List[Profile]:
        """
        Get all profiles
        :return: List[Profile]
        """
        return repository.all()

    def find(self, id: int) -> Profile:
        """
        Get a profile by id
        :param id: int
        :return: Profile
        """
        return repository.find(id)
    