from passlib.context import CryptContext

password_crypter = CryptContext(schemes=["pbkdf2_sha256"])