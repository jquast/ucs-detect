# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "ucs-detect"
copyright = "2023, Jeff Quast"
author = "Jeff Quast"
release = "1.0.7"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


# export DARK=1 for old, tired eyes!
import os
extensions = [
    "sphinxcontrib.jquery",
    "sphinx_datatables",
]
if os.environ.get('DARK'):
    extensions.append("sphinx_rtd_dark_mode")

# Configure DataTables: disable pagination, show all rows, no search
# Custom sorting is handled by custom_table_sort.js per table type
datatables_options = {
    "paging": False,     # Disable pagination completely
    "info": False,       # Hide "Showing X to Y of Z entries" text
    "searching": False,  # Disable search box
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
default_dark_mode = True


def score_ref_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Custom role that combines :ref: with score-* class styling.

    Usage: :sref:`link_text <target> score_number`
    Example: :sref:`100.0% <footvs16> 100`
    """
    from docutils import nodes
    from sphinx import addnodes
    from sphinx.util.nodes import split_explicit_title

    # Split off the score number (last space-separated part)
    parts = text.rsplit(' ', 1)
    if len(parts) != 2:
        msg = inliner.reporter.error(
            f'Score-ref role requires format "text <target> score", got "{text}"',
            line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]

    ref_text, score = parts

    # Parse the reference part (may have explicit title)
    has_explicit_title, title, target = split_explicit_title(ref_text)

    # Create a pending_xref node (Sphinx will resolve it)
    refnode = addnodes.pending_xref(
        ref_text,
        refdomain='std',
        reftype='ref',
        reftarget=target.lower(),
        refexplicit=has_explicit_title,
    )

    # Add the score class
    refnode['classes'].append(f'score-{score}')

    # Create the link text
    innernode = nodes.inline(title, title)
    refnode += innernode

    return [refnode], []


def setup(app):
    from docutils.parsers.rst import roles
    roles.register_local_role('sref', score_ref_role)

    app.add_css_file("my_theme.css")
    app.add_css_file("score-colors.css")
    app.add_js_file("custom_table_sort.js")

