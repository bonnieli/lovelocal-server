import React from "react";
import { Button, Row, Col } from "antd";
import { GiftTwoTone, ShopTwoTone } from "@ant-design/icons";
import { Mixpanel } from "../lib/Mixpanel";

const PlaceCard = ({ place }) => {
  const onClickBuy = () => {
    Mixpanel.track("Clicked Buy Gift Card", place);
  };

  const onClickWebsite = () => {
    Mixpanel.track("Clicked Visit Website", place);
  };

  let website = place.website;

  if (website && !website.includes("www")) {
    website = `http://www.${website}`;
  }

  return (
    <Col xs={24} sm={12}>
      <Row className="place-card">
        <Col xs={8} className="place-container">
          <div
            className="place-image"
            style={{
              backgroundImage: "url(" + place.imageURL + ")",
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
                <GiftTwoTone twoToneColor="#009b8e" />
                Buy Gift Card
              </Button>
            )}

            {place.website && (
              <Button
                href={`${website}`}
                onClick={onClickWebsite}
                target="_blank"
                style={{ margin: 10 }}
              >
                <ShopTwoTone twoToneColor="#00796f" />
                Website
              </Button>
            )}
          </div>
        </Col>
      </Row>
    </Col>
  );
};

export default PlaceCard;
