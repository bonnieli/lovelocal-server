import React, { useState, useEffect } from "react";
import { Typography, Button, Row, Spin } from "antd";
import PlaceCard from "./SuggestedPlaceCards";
import { DebounceInput } from "react-debounce-input";

const NeighborhoodCards = ({}) => {
  const perPage = 15;
  const [suggestedPlaces, setSuggestedPlaces] = useState([]);
  const [loading, setLoading] = useState(false);
  const [moreAvailable, setMoreAvailable] = useState(false);
  const [offset, setOffset] = useState(0);
  const [search, setSearch] = useState("");

  const searchChange = e => {
    const { value } = e.target;

    setOffset(0);
    setSuggestedPlaces([]);
    setSearch(value);
  };

  const getPlaces = async () => {
    const res = await fetch(
      `/api/places/by_neighborhood?offset=${offset}&search=${search}`
    );
    const data = await res.json();

    setLoading(false);

    console.log(data);
    setSuggestedPlaces(prevState => [...prevState, ...data.suggestedPlaces]);
    setMoreAvailable(data.moreAvailable);

    setOffset(prevState => prevState + perPage);
  };

  useEffect(() => {
    getPlaces();
  }, [search]);

  return (
    <>
      <DebounceInput
        minLength={2}
        debounceTimeout={800}
        onChange={searchChange}
        onKeyDown={e => {
          if (search !== e.target.value) setLoading(true);
        }}
        placeholder="Search Toronto's restaurants, coffee shops, etc."
        className="search-bar"
      />

      {loading && (
        <div
          className="loading-search"
          style={{ position: "absolute", top: 35, right: 35 }}
        >
          <Spin />
        </div>
      )}

      {suggestedPlaces && suggestedPlaces.length > 0 && (
        <div style={{ textAlign: "center" }}>
          <Row gutter={16} style={{ justifyContent: "center" }}>
            {suggestedPlaces.map(place => {
              return <PlaceCard place={place} />;
            })}
          </Row>

          {moreAvailable && !loading && (
            <Button
              className="primary-button"
              shape="round"
              size="default"
              onClick={getPlaces}
            >
              Load More
            </Button>
          )}

          {loading && <Spin />}
        </div>
      )}

      {suggestedPlaces && suggestedPlaces.length === 0 && <p>No results</p>}
    </>
  );
};

export default NeighborhoodCards;
