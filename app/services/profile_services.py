from typing import List
from app.models import Profile
from app.repositories import ProfileRepository
from app import cache

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
        #TODO: Implementar auditoria
        repository.save(profile)
        cache.set(f'profile_{profile.id}', profile, timeout=15)
        return profile

    def update(self, profile: Profile, id: int) -> Profile:
        """
        Update a profile
        :param profile: Profile
        :param id: int
        :return: Profile
        """
        #TODO: Implementar auditoria
        repository.update(profile, id)
        cache.set(f'profile_{profile.id}', profile, timeout=15)
        return profile

    def delete(self, profile: Profile) -> None:
        """
        Delete a profile
        :param profile: Profile
        """
        #TODO: Implementar auditoria
        cache.delete(f'profile_{profile.id}')
        repository.delete(profile)

    def all(self) -> List[Profile]:
        """
        Get all profiles
        :return: List[Profile]
        """
        result = cache.get('profiles')
        if result is None:
            result = repository.all()
            cache.set('profiles', result, timeout=15)
        return result

    def find(self, id: int) -> Profile:
        """
        Get a profile by id
        :param id: int
        :return: Profile
        """
        result = cache.get(f'profile_{id}')
        if result is None:
            result = repository.find(id)
            cache.set(f'profile_{id}', result, timeout=15)
        
        return result 
    