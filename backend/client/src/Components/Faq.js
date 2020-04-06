import React, { useEffect } from "react";

import { Typography, Row, Col, Collapse } from "antd";
import { Mixpanel } from "../lib/Mixpanel";

const { Panel } = Collapse;

const { Title } = Typography;

const Faq = () => {
  const FORM_URL = process.env.REACT_APP_FORM_URL;

  useEffect(() => {
    Mixpanel.track("Visit: FAQ Page");
  }, []);

  return (
    <div>
      <Title level={1} style={{ textAlign: "center" }}>
        FAQ
      </Title>

      <Row>
        <Col xs={16} offset={4}>
          <Title level={2}>For Restaurant-goers</Title>

          <Collapse defaultActiveKey={["1"]}>
            <Panel header="What is LoveLocals?" key="1">
              <p>
                Love Local is a directory of gift cards for purchase at local
                Toronto based restaurants and coffee shops. It’s our hope that
                by providing this resource, we’ll be able to mobilize loyal
                customers to provide much-needed support for their favorite
                places in town. We also link to staff donation sites, if they
                are available.
              </p>
            </Panel>
            <Panel
              header="Why isn’t my favorite business on your site?"
              key="2"
            >
              <p>Please help us add any missing spots here.</p>
            </Panel>
            <Panel
              header="How else can I support our local businesses beyond purchasing a gift card?"
              key="3"
            >
              <p>
                There are some great delivery and pickup options available in
                Toronto including SkipTheDishes, UberEats, Foodora and DoorDash.
                These sites should have the most up to date information but some
                restaurants that don’t normally offer delivery have started to
                offer pickup or delivery which is listed on their website or
                socials. Check their website or social media for the latest
                info. Tip generously if you can (even for delivery/pickup),
                since employees are doing extra work and putting their health at
                risk.
              </p>
            </Panel>
          </Collapse>

          <Title level={2} style={{ marginTop: 20 }}>
            For Businesses
          </Title>

          <Collapse defaultActiveKey={["1"]}>
            <Panel
              header="Why isn’t my business showing up in your search results?"
              key="1"
            >
              <p>
                We would love to add your Toronto based business. Please let us
                know{" "}
                <a
                  href={`${FORM_URL}`}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  here
                </a>
                .
              </p>
            </Panel>
            <Panel
              header="My business offers gift certificates, but your site says we don’t"
              key="2"
            >
              <p>
                Please let us know{" "}
                <a
                  href={`${FORM_URL}`}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  here
                </a>
                .
              </p>
            </Panel>
            <Panel header="How can I start offering online gift cards?" key="3">
              <p>
                Check with your POS provider! Many offer their own gift card
                features (e.g. Lightspeed, Square, Toast, ShopKeep), and others
                integrate with specific third-party providers. In the interim if
                you want to include an email address for customers to reach out
                directly that works too.
              </p>
            </Panel>
            <Panel
              header="How can I encourage customers to buy gift cards?"
              key="4"
            >
              <p>
                Use your platform to let people know how they can best support
                you. Many people are looking for ways to support their favorite
                businesses right now but may just not be sure how. Reach out to
                your community on Facebook, Twitter, and Instagram, and use your
                email list to get in touch with your customers.
              </p>
            </Panel>
          </Collapse>
        </Col>
      </Row>
    </div>
  );
};

export default Faq;
