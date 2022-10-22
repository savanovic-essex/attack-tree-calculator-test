# coding=utf-8
import ast
import json
import webbrowser

from pyvis.network import Network

got_net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")
attack_tree_net = Network(height="100%", width="50%", bgcolor="#222222", font_color="white", layout=True)

# JSON file
with open('attack_tree.json', 'r') as file:
    attack_tree = json.load(file)
    attack_tree = ast.literal_eval(json.dumps(attack_tree))

nodes = attack_tree['nodes']
at_nodes = []

for a in nodes:
    name = a['name']
    ID = str(a['id'])
    damage = a["damage"]
    reproducibility = a["reproducibility"]
    exploitability = a["exploitability"]
    affected_users = a["affected_users"]
    discoverability = a["discoverability"]
    at_nodes.append(str(ID) + ':' + name)

attack_tree_net.barnes_hut()

for n in nodes:
    idNumber = n["id"]
    label = n["name"]
    damage = n["damage"]
    reproducibility = n["reproducibility"]
    exploitability = n["exploitability"]
    affected_users = n["affected_users"]
    discoverability = n["discoverability"]
    attack_tree_net.add_node(str(idNumber), str(label), shape="box", damage=damage, reproducibility=reproducibility,
                             exploitability=exploitability, affected_users=affected_users,
                             discoverability=discoverability, title=label)

edges = attack_tree['edges']

for e in edges:
    toID = e['to']
    fromID = e['from']
    attack_tree_net.add_edge(str(fromID), str(toID), value=1)

attack_tree_net.hrepulsion(node_distance=160)
attack_tree_net.show_buttons(filter_=['edges'])

fileName = raw_input("Enter file name:")
print(fileName)
attack_tree_net.show(fileName + ".html")

url = fileName + ".html"
webbrowser.open_new_tab(url)
