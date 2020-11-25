def main():
    with open("2019/day3input.txt", "r") as f:
        data = f.readlines()
        wire_one = data[0].split(",")
        wire_two = data[1].split(",")

    pts_vis_one = set()
    pts_vis_one.add((0, 0))
    last_pt = (0, 0)
    for leg in wire_one:
        new_pts, last_pt = parse_instruction_give_pts(leg, pts_vis_one, last_pt)
        pts_vis_one = new_pts

    pts_vis_two = set()
    pts_vis_two.add((0, 0))
    last_pt = (0, 0)
    for leg in wire_two:
        new_pts, last_pt = parse_instruction_give_pts(leg, pts_vis_two, last_pt)
        pts_vis_two = new_pts

    common = pts_vis_one.intersection(pts_vis_two)
    common.remove((0, 0))
    closest_distance = 1e15
    for pt in common:
        distance = abs(pt[0]) + abs(pt[1])
        closest_distance = min(distance, closest_distance)

    print(closest_distance)


def parse_instruction_give_pts(instruction, points_visited, last_point):
    direction = instruction[0]
    distance = int(instruction[1:])

    for i in range(distance):
        if direction == "R":
            new_point = (last_point[0] + 1, last_point[1])
        elif direction == "L":
            new_point = (last_point[0] - 1, last_point[1])
        elif direction == "U":
            new_point = (last_point[0], last_point[1] + 1)
        elif direction == "D":
            new_point = (last_point[0], last_point[1] - 1)
        else:
            print("Bad direction parsed.")
            raise

        points_visited.add(new_point)
        last_point = new_point

    return points_visited, last_point


if __name__ == "__main__":
    main()