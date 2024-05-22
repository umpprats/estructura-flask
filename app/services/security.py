from abc import ABC, abstractmethod
from passlib.hash import pbkdf2_sha256
from werkzeug.security import generate_password_hash, check_password_hash

class AbstractSecurity(ABC):
    """
    Clase abstracta que define los métodos que todas las clases de seguridad deben implementar.
    """

    @abstractmethod
    def generate_password(self, password: str) -> str:
        pass

    @abstractmethod
    def check_password(self, hashed_password: str, plain_password: str) -> bool:
        pass

class WerkzeugSecurity(AbstractSecurity):
    """
    Clase que implementa la seguridad utilizando la librería Werkzeug.
    """
    def generate_password(self, password: str) -> str:
        return generate_password_hash(password)

    def check_password(self, hashed_password: str, plain_password: str) -> bool:
        return check_password_hash(hashed_password, plain_password)

class PassLibSecurity(AbstractSecurity):
    """
    Clase que implementa la seguridad utilizando la librería PassLib.
    """
    def generate_password(self, password: str) -> str:
        return pbkdf2_sha256.hash(password)

    def check_password(self, hashed_password: str, plain_password: str) -> bool:
        return pbkdf2_sha256.verify(plain_password, hashed_password)

class SecurityManager:
    """
    Clase que se encarga de la seguridad de la aplicación.
    Aplicamos el Principio de Responsabilidad Única (Ver anteriores commits)
    """
    def __init__(self, security: AbstractSecurity):
        self.__security = security
    
    def generate_password(self, password: str ) -> str:
        """
        Método que genera un hash de la contraseña.
        password: str - Contraseña en texto plano.
        return: str
        """
        return self.__security.generate_password(password)
    
    def check_password(self, hashed_password: str, plain_password: str) -> bool:
        """
        Método que verifica si la contraseña en texto plano coincide con el hash.
        hashed_password: str - Contraseña en hash.
        plain_password: str - Contraseña en texto plano.
        return: bool
        """
        return self.__security.check_password(hashed_password, plain_password)
    