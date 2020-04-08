import React from "react";

import { Typography, Row, Col } from "antd";

import NeighborhoodCards from "./NeighborhoodCards";

const { Title } = Typography;

const Main = () => {
  return (
    <div style={{ marginTop: "0px" }}>
      <Row className="hero-row">
        <div style={{ maxWidth: "1100px", margin: "0px auto" }}>
          <Col
            xs={{ span: 18, offset: 3 }}
            span={16}
            offset={4}
            style={{ textAlign: "center", padding: "20px 0px" }}
          >
            <Title level={1} style={{ textAlign: "center" }}>
              Show support to your favourite Toronto businesses.
            </Title>
            <div className="header-sans">
              Support your favourite local restaurants by buying gift cards now
              that will help business owners stay afloat.
            </div>
          </Col>
          <Col sm={{ span: 20, offset: 2 }}>
            <div className="main-results">
              <div className="neighborhood-card-container-outer">
                <NeighborhoodCards />
              </div>
            </div>
          </Col>
          <Row className="footer-content">
            <Col sm={{ span: 20, offset: 2 }} style={{ textAlign: "center" }}>
              <Title level={3}>Our duty as loyal customers</Title>
              <p>
                Many businesses are in a difficult cash situation as social
                isolation and quarantine has forced most people to stay in their
                homes and non- essential businesses have closed their doors.
                Gift cards keep income flowing to local restaurateurs that are
                having to pay rent and other expenses while businesses are
                closed.
              </p>
            </Col>
          </Row>
        </div>
      </Row>
    </div>
  );
};

export default Main;
