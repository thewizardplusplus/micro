// https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060
// https://medium.com/@deathmood/write-your-virtual-dom-2-props-events-a957608f5c76

function make_node(type, ...children) {
  return {type, children}
}

function make_difference(path, action, ...parameters) {
  return {path, action, parameters}
}

function is_different(node_1, node_2) {
  return typeof node_1 !== typeof node_2
    || (typeof node_1 === 'string' && node_1 !== node_2)
    || node_1.type !== node_2.type
}

function compare_nodes(old_node, new_node, index=0, path=[]) {
  if (!old_node) {
    return [make_difference(path, 'create', new_node)]
  } else if (!new_node) {
    return [make_difference(path, 'remove', index)]
  } else if (is_different(old_node, new_node)) {
    return [make_difference(path, 'replace', index, new_node)]
  } else if (old_node.type) {
    let difference = []
    const maximal_length = Math.max(old_node.children.length, new_node.children.length)
    for (let i = 0; i < maximal_length; i++) {
      const child_path = [...path, old_node.type]
      const child_difference = compare_nodes(old_node.children[i], new_node.children[i], i, child_path)
      difference.push(...child_difference)
    }

    return difference
  } else {
    return []
  }
}

module.exports = {
  make_node,
  compare_nodes,
}
