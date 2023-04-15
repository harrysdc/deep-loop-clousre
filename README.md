# Deep-loop-clousre

A C++ library for online SLAM loop closure using CALC models. 

## Dependencies

Required:
- OpenCV >= 2.0
- Eigen >= 3.0
- Boost filesystem
- Caffe 

## Getting started

```
$ mkdir build && cd build
$ cmake -DCaffe_ROOT_DIR=</path/to/caffe> .. && make
$ roslaunch launch/online-demo.launch
```

## Demo
The loop result is in online-demo_ws/loop-points.csv
