from app.services.database import get_nodes
from app.services.utils import sha256

def diff_nodes(ver1, ver2):
    nodes1 = get_nodes(ver1)
    nodes2 = get_nodes(ver2)

    diff_result = []

    n1 = {n[0]: n for n in nodes1}
    n2 = {n[0]: n for n in nodes2}

    for nid in set(list(n1.keys()) + list(n2.keys())):
        if nid in n1 and nid in n2:
            if n1[nid][6] != n2[nid][6]:
                diff_result.append({
                    "node_id": nid,
                    "heading": n1[nid][3],
                    "old_hash": n1[nid][6],
                    "new_hash": n2[nid][6],
                    "changed": True
                })
        elif nid in n1:
            diff_result.append({
                "node_id": nid,
                "heading": n1[nid][3],
                "old_hash": n1[nid][6],
                "new_hash": None,
                "changed": True
            })
        else:
            diff_result.append({
                "node_id": nid,
                "heading": n2[nid][3],
                "old_hash": None,
                "new_hash": n2[nid][6],
                "changed": True
            })

    return diff_result

def get_node_hash(node_id):
    from app.services.database import get_node
    node = get_node(node_id)
    if node:
        return node[6]
    return None
