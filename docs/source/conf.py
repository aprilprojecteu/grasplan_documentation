# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Grasplan'
copyright = '2023, Oscar Lima'
author = 'Oscar Lima'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_logo = 'images/sakura_logo.png'

html_theme = 'alabaster'
# This line tells Sphinx where to find static files
html_static_path = ['_static']

# This line adds your custom CSS file
html_css_files = [
    'custom.css',
]

html_js_files = ['script.js']

html_theme_options = {
    'pre_bg' : '#a9d3ee',
    'warn_bg': '#ffdeea',
    'head_font_family': 'Playfair Display'
}

html_extra_path = ['_files/google8518cc15a82bda49.html', 'custom.html']

# -- Options for EPUB output
epub_show_urls = 'footnote'
