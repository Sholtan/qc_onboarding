import netsquid as ns

print("This example module is located at: {}".format(ns.examples.teleportation.__file__))

from netsquid.examples.teleportation import create_plot


create_plot()