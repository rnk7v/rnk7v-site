#!/usr/bin/env python3
"""Render the static portfolio; refresh release metadata only with authorized access at build time."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
API = 'https://api.github.com/repos/rnk7v/actstride/releases/latest'


def render(source, release=None):
    if release is None:
        return source
    tag = release.get('tag_name', '')
    if not re.fullmatch(r'v[0-9]+\.[0-9]+\.[0-9]+', tag) or release.get('draft') is not False or release.get('prerelease') is not False:
        raise ValueError('Expected a published stable semantic release')
    published = dt.datetime.fromisoformat(release['published_at'].replace('Z', '+00:00'))
    date = f'{published.strftime("%b")} {published.day}, {published.year}'
    # Only explicit metadata fields change. Historical captions stay pinned.
    replacements = [
        (r'(data-release-version>)v[0-9]+\.[0-9]+\.[0-9]+(<)', tag, 1),
        (r'(data-release-date>)[^<]+(<)', date, 1),
    ]
    for pattern, value, expected in replacements:
        source, n = re.subn(pattern, lambda m: m[1] + value + m[2], source)
        if n != expected:
            raise ValueError(f'Unexpected metadata field count: {n} (expected {expected})')
    return source


def fetch():
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'rnk7v-portfolio-build', 'X-GitHub-Api-Version': '2022-11-28'}
    if os.environ.get('GH_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
    with urllib.request.urlopen(urllib.request.Request(API, headers=headers), timeout=25) as response:
        return json.load(response)


def main():
    p = argparse.ArgumentParser()
    group = p.add_mutually_exclusive_group()
    group.add_argument('--refresh', action='store_true', help='Fetch latest stable Actstride release with authorized access; fail closed on error')
    group.add_argument('--release-json', type=Path, help='Offline test fixture')
    p.add_argument('--output', type=Path, default=ROOT / 'dist/index.html')
    args = p.parse_args()
    release = fetch() if args.refresh else json.loads(args.release_json.read_text()) if args.release_json else None
    html = render((ROOT / 'index.html').read_text(encoding='utf-8'), release)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding='utf-8')
    print('Rendered', args.output, 'release:', release['tag_name'] if release else 'bundled fallback')


if __name__ == '__main__':
    main()
