#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

"""
Script para detectar el sistema operativo de un host remoto basado en el valor del TTL (Time to Live) obtenido mediante un comando `ping`.
Este script es útil en plataformas como Hack The Box (HTB) para identificar si un host está ejecutando Linux o Windows.

Uso:
    python3 whichSystem.py <Direccion Ip>
"""

from re import findall
from subprocess import PIPE, Popen
from sys import argv, exit, stderr, stdout
from typing import List, Optional, Union

if len(argv) != 2:
    print(f"\n [!] Uso: python3 {argv[0]} <Direccion Ip>\n", end="\n", file=stderr)
    exit(1)

def get_ttl(ip_address: str) -> str:
    """
    Ejecuta un comando `ping` al host especificado y extrae el valor del TTL de la respuesta.

    Parámetros:
        ip_address (str): Dirección IP del host remoto.

    Retorna:
        str: Valor del TTL obtenido del comando `ping`.

    Excepciones:
        Exit(1): Finaliza el script si no se puede obtener el TTL.
    """
    proc: Popen = Popen(
        ["/usr/bin/ping -c 1 %s" % ip_address, ""],
        stdout=PIPE,
        shell=True
    )
    out: Union[Optional[bytes], str, List[str]] = None
    err: None = None
    (out, err) = proc.communicate()

    if out is not None:
        out = str(out)
        out = out.split()

        out = out[11].encode("utf-8").decode("utf-8")
        ttl_value: Optional[str] = findall(pattern=r"\d{1,3}", string=out)[0]

        match ttl_value:
            case ttl_value if isinstance(ttl_value, str):
                return ttl_value
            case _:
                pass
    exit(1)
    return "[!] Error"

def get_os(ttl: Union[str, int]) -> str:
    """
    Determina el sistema operativo basado en el valor del TTL.

    Parámetros:
        ttl (Union[str, int]): Valor del TTL como cadena o entero.

    Retorna:
        str: Nombre del sistema operativo (Linux, Windows o Not Found).
    """
    ttl = int(ttl)
    if ttl >= 0 and ttl <= 64:
        return "Linux"
    elif ttl >= 65 and ttl <= 128:
        return "Windows"
    else:
        return "Not Found"

if __name__ == "__main__":
    """
    Punto de entrada del script. Obtiene la dirección IP de la entrada del usuario,
    recupera el TTL y determina el sistema operativo basado en el TTL.
    """
    ip_address: str = argv[1]
    ttl: str = get_ttl(ip_address=ip_address)
    os_name: str = get_os(ttl=ttl)
    print("\n %s (ttl -> %s): %s" % (ip_address, ttl, os_name), end="\n", file=stdout)
    exit(0)

