import matplotlib.pyplot as plt


class Projection3D:
    def __init__(self):
        fig = plt.figure()
        fig.suptitle("World Landmarks", fontsize=20)
        self.ax_list = [
            fig.add_subplot(121, projection="3d"),
            fig.add_subplot(122, projection="3d"),
        ]
        fig.subplots_adjust(left=0.0, right=1, bottom=0, top=1)

    def initialize(self):
        self.ax_list[0].cla()
        self.ax_list[0].set_title("Left")
        self.ax_list[0].set_xlim3d(-0.1, 0.1)
        self.ax_list[0].set_ylim3d(-0.1, 0.1)
        self.ax_list[0].set_zlim3d(-0.1, 0.1)
        self.ax_list[0].set_xlabel("X")
        self.ax_list[0].set_zlabel("Y")
        self.ax_list[0].set_ylabel("Z")
        self.ax_list[1].cla()
        self.ax_list[1].set_title("Right")
        self.ax_list[1].set_xlim3d(-0.1, 0.1)
        self.ax_list[1].set_ylim3d(-0.1, 0.1)
        self.ax_list[1].set_zlim3d(-0.1, 0.1)
        self.ax_list[1].set_xlabel("X")
        self.ax_list[1].set_zlabel("Y")
        self.ax_list[1].set_ylabel("Z")

    def wait(self):
        plt.pause(0.001)
