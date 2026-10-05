"""Découpe un export JSON du wiki (wiki-export.json) en un fichier markdown par page.

Chaque fichier reçoit un front matter YAML avec l'identifiant de la page dans Wiki.js.
Usage : python3 tools/export_to_md.py chemin/vers/wiki-export.json
Les fichiers sont écrits dans wiki/pages/<langue>/<chemin>.md (les fichiers existants sont remplacés).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / 'pages'


def front_matter(page, source):
    fields = {
        'wiki_id': page['id'],
        'locale': page['locale'],
        'path': page['path'],
        'url': f"{source}/{page['locale']}/{page['path']}",
        'title': page['title'],
        'description': page['description'],
        'tags': page['tags'],
        'published': page['isPublished'],
        'created': page['createdAt'],
        'updated': page['updatedAt'],
    }
    lines = ['---']
    for key, value in fields.items():
        lines.append(f'{key}: {json.dumps(value, ensure_ascii=False)}')
    lines.append('---')
    return '\n'.join(lines) + '\n\n'


def main(export_path):
    data = json.loads(Path(export_path).read_text(encoding='utf-8'))
    source = data.get('source', 'https://wiki.dynastynova.com')
    written = 0
    for page in data['pages']:
        target = ROOT / page['locale'] / f"{page['path']}.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(front_matter(page, source) + page['content'], encoding='utf-8')
        written += 1
    print(f"{written} pages écrites dans {ROOT} (export du {data.get('exportedAt', '?')})")


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'wiki-export.json')
