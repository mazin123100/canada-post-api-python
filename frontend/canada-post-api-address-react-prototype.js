import React, { useState } from 'eact';

const CanadaPostApiAddressPrototype = () => {
  const [addressInput, setAddressInput] = useState('');
  const [addressData, setAddressData] = useState(null);
  const [errorMessage, setErrorMessage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setErrorMessage(null);
    setAddressData(null);
    try {
      const response = await fetch('/complete_address/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ address: addressInput }),
      });
      const data = await response.json();
      setAddressData(data);
    } catch (error) {
      setErrorMessage(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={addressInput}
        onChange={(event) => setAddressInput(event.target.value)}
        placeholder="Enter address"
      />
      <button type="submit">Get Address</button>
      {loading? <div>Loading...</div> : null}
      {addressData? (
        <div>
          <h2>Address Data:</h2>
          <pre>{JSON.stringify(addressData, null, 2)}</pre>
        </div>
      ) : null}
      {errorMessage? (
        <div>
          <h2>Error:</h2>
          <p>{errorMessage}</p>
        </div>
      ) : null}
    </form>
  );
};

export default CanadaPostApiAddressPrototype;


/* This is a react prototype so you still need to update the following
  import React from 'react';
  import CanadaPostApiAddressPrototype from './CanadaPostApiAddressPrototype';

  const App = () => {
    return (
      <div>
        <CanadaPostApiAddressPrototype />
      </div>
    );
  };

  export default App;


// update the index.js file to render the App component:
import React from 'eact';
import ReactDOM from 'eact-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

   that spans multiple lines */