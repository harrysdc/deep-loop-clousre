import matplotlib.pyplot as plt



def plot_xy_position(filename, filename2):
    # Read in data from file
    ids, xs, ys, zs = [], [], [], []
    with open(filename, 'r') as f:
        for line in f:
            id, x, y, z = line.strip().split(',')
            ids.append(int(id))
            xs.append(float(x))
            ys.append(float(y))
            zs.append(float(z))
    
    # Create scatter plot of x-y positions
    fig, ax = plt.subplots()
    ax.scatter(xs, zs)


    loop_ids = []
    with open(filename2, 'r') as f:
        for line in f:
            frame_id1, frame_id2, x1, y1, z1, x2, y2, z2 = line.strip().split(', ')
            loop_ids.append(int(frame_id1))
    print(loop_ids)



    # Mark data point with id 315 and 2 in red
    for id, x, y in zip(ids, xs, zs):
        if id in loop_ids and not id%2:
            ax.scatter(x, y, color='red')

    # Set axis labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Loop Detection Result (KITTI Sequence 00)')
    ax.legend()
    
    # Show plot
    plt.show()

plot_xy_position('db-points.txt', 'loop-points.txt')