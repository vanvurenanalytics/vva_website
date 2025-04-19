# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'VAN VUREN ANALYTICS'
copyright = '2025, Oscar van Vuren'
author = 'Oscar van Vuren'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'

html_sidebars = {
    "**": ["sbt-sidebar-nav.html", "navbar-logo.html"],
}

html_title = "VAN VUREN ANALYTICS"

html_logo = 'images/logo.svg'

html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

html_theme_options = {
    "toc_title": "",
    "home_page_in_toc": True
}


