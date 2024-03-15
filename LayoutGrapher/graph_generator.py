from pyvis.network import Network

key_spacing = 100
key_size = 20
edge_width = 5
color_offset = 50

def generate(result, keymap):
    net = Network(directed=False, height= '1200px')
    net.toggle_physics(False)
    net.set_edge_smooth('curvedCW')

    for key, value in keymap['left'].items() | keymap['right'].items():
        net.add_node(key, size = key_size, label = key, shape = "box",
                     x = value[0] * key_spacing, y = value[1] * key_spacing)
        
    limit = max(result.values())
    for key, value in result.items():
        edge_weight = value / limit
        net.add_edge(key[0], key[1], width= edge_weight * edge_width,
                     color='%s' % get_color(edge_weight))
    net.show('mygraph.html', notebook=False)

def get_color(weight):
    brightness = int(max(0, (1 - weight) * 255 - color_offset))
    return f'rgb({brightness},{brightness},{brightness})'

    