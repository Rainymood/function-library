#!/usr/bin/env python3

from urllib.parse import quote
from pathlib import Path
import json
import click

MARKDOWN_PREFIX = [
    "# {}",
    "- {}",
]

MARKDOWN_HEADER = """
# Function-library

![](./library-of-alexandria.png)

**This `README.md` is automatically generated.**

This repository contains some Jupyter notebooks that may or may not be useful to you.

Link to Trello board can be found [here](https://trello.com/b/mRx0Lpqv).

# Setup

To generate this readme file run `markdown_tree.py`

```bash
python markdown-tree.py > README.md
```

Run with

```bash
jupyter notebook
```

# Content
"""

MARKDOWN_FOOTER = """
# Acknowledgements

* [Chris Albon](https://chrisalbon.com/)
* [Markdown tree](https://pypi.org/project/markdown-tree/)
""".strip()


IGNORED_FILES = [".*", "README.md", "library-of-alexandria.png", "markdown_tree.py", "readme_auto.md"]


class MarkdownTreeGenerator(object):
    def __init__(self, dir, ignore, header, footer, emoji, prefixes):
        self.dir = dir
        self.ignore = ignore
        self.header = header
        self.footer = footer
        self.prefixes = prefixes
        self.emoji = emoji

    def generate(self):
        if self.header:
            yield self.header

        for line in self.walk(Path(self.dir), 0):
            yield line

        if self.footer:
            yield self.footer

    def walk(self, dir, level):
        for entry in sorted(self.iterdir(dir)):
            content = self.link(entry.name, quote(str(entry)))

            emoji = self.get_emoji(entry)
            if emoji:
                content = '{} {}'.format(emoji, content)

            line = self.markdown_prefix(level).format(content)

            if entry.is_file():
                yield line

            if entry.is_dir():
                if list(self.iterdir(entry)):
                    yield line
                    for line in self.walk(entry, level + 1):
                        yield line

    def iterdir(self, dir):
        for entry in sorted(dir.iterdir()):
            if self.check_against_filters(entry):
                yield entry

    def check_against_filters(self, entry):
        for i in self.ignore:
            if i.endswith('/'):
                if entry.is_dir() and entry.match(i):
                    return False
            else:
                if entry.match(i):
                    return False
        return True

    def markdown_prefix(self, i):
        if i < len(self.prefixes):
            return self.prefixes[i]
        return '  ' * (i - len(self.prefixes) + 1) + self.prefixes[-1]

    def link(self, text, href):
        return '[{}]({})'.format(text.replace("_", " ").replace("-", " "), href) # replace underscores/hypens with spaces

    def get_emoji(self, entry):
        if not self.emoji:
            return None
        if entry.is_file():
            return '📄'
        if entry.is_dir():
            return '📁'
        return None


@click.command()
@click.argument("directory", type=click.Path(exists=True), default=".")
@click.option("--ignore", type=str, default=','.join(IGNORED_FILES), help="Ignored files or dirs, comma separated, default=.*")
@click.option("--header", type=str, default=MARKDOWN_HEADER, help="Header")
@click.option("--footer", type=str, default=MARKDOWN_FOOTER, help="Footer")
@click.option("--emoji/--no-emoji", default=False, help="Enable file/folder emoji")
@click.option("--prefixes", type=str, default=','.join(MARKDOWN_PREFIX), help="Prefixes, default='## {},- {}', which means, top level entries are <h2> and the rest are <ul>")
@click.option("-c", "--config", type=click.Path(exists=False), default=".mdtreeconfig.json", help="Load all configs from a json file if exists, default=.mdtreeconfig.json")
@click.option("-o", "--output", type=click.Path(exists=False), default=None, help="Output filename, default is stardard output")
def generate_markdown_tree(directory, ignore="", header="", footer="", emoji=False, prefixes="", config="", output=None):
    directory = Path(directory)
    options = {}
    if config and (directory / config).exists():
        options = json.loads((directory / config).read_text())
    if 'ignore' not in options:
        options['ignore'] = ignore.split(',')
    if 'header' not in options:
        options['header'] = header
    if 'footer' not in options:
        options['footer'] = footer
    if 'emoji' not in options:
        options['emoji'] = emoji
    if 'prefixes' not in options:
        options['prefixes'] = prefixes.split(',')
    if 'output' not in options:
        options['output'] = output
    output = options.pop('output')

    gen = MarkdownTreeGenerator(dir=directory, **options)
    text = '\n'.join(gen.generate())

    if output:
        Path(output).write_text(text)
    else:
        print(text)


if __name__ == "__main__":
    generate_markdown_tree()
