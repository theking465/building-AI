portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    # write the recursive function here
    # remember to print out the route as the recursion ends
    if len(ports) is 0:
        print(' '.join([portnames[i] for i in route]))
        return
    for i in range(len(ports)):
        newRoute = []
        for j in route:
            newRoute.append(j)
        port = ports[i]
        remPorts = ports[:i] + ports[i + 1:]
        newRoute.append(port)
        permutations(newRoute, remPorts)


# this will start the recursion with 0 as the first stop
permutations([0], list(range(1, len(portnames))))
