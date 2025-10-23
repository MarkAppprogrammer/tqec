"""
Move Rotation
=============

Rotate the spatial boundary of a logical qubit.
"""

# sphinx-gallery: thumbnail _static/media/gallery/move_rotation.png

from tqec import Basis
from tqec.gallery import move_rotation

graph = move_rotation()
correlation_surfaces = graph.find_correlation_surfaces()
graph.view_as_html(pop_faces_at_directions=("-Y",), show_correlation_surface=correlation_surfaces[0])
