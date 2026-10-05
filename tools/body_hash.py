"""Affiche l'empreinte SHA-256 du corps (sans front matter) des pages markdown du wiki.

Sert à vérifier qu'une page poussée sur Wiki.js est identique au fichier local.
Usage : python3 tools/body_hash.py pages/fr/fleet/ships.md [autres fichiers...]
"""
import hashlib
import sys
from pathlib import Path

SEPARATOR = '\n---\n\n'


def body(path):
    text = Path(path).read_text(encoding='utf-8')
    if text.startswith('---\n') and SEPARATOR in text:
        return text.split(SEPARATOR, 1)[1]
    return text


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        content = body(arg)
        print(hashlib.sha256(content.encode('utf-8')).hexdigest(), len(content), arg)
