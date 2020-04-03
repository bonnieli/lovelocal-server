import "./App.scss";
import React from "react";

import { Button, Popover, Row, Col } from "antd";

import logo from "./assets/images/logo.jpg";
import Main from "./Components/Main";
import ShareOptions from "./Components/ShareOptions";
import About from "./Components/About";

import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

const App = () => {
  return (
    <Router>
      <div>
        <Row className="top-header">
          <Col xs={24} sm={8}>
            <Link to="/">
              <img src={logo} width={100} style={{ padding: 10 }} />
            </Link>
          </Col>
          <Col xs={24} sm={16}>
            <ul className="nav">
              <li>
                <Link to="/about">About</Link>
              </li>
              <li>
                <Link to="/faq">FAQ</Link>
              </li>
              <li>
                <Popover content={<ShareOptions />}>
                  <Button shape="round" className="header-button">
                    Tell friends
                  </Button>
                </Popover>
              </li>
            </ul>
          </Col>
        </Row>

        <Switch>
          <Route path="/about">
            <About />
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
