import sys
import os
import argparse
import xml.etree.cElementTree as ET

from hilton.finder import *


def read_goals(goalpath):
    with open(goalpath, 'r') as f:
        data = f.read().split(os.linesep)
        data = filter(lambda l: l, data)  # filter empty strings
        return data[0], data[1:]


def output(text):
    sys.stdout.write(text+'\n')


def valid_path(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError("Invalid path: {}".format(path))
    return path


def get_args():

    parser = argparse.ArgumentParser(description="Test task")
    parser.add_argument('-m', '--map', type=valid_path, required=True,
                        help='the path to the file with a map')
    parser.add_argument('-g', '--goal', type=valid_path, required=True,
                        help='the path to the file with goals')
    return parser.parse_args()


def main():

    args = get_args()

    start, targets = read_goals(args.goal)
    tree = ET.parse(args.map)
    rooms = dict(map_from_xml(tree))

    directs = find_directions(rooms, start, targets)

    objcnt = 0
    for room, wall in directs:
        obj = get_object(rooms, room)
        if not obj is None:
            outobj = obj
            if obj in targets:
                objcnt += 1
                outobj += " ({}/{})".format(objcnt, len(targets))
            output(outobj)
        if wall:
            output(wall)


if __name__ == '__main__':
    main()
