import json
from rosbags.rosbag2 import Reader
from rosbags.typesys import Stores, get_typestore

typestore = get_typestore(Stores.ROS2_HUMBLE)

scan_msgs_json = []
# see https://answers.ros.org/question/358686/how-to-read-a-bag-file-in-ros2/
with Reader("scan") as reader:
    # iterate over messages
    for connection, timestamp, rawdata in reader.messages():
        if connection.topic == "/scan":
            msg = typestore.deserialize_cdr(rawdata, connection.msgtype)
            scan_msgs_json.append(
                {
                    "timestamp": msg.header.stamp.sec + 1e-9 * msg.header.stamp.nanosec,
                    "angle_min": msg.angle_min,
                    "angle_max": msg.angle_max,
                    "angle_increment": msg.angle_increment,
                    "ranges": msg.ranges.tolist(),
                }
            )

with open("scan.json", "w") as f:
    json.dump(scan_msgs_json, f)
