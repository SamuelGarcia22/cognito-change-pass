import subprocess
from data.letters import upper, lower
from data.numbers import numbers
from data.specialChars import specialChars

from utils.getRandomPass import getRandomPass

# AWS values
AWS_POOL = ""  # Place here the user pool id
AWS_REGION = "us-east-1"

# Set all available characters
allValues = upper + lower + numbers + specialChars

# User data to update
USERNAME = input("Escribe el correo a actualizar: \n")
PASSWORD = getRandomPass(allValues)


result = subprocess.run(
    [
        "aws",
        "cognito-idp",
        "admin-set-user-password",
        "--user-pool-id",
        AWS_POOL,
        "--username",
        USERNAME,
        "--password",
        PASSWORD,
        "--permanent",
    ]
)

print(
    f"\n\n --------- \n\n Usuario: \x1b[32m{USERNAME}\x1b[0m modificado con contraseña: \x1b[92m \x1b[1m{PASSWORD}\x1b[0m"
) if result.returncode == 0 else print(
    f"\n\n --------- \n\nFalló el comando: \x1b[31m code {result.returncode}\x1b[0m"
)
