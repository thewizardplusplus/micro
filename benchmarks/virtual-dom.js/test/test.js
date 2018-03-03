require('chai').should()
const {make_node, compare_nodes} = require('..')

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
})
