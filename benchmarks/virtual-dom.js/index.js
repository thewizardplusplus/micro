// https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060
// https://medium.com/@deathmood/write-your-virtual-dom-2-props-events-a957608f5c76

// Verbose naming of properties is needed for Google Closure Compiler.

function make_node(type, properties, ...children) {
  return {
    'type': type,
    'properties': properties || {},
    'children': children,
  }
}

function make_difference(path, action, ...parameters) {
  return {
    'path': path,
    'action': action,
    'parameters': parameters,
  }
}

function is_different(node_1, node_2) {
  return typeof node_1 !== typeof node_2
    || (typeof node_1 === 'object'
      ? node_1['type'] !== node_2['type']
      : node_1 !== node_2)
}

function compare_property(path, name, old_value, new_value) {
  let difference
  if (!new_value) {
    difference = make_difference(path, 'remove_property', name)
  } else if (!old_value || new_value !== old_value) {
    difference = make_difference(path, 'set_property', name, new_value)
  }

  return difference
}

function compare_properties(path, old_properties, new_properties) {
  const properties = Object.assign({}, old_properties, new_properties)
  return Object.keys(properties)
    .map(name => compare_property(path, name, old_properties[name], new_properties[name]))
    .filter(difference => difference)
}

function compare_nodes(old_node, new_node, index=0, path=[]) {
  let differences = []
  if (!old_node) {
    differences.push(make_difference(path, 'create', new_node))
  } else if (!new_node) {
    differences.push(make_difference(path, 'remove', index))
  } else if (is_different(old_node, new_node)) {
    differences.push(make_difference(path, 'replace', index, new_node))
  } else if (old_node['type']) {
    const child_path = [...path, old_node['type']]
    const properties_differences = compare_properties(child_path, old_node['properties'], new_node['properties'])
    differences.push(...properties_differences)

    const maximal_children_length = Math.max(old_node['children'].length, new_node['children'].length)
    for (let i = 0; i < maximal_children_length; i++) {
      const child_differences = compare_nodes(old_node['children'][i], new_node['children'][i], i, child_path)
      differences.push(...child_differences)
    }
  }

  return differences
}

module['exports'] = {
  'make_node': make_node,
  'compare_nodes': compare_nodes,
}
