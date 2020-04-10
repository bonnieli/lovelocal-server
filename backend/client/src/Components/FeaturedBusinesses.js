import React, { useState, useEffect } from "react";
import { Button, Row, Spin, Typography } from "antd";
import PlaceCard from "./SuggestedPlaceCards";

const { Title } = Typography;

const FeaturedBusinesses = ({}) => {
  const [businesses, setBusinesses] = useState([]);
  const [loading, setLoading] = useState(true);
  const getFeaturedBusinesses = async () => {
    const res = await fetch(`/api/places/featured_businesses`);
    const data = await res.json();

    setLoading(false);
    setBusinesses(data.featuredBusinesses);
  };

  useEffect(() => {
    getFeaturedBusinesses();
  }, []);

  return (
    <>
      <Title level={4} style={{ textAlign: "center" }}>
        Check out this business
      </Title>
      {loading && (
        <div
          className="loading-search"
          style={{ position: "absolute", top: 35, right: 35 }}
        >
          <Spin />
        </div>
      )}

      {businesses && businesses.length > 0 && (
        <div style={{ textAlign: "center" }}>
          <Row gutter={16} style={{ justifyContent: "center" }}>
            {businesses.map((place) => {
              return <PlaceCard place={place} />;
            })}
          </Row>

          {loading && <Spin />}
        </div>
      )}
    </>
  );
};

export default FeaturedBusinesses;
