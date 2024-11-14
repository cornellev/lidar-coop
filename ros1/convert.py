import rosbag
import json

bag = rosbag.Bag("scan.bag", "r")

scan_msgs_json = []
for bag_msg in bag.read_messages("/scan"):
    msg = bag_msg.message
    scan_msgs_json.append({
        "timestamp": bag_msg.timestamp.secs + 1e-9 * bag_msg.timestamp.nsecs,
        "angle_min": msg.angle_min,
        "angle_max": msg.angle_max,
        "angle_increment": msg.angle_increment,
        "ranges": msg.ranges
    })

with open("scan.json", "w") as f:
    json.dump(scan_msgs_json, f)