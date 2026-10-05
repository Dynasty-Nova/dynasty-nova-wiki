"""Applique une liste de remplacements aux pages markdown locales (corps uniquement).

Format du fichier d'éditions (JSON) : {"fr/universe/planets": [["ancien", "nouveau"], ...], ...}
Chaque texte « ancien » doit exister dans la page, sinon rien n'est écrit pour cette page.
La même liste est ensuite rejouée sur le wiki, puis les empreintes sont comparées (tools/body_hash.py).
Usage : python3 tools/apply_edits.py edits.json
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / 'pages'
SEPARATOR = '\n---\n\n'


def main(edits_path):
    edits = json.loads(Path(edits_path).read_text(encoding='utf-8'))
    ok = True
    for key, pairs in edits.items():
        path = ROOT / f'{key}.md'
        head, body = path.read_text(encoding='utf-8').split(SEPARATOR, 1)
        for old, new in pairs:
            if old not in body:
                print(f'MANQUANT {key} : {old[:60]!r}')
                ok = False
                break
            body = body.replace(old, new)
        else:
            path.write_text(head + SEPARATOR + body, encoding='utf-8')
            print(f'ok {key} {len(body)}')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main(sys.argv[1])
