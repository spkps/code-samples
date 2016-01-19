from hilton.search import search


def find_directions(rooms, start, objects):

    found = []

    def completed(rooms, targets, found, room_id):
        obj = get_object(rooms, room_id)
        if obj in targets and obj not in found:
            found.append(obj)
        return len(found) == len(targets)

    start_id = get_id_by_name(rooms, start)
    graph = list(build_graph(rooms))
    path = search(
        graph, start_id,
        lambda room_id: completed(rooms, objects, found, room_id)
    )
    return path_to_directions(rooms, path)


def map_from_xml(tree):

    root = tree.getroot()

    if root.tag != 'map':
        raise ValueError('INVALID ROOT TAG: {}'.format(root.tag))

    for child in root:
        room = room_from_xml(child)
        yield room.pop('id'), room


def room_from_xml(element):

    DIRECTIONS = ['north', 'south', 'east', 'west']

    if element.tag != 'room':
        raise ValueError('INVALID ROOM TAG: {}'.format(element.tag))

    room = element.attrib.copy()
    obj = element.find('object')
    if not obj is None:
        obj = obj.get('name')
    room['object'] = obj

    neighbors = filter(lambda key: key in DIRECTIONS, element.attrib.keys())
    room['neighbors'] = {element.attrib[key]: key for key in neighbors}
    return room


def build_graph(rooms):
    if not isinstance(rooms, dict):
        raise ValueError
    for room, props in rooms.iteritems():
        for neighb in props.get('neighbors').keys():
            yield (room, neighb)


def path_to_directions(rooms, path):
    current = path[0]
    for n in path[1:]:
        yield current, get_direction(rooms, current, n)
        current = n
    else:
        yield current, ''


def get_id_by_name(rooms, name):
    if not isinstance(rooms, dict):
        raise ValueError
    ids = filter(lambda key: rooms[key].get('name') == name, rooms.keys())
    assert len(ids) == 1
    return ids[0]


def get_object(rooms, rid):
    if not isinstance(rooms, dict):
        raise ValueError
    return rooms[rid].get('object')


def get_direction(rooms, a, b):
    if not isinstance(rooms, dict):
        raise ValueError
    return rooms[a]['neighbors'].get(b)

