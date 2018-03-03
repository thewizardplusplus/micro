require('chai').should()
// const {make_node, compare_nodes} = require('..')
const {make_node, compare_nodes} = require('../index.min.js')

describe('compare_nodes', () => {
  it("should create a node when there's no old node at same place", () => {
    const new_node = make_node('input')
    const difference = compare_nodes(undefined, new_node, 5, ['section', 'form'])
    difference.should.deep.equal([{
      path: ['section', 'form'],
      action: 'create',
      parameters: [new_node],
    }])
  })

  it("should remove a node when there's no new node at same place", () => {
    const old_node = make_node('input')
    const difference = compare_nodes(old_node, undefined, 5, ['section', 'form'])
    difference.should.deep.equal([{
      path: ['section', 'form'],
      action: 'remove',
      parameters: [5],
    }])
  })

  it("should replace a node when there's a different node at same place", () => {
    const old_node = make_node('input')
    const new_node = make_node('textarea')
    const difference = compare_nodes(old_node, new_node, 5, ['section', 'form'])
    difference.should.deep.equal([{
      path: ['section', 'form'],
      action: 'replace',
      parameters: [5, new_node],
    }])
  })

  it("should go deeper when there're same nodes at same place", () => {
    const old_node = make_node('label', make_node('span'), make_node('input'))
    const new_node = make_node('label', make_node('span'), make_node('textarea'))
    const difference = compare_nodes(old_node, new_node, 5, ['section', 'form'])
    difference.should.deep.equal([{
      path: ['section', 'form', 'label'],
      action: 'replace',
      parameters: [1, make_node('textarea')],
    }])
  })
})
