from .decoder import MapDatabase
import psycopgr as pgr


class PGRouting(MapDatabase):
    def connect_lines(self, node, frc_max, beardir):    
        """ Return connected lines to/from the node 'node'
        
            :param frc_max: the frc max of the requested lines
            :param beardir: select the inwards (AGAINST_LINE_DIRECTION)
            or the outwards (WITH_LINE_DIRECTION) connected lines

            return an iterable of objects of type Line
        """
        raise NotImplementedError("MapDatabase:connectedlines")

    def find_closeby_nodes(self, coords, max_node_dist):
        """ Look for all nodes at less than max_node_dist from
            the given coordinates
            
            :param coords: an tuple or iterable holding location coordinates
            :param max_node_dist: max distance to nearch for nodes

            return an iterable of Node objects
        """
        raise NotImplementedError("MapDatabase:find_closeby_nodes")

    def find_closeby_lines(self, coords, max_node_dist, frc_max, beardir):
        """ Look for all lines at less than max_node_dist from
            the given coordinates
            
            :param coords: an tuple or iterable holding location coordinates
            :param max_node_dist: max distance to nearch for nodes
            :param frc_max: the frc max of the requested line
            :param beardir: select the inwards (AGAINST_LINE_DIRECTION)
            or the outwards (WITH_LINE_DIRECTION) connected lines

            return an iterable of Line objects
        """
        raise NotImplementedError("MapDatabase:find_closeby_lines")

    def calculate_route(self, l1, l2, maxdist, lfrc, islastrp):
        """ Calculate the shortest paths between two lines
        
            :param l1: the first candidate line to begin the search from
            :param l2: the second candidate line to stop the search to
            :param maxdist: The maximum distance allowed
            :param lfrc: The least frc allowed
            :param islastrp: True if we are calculating the route to the last
            reference point
            :return: (route, length) where route is an iterable holding the lines found
            and length the calculated length  of the route
    
            The method must throw a RouteNotFoundException or a RouteConstructionFailed
            exception in case a route cannot be calculated
        """
        raise NotImplementedError("MapDatabase:calculate_route")
