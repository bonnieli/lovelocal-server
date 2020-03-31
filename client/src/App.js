import "./App.scss";
import React from "react";
import axios from "axios";

import { Button, Popover, Typography, Row, Col } from "antd";
import Areas from "./CityData/Areas";

import Config from "./Config";
import GoogleAnalyticsTag from "./Components/GoogleAnalyticsTag";
import FAQModal from "./Components/FAQModal";
import AddNewPlaceModal from "./Components/AddNewPlaceModal";
import NeighborhoodCards from "./Components/NeighborhoodCards";
import ShareOptions from "./Components/ShareOptions";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

const { Title } = Typography;

class App extends React.Component {
  constructor(props) {
    super(props);
    const path = window.location.pathname.slice(1).toLowerCase();
    const currentArea = Areas[path] ? path : "sf";

    this.state = {
      faqVisible: false,
      shareVisible: true,
      currentArea: currentArea,
      addPlaceVisible: path === "addplace"
    };

    this.selfRef = React.createRef();
  }

  showFAQModal() {
    this.setState({ faqVisible: true });
  }
  hideFAQModal() {
    this.setState({ faqVisible: false });
  }
  showShareModal() {
    this.setState({ shareVisible: true });
  }
  hideShareModal() {
    this.setState({ shareVisible: false });
  }
  hideAddModal() {
    window.history.pushState({}, "", "/");
    this.setState({ addPlaceVisible: false });
  }
  render() {
    return (
      <div>
        <div style={{ marginTop: "0px" }}>
          <FAQModal
            shouldShow={this.state.faqVisible}
            onClose={() => {
              this.hideFAQModal();
            }}
          />

          <Row className="hero-row">
            <div style={{ maxWidth: "1100px", margin: "0px auto" }}>
              <Row className="top-header">
                <Col span={24} offset={0}>
                  <Title style={{ float: "left", color: "white" }} level={4}>
                    LoveLocals
                  </Title>
                  <div style={{ float: "right" }}>
                    <a href="#">
                      <Title
                        onClick={() => {
                          this.showFAQModal();
                        }}
                        style={{
                          color: "white",
                          display: "inline",
                          marginRight: "16px"
                        }}
                        level={4}
                      >
                        FAQ
                      </Title>
                    </a>
                    <Popover content={<ShareOptions />}>
                      <Button shape="round" className="header-button">
                        Tell friends
                      </Button>
                    </Popover>
                  </div>
                </Col>
              </Row>

              <Col
                xs={{ span: 18, offset: 3 }}
                span={16}
                offset={4}
                style={{ textAlign: "center", padding: "20px 0px" }}
              >
                <Title
                  level={1}
                  style={{ color: "white", textAlign: "center" }}
                >
                  Your favorite Toronto restaurant might close forever. Help
                  save it.
                </Title>
                <div className="header-sans">
                  Gift cards help "flatten the curve" of lost income from
                  COVID-19.
                </div>
              </Col>
              <Col sm={{ span: 20, offset: 2 }} lg={{ span: 20, offset: 2 }}>
                <div className="main-results">
                  <div className="neighborhood-card-container-outer">
                    <NeighborhoodCards />
                  </div>
                </div>
              </Col>
              <Row className="footer-content">
                <Col offset={2} xs={18} style={{ textAlign: "center" }}>
                  <Title level={3}>Our duty as loyal customers</Title>
                  <p>
                    Many businesses are in a difficult cash situation as social
                    isolation and quarantine has forced most people to stay in
                    their homes and non- essential businesses have closed their
                    doors. Gift cards keep income flowing to local restaurateurs
                    that are having to pay rent and other expenses while
                    businesses are closed.
                  </p>
                </Col>
              </Row>
            </div>
          </Row>
        </div>
      </div>
    );
  }
}

export default App;
