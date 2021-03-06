require('chai').should()
const {make_node, compare_nodes} = require(process.env.TEST_SOURCE)

describe('compare_nodes()', () => {
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

  it("should replace a node when there's a different object at same place", () => {
    const old_node = make_node('input')
    const new_node = make_node('textarea')
    const difference = compare_nodes(old_node, new_node, 5, ['section', 'form'])
    difference.should.deep.equal([{
      path: ['section', 'form'],
      action: 'replace',
      parameters: [5, new_node],
    }])
  })

  it("should replace a node when there's an object and a string at same place", () => {
    const old_node = make_node('input')
    const new_node = 'text'
    const difference = compare_nodes(old_node, new_node, 5, ['section', 'form'])
    difference.should.deep.equal([{
      path: ['section', 'form'],
      action: 'replace',
      parameters: [5, new_node],
    }])
  })

  it("should replace a node when there's a different string at same place", () => {
    const old_node = 'text #1'
    const new_node = 'text #2'
    const difference = compare_nodes(old_node, new_node, 5, ['section', 'form'])
    difference.should.deep.equal([{
      path: ['section', 'form'],
      action: 'replace',
      parameters: [5, new_node],
    }])
  })

  it("should go deeper when there're same nodes at same place", () => {
    const old_node = make_node('label', {}, 'Message', make_node('input'))
    const new_node = make_node('label', {}, 'Message', make_node('textarea'))
    const difference = compare_nodes(old_node, new_node, 5, ['section', 'form'])
    difference.should.deep.equal([{
      path: ['section', 'form', 'label'],
      action: 'replace',
      parameters: [1, make_node('textarea')],
    }])
  })

  it("should set a property when an old node hasn't a property with same name", () => {
    const old_node = make_node('input', {class: 'form-control'})
    const new_node = make_node('input', {class: 'form-control', type: 'email'})
    const difference = compare_nodes(old_node, new_node, 5, ['section', 'form'])
    difference.should.deep.equal([{
      path: ['section', 'form', 'input'],
      action: 'set_property',
      parameters: ['type', 'email'],
    }])
  })

  it("should remove a property when a new node hasn't a property with same name", () => {
    const old_node = make_node('input', {class: 'form-control', type: 'email'})
    const new_node = make_node('input', {class: 'form-control'})
    const difference = compare_nodes(old_node, new_node, 5, ['section', 'form'])
    difference.should.deep.equal([{
      path: ['section', 'form', 'input'],
      action: 'remove_property',
      parameters: ['type'],
    }])
  })

  it("should set a property when a property with same name has a different value", () => {
    const old_node = make_node('input', {class: 'form-control', type: 'username'})
    const new_node = make_node('input', {class: 'form-control', type: 'email'})
    const difference = compare_nodes(old_node, new_node, 5, ['section', 'form'])
    difference.should.deep.equal([{
      path: ['section', 'form', 'input'],
      action: 'set_property',
      parameters: ['type', 'email'],
    }])
  })
})
