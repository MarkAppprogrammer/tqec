"""
Memory
======

Demonstrates a logical memory experiment.
"""

# sphinx-gallery: thumbnail _static/media/gallery/memory.png

from tqec import Basis
from tqec.gallery import memory

graph = memory(Basis.Z)
correlation_surfaces = graph.find_correlation_surfaces()
# show one correlation surface as in the notebook
graph.view_as_html(pop_faces_at_directions=("-Y",), show_correlation_surface=correlation_surfaces[0])
