from graph_layout import _create_layout, SVG, draw
from StringIO import StringIO

def complete_graph(n):
    vertices = range(1, n+1)
    return {
        "vertices": vertices,
        "edges": [(i,j) for i in vertices for j in vertices if i < j]
    }

def test_create_layout_basic():
    G = complete_graph(4)
    layout = _create_layout(G)
    assert layout.width == 400
    assert layout.height == 400
    assert len(layout.locations) == 4

def test_svg():
    svg = SVG(width=100, height=100)
    svg.add_vertex((40, 40))
    svg.add_vertex((40, 60))
    svg.add_edge((40, 60), (40, 40))
    edge = '<line x1="40" y1="60" x2="40" y2="40" class="edge"/>'
    v1 = '<circle cx="40" cy="40"'
    v2 = '<circle cx="40" cy="60"'
    string_repr = str(svg)
    assert edge in string_repr 
    assert v1 in string_repr
    assert v2 in string_repr


def test_draw():
    G = complete_graph(4)
    buf = StringIO()
    draw(G, buf)
