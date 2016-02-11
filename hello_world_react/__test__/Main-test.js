jest.dontMock('../app/components/Main.jsx');

var React = require('react');
var ReactDOM = require('react-dom');
var TestUtils = require('react-addons-test-utils');

var Main = require('../app/components/Main.jsx');

describe('Main', function() {
  it('render', function() {
    var renderedComponent = TestUtils.renderIntoDocument(
      <Main />
    );

    var h1 = TestUtils.findRenderedDOMComponentWithTag(renderedComponent, 'h1'
      );

    this.titleElement = h1.getDOMNode();
  });

  
});
