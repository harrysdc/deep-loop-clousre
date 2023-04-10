# Deep-loop-clousre

A C++ library for online SLAM loop closure using CALC models. 

## Dependencies

Required:
- OpenCV >= 2.0
- Eigen >= 3.0
- Boost filesystem
- Caffe 

Optional but HIGHLY Recommended:
- CUDA

## To Compile

```
$ mkdir build && cd build
$ cmake .. && make # Already set to Release build
```

Note that if your caffe is not installed in ~/caffe, you must use 

```
$ cmake -DCaffe_ROOT_DIR=</path/to/caffe> .. && make
```
instead.


## Demo
The loop result is in online-demo_ws/loop-points.csv


## Online Loop Closure Demo with ROS

See online-demo-ws
