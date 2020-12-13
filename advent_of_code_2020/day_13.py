import logging
from functools import reduce
import numpy as np

from .utils import read_list_file, sort_list


logger = logging.getLogger(__name__)


def read_shuttle_schedule(input_file):
    lines = read_list_file(input_file)
    timestamp = int(lines[0].rstrip())
    bus_ids = lines[1].rstrip().split(",")
    offsets = list(range(len(bus_ids)))
    offsets = [offset for bus_id, offset in zip(bus_ids, offsets) if bus_id != "x"]
    bus_ids = [int(bus_id) for bus_id in bus_ids if bus_id != "x"]
    return timestamp, bus_ids, offsets


def get_next_bus(timestamp, bus_ids):
    this_timestamp = timestamp
    while True:
        residuals = [this_timestamp % bus_id for bus_id in bus_ids]
        try:
            bus_depart_index = residuals.index(0)
            bus_id = bus_ids[bus_depart_index]
            return this_timestamp - timestamp, bus_id
        except:
            logger.debug("No bus here")
            this_timestamp += 1


def get_auspicious_timestamp(bus_ids, offsets):
    this_timestamp = 0
    max_bus_id = max(bus_ids)
    max_bus_id_index = bus_ids.index(max_bus_id)
    max_bus_id_offset = offsets[max_bus_id_index]
    max_relative_offsets = [offset - max_bus_id_offset for offset in offsets]

    aligned_bus_ids = [
        bus_id for bus_id, relative_offset in zip(bus_ids, max_relative_offsets)
        if (relative_offset % bus_id) == 0
    ]
    nonaligned_bus_ids_offsets = [
        (bus_id, relative_offset)
        for bus_id, relative_offset in zip(bus_ids, max_relative_offsets)
        if (relative_offset % bus_id) != 0
    ]
    min_factor = reduce((lambda x, y: x * y), aligned_bus_ids)

    while True:
        residuals = [
            (this_timestamp + offset) % bus_id
            for bus_id, offset in nonaligned_bus_ids_offsets
        ]

        if all(residual == 0 for residual in residuals):
            return this_timestamp + max_relative_offsets[0]
        else:
            this_timestamp += min_factor



def day_13(part, input_file):
    timestamp, bus_ids, offsets = read_shuttle_schedule(input_file)
    if part == 1:
        wait_time, departure_bus_id = get_next_bus(timestamp, bus_ids)
        output = wait_time * departure_bus_id
        logger.info(f"You wait {wait_time} minutes for the {departure_bus_id} bus, yielding {output}")
    elif part == 2:
        timestamp = get_auspicious_timestamp(bus_ids, offsets)
        logger.info(f"The auspicious time is {timestamp}")
