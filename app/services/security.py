from werkzeug.security import generate_password_hash, check_password_hash

class Security:
    """
    Clase que se encarga de la seguridad de la aplicación.
    Aplicamos el Principio de Responsabilidad Única (Ver anteriores commits)
    """
    @staticmethod
    def generate_password(text: str ) -> str:
        return generate_password_hash(text)
    
    @staticmethod
    def check_password( text1:str, text2: str) -> bool:
        return check_password_hash(text1, text2)