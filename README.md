# Deep-loop-clousre
A C++ library for online SLAM loop closure using CALC models.

<p float="left">
<img src="https://github.com/harrysdc/deep-loop-clousre/blob/main/loop-kitti-09.png"  width="30%" height="30%">
<img src="https://github.com/harrysdc/deep-loop-clousre/blob/main/loop-kitti-00.png"  width="30%" height="30%">
<img src="https://github.com/harrysdc/deep-loop-clousre/blob/main/loop-kitti-05.png"  width="30%" height="30%">
</p>


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

## Reference
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
