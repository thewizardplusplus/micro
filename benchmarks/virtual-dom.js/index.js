// https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060
// https://medium.com/@deathmood/write-your-virtual-dom-2-props-events-a957608f5c76

function make_node(type, ...children) {
  return {type, children}
}

function make_difference(path, action, ...parameters) {
  return {path, action, parameters}
}

module.exports = {
  make_node,
}
