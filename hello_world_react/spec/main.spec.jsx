var React = require('react/addons'),
    Main = require('../app/components/Main.jsx'),
    jsdom = require('jsdom'),
    TestUtils = React.addons.TestUtils;

global.document = jsdom.jsdom('<!doctype html><html><body></body></html>');
global.window = document.parentWindow;

describe('Main', function() {
  before('render and locate element', function() {
    var renderedComponent = TestUtils.renderIntoDocument(
      <Main />
    );

    var h1 = TestUtils.findRenderedDOMComponentWithTag(renderedComponent, 'h1'
    );

    this.titleElement = h1.getDOMNode();
  });

  it('<h1> should contain Hello World', function() {
    expect(titleElement.testContent).toEqual("Hello World");
  });
});
