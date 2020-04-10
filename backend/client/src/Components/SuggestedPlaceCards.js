import React from "react";
import { Button, Row, Col } from "antd";
import {
  GiftTwoTone,
  ShopTwoTone,
  ShoppingTwoTone,
  InstagramOutlined,
} from "@ant-design/icons";
import { Mixpanel } from "../lib/Mixpanel";

const PlaceCard = ({ place }) => {
  const onClickBuy = () => {
    Mixpanel.track("Clicked Buy Gift Card", place);
  };

  const onClickWebsite = () => {
    Mixpanel.track("Clicked Visit Website", place);
  };

  const onClickShop = () => {
    Mixpanel.track("Clicked Visit Shop", place);
  };

  const onClickInstagram = () => {
    Mixpanel.track("Clicked Visit Instagram", place);
  };

  let website = place.website;

  if (website && !website.includes("www")) {
    website = `https://www.${website}`;
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
          <h3>{place.name}</h3>
          <div>
            {place.giftCardURL && (
              <Button
                href={place.giftCardURL}
                onClick={onClickBuy}
                target="_blank"
                style={{ margin: `5px 10px` }}
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
                style={{ margin: `5px 10px` }}
              >
                <ShopTwoTone twoToneColor="#00796f" />
                Website
              </Button>
            )}

            {place.shopURL && (
              <Button
                href={`${place.shopURL}`}
                onClick={onClickShop}
                target="_blank"
                style={{ margin: `5px 10px` }}
              >
                <ShoppingTwoTone twoToneColor="#00796f" />
                Shop
              </Button>
            )}

            {place.igHandle && (
              <Button
                href={`https://instagram.com/${place.igHandle}`}
                onClick={onClickInstagram}
                target="_blank"
                style={{ margin: `5px 10px`, color: "#00796f" }}
              >
                <InstagramOutlined />
                Shop
              </Button>
            )}
          </div>
        </Col>
      </Row>
    </Col>
  );
};

export default PlaceCard;
