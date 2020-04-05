import React from "react";
import { Button, Row, Col } from "antd";
import { Mixpanel } from "../lib/Mixpanel";

const PlaceCard = ({ place }) => {
  const onClickBuy = () => {
    Mixpanel.track("Clicked Buy Gift Card", place);
  };

  return (
    <Col xs={24} sm={12}>
      <Row className="place-card">
        <Col xs={8} className="place-container">
          <div
            className="place-image"
            style={{
              backgroundImage: "url(" + place.imageURL + ")"
            }}
          ></div>
        </Col>
        <Col xs={16} style={{ paddingLeft: 10 }}>
          <h3>{place.placeID}</h3>
          <div>
            {place.giftCardURL && (
              <Button
                href={place.giftCardURL}
                onClick={onClickBuy}
                target="_blank"
              >
                Buy Gift Card
              </Button>
            )}
          </div>
        </Col>
      </Row>
    </Col>
  );
};

export default PlaceCard;
