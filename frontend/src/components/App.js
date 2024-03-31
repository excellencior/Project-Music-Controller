import React, { Component } from "react";
import { render } from "react-dom";

export default class App extends Component {
	constructor(props) {
		super(props);
	}

	render() {
		return <p style={{ fontSize: "10em", color: "red" }}>Hello World</p>;
	}
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
