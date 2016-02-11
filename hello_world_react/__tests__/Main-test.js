jest.dontMock('../app/components/Main.jsx');

var React = require('react');
var ReactDOM = require('react-dom');
var TestUtils = require('react-addons-test-utils');

var Main = require('../app/components/Main.jsx');

describe('Main', function() {
  it('should exists', function() {
    var renderedComponent = TestUtils.renderIntoDocument(
      <Main />
    );
    expect(TestUtils.isCompositeComponent(renderedComponent)).toBeTruthy();
  });

  //
  // var h1 = TestUtils.findRenderedDOMComponentWithTag(renderedComponent, 'h1'
  // );
  //
  // expect(h1.textContent).toEqual("Hello World");


});
