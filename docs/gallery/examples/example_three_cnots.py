"""
Three CNOTs
===========

Construct and visualize three compressed logical CNOT gates.
"""

# sphinx-gallery: thumbnail _static/media/gallery/three_cnots.png

from tqec.gallery import three_cnots

graph = three_cnots()
correlation_surfaces = graph.find_correlation_surfaces()
# show the first correlation surface
graph.view_as_html(pop_faces_at_directions=("-Y",), show_correlation_surface=correlation_surfaces[0])
