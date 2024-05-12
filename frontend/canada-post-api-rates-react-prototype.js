import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CanadaPostApiRatesReactPrototype = () => {
  const [rates, setRates] = useState([]);

  useEffect(() => {
    axios.post('/api/rates')
    .then(response => {
        setRates(response.data);
      })
    .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      {rates.map((rate, index) => (
        <div key={index}>
          <p>Service: {rate.service_name} ({rate.service_code})</p>
          <p>Price: {rate.price}</p>
          <p>Estimated Delivery Date: {rate.estimated_delivery_date}</p>
        </div>
      ))}
    </div>
  );
};

export default CanadaPostApiRatesReactPrototype;


/*
This is a react prototype so you still need to update the following
in the index.js
import React from 'react';
import ReactDOM from 'react-dom';
import CanadaPostApiRatesReactPrototype from './CanadaPostApiRatesReactPrototype';

ReactDOM.render(
  <React.StrictMode>
    <CanadaPostApiRatesReactPrototype />
  </React.StrictMode>,
  document.getElementById('root')
);

*/