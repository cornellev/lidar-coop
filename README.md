# LiDAR Coop

Conversion code so Data A&A can work on LiDAR data visualization without needing ROS. We're going to write realtime ROS code that sends this data to their HTTP endpoints at some point, but this is a workaround until both of us have our respective ends set up for that.

This conversion relies on rosbag recordings of experiments where LiDAR data was collected. Since rosbag behavior is different across ROS1 and ROS2, there are different `convert.py` scripts in `ros1/` and `ros2/`.

## Usage for ROS 1

Copy bagfile into `ros1/scan.bag`. It must have that name. Then `cd ros1` and run `convert.py`.

## Usage for ROS 2

Bagfiles in ROS 2 are actually directories. Copy the `.db3` file and `metadata.yaml` file into `ros2/scan/`. Then `cd ros2` and run `convert.py`.
