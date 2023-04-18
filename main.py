from dijkstar import Graph, find_path, NoPathError
graph = Graph()
open('output.txt', 'w').close
output = open('output.txt', 'w')
file_position = 0


def create_graph():
    topo = open('topology.txt', 'r')
    for node in topo:
        node = node.rstrip("\n").split(" ")
        graph.add_edge(int(node[0]), int(node[1]), int(node[2]))
        graph.add_edge(int(node[1]), int(node[0]), int(node[2]))


def count_clines():
    with open('changes.txt', 'r') as file:
        line_count = 0
        for line in file:
            line_count += 1
        return line_count


def count_mlines():
    with open('message.txt', 'r') as file:
        line_count = 0
        for line in file:
            line_count += 1
        return line_count


def topology():
    num_nodes = graph.node_count
    for node_num in (range(num_nodes)):
        for next_node in (range(num_nodes)):
            path_info = find_path(graph, node_num+1, next_node+1)
            path = path_info.nodes
            cost = path_info.total_cost

            if len(path) < 2:
                output.write(
                    f"{str(path_info.nodes).strip('[]')} {str(path_info.nodes).strip('[]')} 0\n")
            else:
                output.write(
                    f"{next_node+1} {str(path_info.nodes[1]).strip('[]')} {cost}\n")
        output.write("\n")


def change():
    global file_position
    with open('changes.txt', 'r') as changes:
        changes.seek(file_position)
        node = changes.readline().rstrip("\n").split(" ")
        if node[2] == str(-999):
            graph.remove_edge(int(node[0]), int(node[1]))
        else:
            graph.add_edge(int(node[0]), int(node[1]), int(node[2]))
            graph.add_edge(int(node[1]), int(node[0]), int(node[2]))
        file_position = changes.tell()


def read_messages():
    message = open('message.txt', 'r')
    msg = []
    for line in message:
        msg.append(line[0:1])
        msg.append(line[2:3])
        msg.append(line[4:].rstrip("\n"))
        try:
            path_info = find_path(graph, int(msg[0]), int(msg[1]))
            path = path_info.nodes
            path_cost = path_info.total_cost

            output.write(
                f'from {msg[0]} to {msg[1]} cost {path_cost} hops {str(path[:-1]).strip("[,]")} message {msg[2]}\n')
            msg = []
        except NoPathError:
            output.write(
                f'from {msg[0]} to {msg[1]} cost infinite hops unreachable message {msg[2]}\n')
            msg = []


def main():
    counter = 0
    create_graph()
    while True:
        if count_clines() == 0 or count_mlines() == 0:
            topology()
            break
        else:
            if counter < count_clines():
                topology()
                read_messages()
                change()
                counter += 1
            elif counter == count_clines():
                topology()
                read_messages()
                break
    output.write("end")


if __name__ == '__main__':
    main()
