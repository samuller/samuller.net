"""Pelican plugin: read quote TSV files and inject them into template context."""
import csv
import os
from pelican import signals


def inject_quotes(generator):
    data_dir = os.path.join(
        os.path.dirname(os.path.dirname(generator.settings['PATH'])),
        '_data', 'quotes',
    )
    if not os.path.isdir(data_dir):
        return
    quotes = {}
    for fname in sorted(os.listdir(data_dir)):
        if fname.endswith('.tsv'):
            category = fname[:-4]
            with open(os.path.join(data_dir, fname), newline='', encoding='utf-8') as f:
                quotes[category] = list(csv.DictReader(f, delimiter='\t'))
    generator.context['quotes_data'] = quotes


def register():
    signals.generator_init.connect(inject_quotes)
