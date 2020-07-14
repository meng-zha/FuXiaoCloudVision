
import open3d as o3d
import os


class Display:

    path_number = 4
    current_position = [0]*path_number
    path = [os.path]*path_number
    activated_path = 1

    def __init__(self, position):
        self.current_position = position

    def pre_process(self):
        PATH = "data"
        points = []
        for i in range(self.path_number):
            self.path[i] = os.path.join(PATH, "FuXiao_"+str(i+1),
                                        "FuXiao_"+str(i+1)+"__"+str(self.current_position[i])+".pcd")
            points.append(o3d.io.read_point_cloud(self.path[i]))

        points[0].paint_uniform_color([254/254, 67/254, 101/254])  # FuXiao1 is red
        points[1].paint_uniform_color([249/254, 205/254, 173/254])  # FuXiao2 is yellow
        points[2].paint_uniform_color([131/254, 175/254, 155/254])  # FuXiao3 is green
        points[3].paint_uniform_color([38/254, 188/254, 213/254])  # FuXiao4 is blue
        result = points[0] + points[1] + points[2] + points[3]
        print(self.path)
        return result

    def draw_geometry_with_key_callback(self):

        def move_next_100_simul(vis):
            for i in range(self.path_number):
                self.current_position[i] = self.current_position[i] + 100
            points = self.pre_process()
            vis.clear_geometries()
            vis.add_geometry(points)
            vis.poll_events()
            vis.update_renderer()

        def move_pre_100_simul(vis):
            for i in range(self.path_number):
                self.current_position[i] = self.current_position[i] - 100
            points = self.pre_process()
            vis.clear_geometries()
            vis.add_geometry(points)
            vis.poll_events()
            vis.update_renderer()

        def free_choose_frame(vis):
            i, j = map(int, input("input your choice of path and frame for subsequent operation: ").strip().split())
            self.activated_path = i
            self.current_position[i-1] = j
            print("Next frame is FuXiao_", self.activated_path, " ", self.current_position[i-1], "pcd")
            points = self.pre_process()
            vis.clear_geometries()
            vis.add_geometry(points)
            vis.poll_events()
            vis.update_renderer()

        def activate_path(vis):
            self.activated_path = int(input("input your choice of path for subsequent operation: "))

        def dropout(vis):
            print("\nDisplay finished\n")
            exit(0)

        def move_next_10_for_activated_path(vis):
            self.current_position[self.activated_path-1] = self.current_position[self.activated_path-1] + 10
            points = self.pre_process()
            vis.clear_geometries()
            vis.add_geometry(points)
            vis.poll_events()
            vis.update_renderer()

        def move_pre_10_for_activated_path(vis):
            self.current_position[self.activated_path-1] = self.current_position[self.activated_path-1] - 10
            points = self.pre_process()
            vis.clear_geometries()
            vis.add_geometry(points)
            vis.poll_events()
            vis.update_renderer()

        def move_next_for_activated_path(vis):
            self.current_position[self.activated_path-1] = self.current_position[self.activated_path-1] + 1
            points = self.pre_process()
            vis.clear_geometries()
            vis.add_geometry(points)
            vis.poll_events()
            vis.update_renderer()

        def move_pre_for_activated_path(vis):
            self.current_position[self.activated_path-1] = self.current_position[self.activated_path-1] -1
            points = self.pre_process()
            vis.clear_geometries()
            vis.add_geometry(points)
            vis.poll_events()
            vis.update_renderer()

        points = self.pre_process()
        vis = o3d.visualization.VisualizerWithKeyCallback()
        vis.create_window()
        vis.add_geometry(points)

        while True:
            vis.poll_events()
            vis.update_renderer()

            vis.register_key_callback(ord("."), move_next_100_simul)
            vis.register_key_callback(ord(","), move_pre_100_simul)
            vis.register_key_callback(ord("O"), dropout)
            vis.register_key_callback(ord("P"), free_choose_frame)
            vis.register_key_callback(ord("A"), activate_path)
            vis.register_key_callback(ord("E"), move_next_10_for_activated_path)
            vis.register_key_callback(ord("W"), move_pre_10_for_activated_path)
            vis.register_key_callback(ord("S"), move_pre_for_activated_path)
            vis.register_key_callback(ord("D"), move_next_for_activated_path)


if __name__ == '__main__':
    option = list(input("Please input 4 initial positions: ").split())
    option = [int(option[i]) for i in range(len(option))]
    print(option)
    demo = Display(option)
    demo.draw_geometry_with_key_callback()











