# Deep-loop-clousre

A C++ library for online SLAM loop closure using CALC models. 

## Dependencies

Required:
- OpenCV >= 2.0
- Eigen >= 3.0
- Boost filesystem
- Caffe 

## Build

```
$ mkdir build && cd build
$ cmake -DCaffe_ROOT_DIR=<path/to/caffe> .. && make
```

## ROS Demo

## Dependencies
- ROS Melodic

## Build
```
catkin_make -DCaffe_ROOT_DIR=<path/to/caffe>
```

## Run
```
$ roscore
$ source devel/setup.bash
$ roslaunch launch/online-demo.launch
```

## Result
see online-demo_ws/loop-points.csv
