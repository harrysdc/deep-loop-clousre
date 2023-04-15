# Deep-loop-clousre
  src="loop-kitti-09.png"
  alt="Alt text"
  title="Optional title"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  
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

```
@InProceedings{Merrill2018RSS,
  Title                    = {Lightweight Unsupervised Deep Loop Closure},
  Author                   = {Nathaniel Merrill and Guoquan Huang},
  Booktitle                = {Proc. of Robotics: Science and Systems (RSS)},
  Year                     = {2018},
  Address                  = {Pittsburgh, PA},
  Month                    = jun # { 26-30, }
}
```
