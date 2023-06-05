import base64
import json
import time
from datetime import datetime
from jose import jwe


# Metodos para descifrar el JWT-E
def is_jwe(token):
    try:
        """Verifica si la cadena pasada es un JWE válido o no."""
        segments = token.split(".")
        if len(segments) != 5:
            return False

        header = base64.b64decode(segments[0] + '==')
        data = json.loads(header.decode('utf-8'))
        if "alg" in data and "enc" in data:
            return True

        return False

    except Exception as e:
        print(f"[KeyboardReader] (is_jwe): Error: {e}")
        return False


def decrypt_jwt_token(jwt_token, key):
    try:
        """Verifica si la cadena recibida es un JWE válido"""
        if is_jwe(jwt_token):

            """Convierte una cadena hexadecimal a un objeto bytes y codifica un objeto bytes en base64 y lo devuelve como una cadena de texto."""
            key = base64.b64decode(base64.b64encode(bytes.fromhex(key)).decode('utf-8'))

            """Descifra el token JWT y devuelve los datos en formato JSON."""
            data = json.loads(jwe.decrypt(jwt_token, key).decode())

            """Verifica si el token JWT ha expirado."""
            # Verifique que el token JWT y
            fecha_expiracion = data.get("exp")
            fecha_actual = datetime.now().timestamp()

            if fecha_expiracion < fecha_actual:
                print(f"[KeyboardReader] (decrypt_jwt_token): El token ha expirado:")
                print(f"{datetime.fromtimestamp(fecha_expiracion)}): {data})")
                return -2
            else:
                print(f"[KeyboardReader] (decrypt_jwt_token): El token es valido:")
                print(f"{data}")
                return data.get("sub")
        else:
            print(f"[KeyboardReader] (decrypt_jwt_token): La cadena recibida no es un JWE válido: {jwt_token}")
            return -3

    except Exception as e:
        print(f"[KeyboardReader] (decrypt_jwt_token) - Error : {e}")
        return -3


# Variable para el token JWT
JWT_TOKEN = ".....YOUR____TOKEN........"
# Constante para la clave en formato hexadecimal
HEX_KEY = ".....YOUR____KEY........"
data = decrypt_jwt_token(JWT_TOKEN, HEX_KEY)

