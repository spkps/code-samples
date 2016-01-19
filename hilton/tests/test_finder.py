import os
import unittest
import xml.etree.cElementTree as ET

from hilton.finder import *


TEST_DATA_PATH = 'tests/data'

class FinderTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = ET.parse(os.path.join(TEST_DATA_PATH, 'rooms.map'))
        self.room6 = ET.fromstring("""<room id="6" name="dining room" east="5" north="7">
     <object name="banjo"/>
</room>""")

    def getrooms(self):
        return dict(map_from_xml(self.tree))

    def test_a_room(self):
        room = room_from_xml(self.room6)
        self.assertEqual(room['id'], '6')
        self.assertEqual(room['name'], 'dining room')
        self.assertEqual(room['object'], 'banjo')
        self.assertItemsEqual(room['neighbors'], ['5', '7'])

    def test_rooms(self):
        rooms = self.getrooms()
        self.assertEqual(len(rooms), 7)

    def test_getobject(self):
        rooms = self.getrooms()
        self.assertEqual(get_object(rooms, '3'), 'rubber chicken')
        self.assertIsNone(get_object(rooms, '1'))

    def test_getdirection(self):
        rooms = self.getrooms()
        self.assertEqual(get_direction(rooms, '1', '2'), 'east')
        self.assertEqual(get_direction(rooms, '2', '1'), 'west')
        self.assertIsNone(get_direction(rooms, '3', '1'))

    def test_buildgraph(self):
        rooms = self.getrooms()
        graph =list(build_graph(rooms))
        self.assertEqual(len(graph), 12)

    def test_path2directs(self):
        rooms = self.getrooms()
        path = ['1', '2', '3', '5', '6']
        dirs = ['east', 'east', 'north', 'west', '']
        result = list(path_to_directions(rooms, path))
        self.assertSequenceEqual(result, zip(path, dirs))

    def test_findirects(self):
        rooms = self.getrooms()
        path = ['1', '2', '3']
        dirs = ['east', 'east', '']
        result = list(find_directions(rooms, 'arboretum', ['rubber chicken']))
        self.assertSequenceEqual(result, zip(path, dirs))

