import "./App.scss";
import React, { useEffect } from "react";

import { Row, Col } from "antd";

import logo from "./assets/images/logo.jpg";
import Main from "./Components/Main";
import About from "./Components/About";
import Faq from "./Components/Faq";
import { Mixpanel } from "./lib/Mixpanel";

import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

const App = () => {
  const FORM_URL = process.env.REACT_APP_FORM_URL;

  useEffect(() => {
    Mixpanel.track("Visit: Homepage");
  }, []);

  return (
    <Router>
      <div>
        <Row className="top-header">
          <Col xs={24} sm={8}>
            <Link to="/">
              <img
                src={logo}
                alt="LoveLocals Logo"
                width={100}
                style={{ padding: 10 }}
              />
            </Link>
          </Col>
          <Col xs={24} sm={16}>
            <ul className="nav">
              <li>
                <Link to="/about">About</Link>
              </li>
              <li>
                <a
                  href={`${FORM_URL}`}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Add a business
                </a>
              </li>
              <li>
                <Link to="/faq">FAQ</Link>
              </li>
            </ul>
          </Col>
        </Row>

        <Switch>
          <Route path="/about">
            <About />
          </Route>

          <Route path="/faq">
            <Faq />
          </Route>

          <Route path="/">
            <Main />
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

export default App;
