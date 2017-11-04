# Komment

class Base(object):
    """A Base is the underlying construct of the other classes defined here"""
    
    # A Base can be created
    def __init__(self):
        # A Base has a Name
        self.name       = None
        # A Base contains something
        self.contains   = None

    # What else is Common Amongst ALL?
    
    # A Base can create something to contain
    def create(self):
        """This function is supposed to create something this will then
        contain."""
        print "Not yet defined, go and do so!"
        pass

    # A Base can list whatever it contains
    def list(self):
        """This function is supposed to list whatever this contains."""
        print "Not yet defined, go and do so!"
        pass

    # A Base can be delete something it contains
    def delete(self):
        """This function is supposed to delete something this contains."""
        print "Not yet defined, go and do so!"

    # A base can show what it contains
    def show(self):
        """This function will show everything it contains."""
        print "Not yet defined, go and do so!"
        #May be defined here!!


class Node(Base):
    """A Node is a bit of Information, that may be a Theorem an Equation or
    just an Idea; transferable to other fields, too """
    
    # A Node is contained in a Network

    # A Node is linked to other Nodes

    # A Node may be contained in Clusters.

    # A if a Node is connected to a Node within a Cluster it is connected to
    #   that, too.

    pass

class Connection(Base):
    """A Connection signifies a Link between to Nodes, that may be an
    argumentation, or simply a relationship between the two."""

    # A Connection can exist:
    #   between a Node and a Node
    #   between a Node and a Cluster


    pass

class Network(Base):
    """A Network is a collection of Nodes,
    Connections and Clusters, it's the overarching structure of my project"""

    # A Network contains:
    #   Nodes
    #   Clusters

    # A Network can:
    
    #   create  : Nodes and Clusters

    #   create  : Connections between:
    #               Nodes and Nodes
    #               Nodes and Clusters
    #               Clusters and Clusters

    #   list    : Nodes and Clusters it contains

    #   see     : Connections between:
    #               all its Nodes and Clusters
    #               only its Nodes and Nodes
    #               only its Clusters and Clusters
    #               only its Nodes and Clusters

    #   delete  : Nodes and Clusters it contains
    
    #   remove  : Connections between any of its Contingents



    pass

class Cluster(Network, Node):
    """A Cluster is a Node that also is a Network,
    representing an entity within the Network.
    All Nodes with Connections to Nodes within a Cluster have a Connection to
    the Cluster as well."""

    # A Cluster is a Network and a Node
    # What else?

    passs
