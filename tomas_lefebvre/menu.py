# -*- coding: UTF-8 -*-
import nuke

m = nuke.menu('Nodes')
m.menu('3D').addCommand('TX_Fog', lambda: nuke.createNode('TX_Fog'))
m.menu('Keyer').addCommand('TX_HueKeyer', lambda: nuke.createNode('TX_HueKeyer'))
