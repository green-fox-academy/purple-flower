'use strict';

jest.dontMock('../app/components/Main.jsx');

var React = require('react');
var ReactDOM = require('react-dom');
var TestUtils = require('react-addons-test-utils');

var Main = require('../app/components/Main.jsx');

describe('Main', function() {
  var h1;

  it('should exists', function() {
    var renderedComponent = TestUtils.renderIntoDocument(
      <Main />
    );
    expect(TestUtils.isCompositeComponent(renderedComponent)).toBeTruthy();

    var renderedh1 = TestUtils.findRenderedDOMComponentWithTag(renderedComponent, 'h1'
    );

    h1 = ReactDOM.findDOMNode(renderedh1);
  });

  it('contain Hello World text', function() {
    expect(h1.textContent).toEqual("Hello World");

  });

});
