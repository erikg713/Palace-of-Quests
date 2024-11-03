import React, { useState } from "react";
import axios from "axios";

const signIn = async () => {
  const scopes = ["username", "payments"];
  const authResponse = await window.Pi.authenticate(scopes, onIncompletePaymentFound);

  // Send auth data to the backend for verification
  await axios.post("/signin", { authResult: authResponse });
};

const onIncompletePaymentFound = (payment) => {
  console.log("Incomplete Payment Found:", payment);
  axios.post("/incomplete", { payment });
};

const Shop = () => {
  return (
    <div>
      <button onClick={signIn}>Sign In with Pi</button>
    </div>
  );
};

export default Shop;
