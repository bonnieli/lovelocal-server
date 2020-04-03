import React, { useState } from "react";

import { Button, Popover, Typography, Row, Col } from "antd";

const { Title } = Typography;

const About = () => {
  return (
    <div>
      <Title level={1} style={{ textAlign: "center" }}>
        About
      </Title>

      <Row>
        <Col xs={16} offset={4} style={{ textAlign: "center" }}>
          <p>
            Coronavirus is a global public health crisis that is affecting all
            corners of the population and economy in different ways. Local
            businesses are the cornerstone of our communities, where we gather
            to celebrate, to connect, to conduct business and to eat some great
            food! Social isolation and quarantine during this time are hurting
            local businesses, as restaurants are forced to limit their options
            to take out and many people are choosing to stay home.{" "}
          </p>

          <p>
            Our goal with Love Local is to keep income flowing to local
            restaurants. LoveLocal is a directory of Toronto restaurants selling
            gift certificates to offset lost income. Users can search for
            restaurants or browse by neighborhood, and then click through to buy
            gift certificates straight from the eateries. Community members can
            support their local businesses by purchasing a gift card that they
            know they will use once circumstances change and they are able to
            leave their homes and conduct business as usual.{" "}
          </p>

          <p>
            We are trying to make it easier for people to support local
            businesses. We were inspired by initiatives in other cities and used
            the open sourced code from SaveOurFaves (thank you!)
          </p>
        </Col>
      </Row>
    </div>
  );
};

export default About;
