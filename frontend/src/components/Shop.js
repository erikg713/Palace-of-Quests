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
const orderProduct = async (memo, amount, paymentMetadata) => {
  const paymentData = { amount, memo, metadata: paymentMetadata };
  const callbacks = {
    onReadyForServerApproval,
    onReadyForServerCompletion,
    onCancel,
    onError,
  };

  await window.Pi.createPayment(paymentData, callbacks);
};

const onReadyForServerApproval = (paymentId) => {
  console.log("Approving Payment:", paymentId);
  axios.post("/approve", { paymentId });
};

const onReadyForServerCompletion = (paymentId, txid) => {
  console.log("Completing Payment:", paymentId, txid);
  axios.post("/complete", { paymentId, txid });
};

const onCancel = (paymentId) => {
  console.log("Payment Canceled:", paymentId);
  axios.post("/cancelled_payment", { paymentId });
};

const onError = (error, payment) => {
  console.error("Payment Error:", error);
  if (payment) {
    console.log("Error Details:", payment);
  }
};
