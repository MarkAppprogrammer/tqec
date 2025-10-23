"""
Steane Encoding
===============

Demonstrates the Steane encoding routine used to prepare logical magic states.
"""

# sphinx-gallery: thumbnail _static/media/gallery/steane_encoding.png

from tqec.gallery.steane_encoding import steane_encoding

graph = steane_encoding()
correlation_surfaces = graph.find_correlation_surfaces()
# show one correlation surface
graph.view_as_html(pop_faces_at_directions=("-Y",), show_correlation_surface=correlation_surfaces[0])
