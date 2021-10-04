# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:49:28 2020

@author: krish
"""
import networkx as nx
import matplotlib.pyplot as plt

G=nx.barabasi_albert_graph(50,2)

nx.draw(G)
plt.show()

nx.write_gexf(G,"analysis1.gexf")