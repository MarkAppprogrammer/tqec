"""
CNOT
====

This example shows the construction and visualization of the logical CNOT gate.

Notes
-----
This example is converted from the original Jupyter notebook. Run the example locally
via the documentation build; sphinx-gallery will produce a downloadable notebook if
requested.
"""

# sphinx-gallery: thumbnail _static/media/gallery/cnot.png

# Import the example helper from the project
from tqec.gallery import cnot

# Construct the graph and display an interactive HTML view when run in the docs
graph = cnot()
# The original notebook called graph.view_as_html() to show an interactive view.
# Sphinx-gallery will execute the script and capture outputs; the view_as_html
# call is left here so local interactive runs behave similarly.
graph.view_as_html()
