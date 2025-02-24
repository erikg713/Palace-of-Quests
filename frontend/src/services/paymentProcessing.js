// src/services/paymentProcessing.js

const axios = require('axios');

// Define axios client
const axiosClient = axios.create({
    baseURL: 'https://api.example.com', // Replace with your actual API base URL
    headers: {
        'Content-Type': 'application/json'
    }
});

// Define payment data and callbacks
const paymentData = {
    amount: 123.45, // Amount being transacted
    memo: "Payment for services rendered",
    metadata: { specialInfo: 1234 }
};

const onReadyForServerApproval = (paymentId) => {
    console.log("onReadyForServerApproval", paymentId);
    axiosClient.post('/payments/approve', { paymentId })
        .then(response => console.log('Approved:', response))
        .catch(error => console.error('Approval Error:', error));
};

const onReadyForServerCompletion = (paymentId, txid) => {
    console.log("onReadyForServerCompletion", paymentId, txid);
    axiosClient.post('/payments/complete', { paymentId, txid })
        .then(response => console.log('Completed:', response))
        .catch(error => console.error('Completion Error:', error));
};

const onCancel = () => {
    console.log("Payment cancelled");
};

const onError = (error) => {
    console.error("Payment error", error);
};

// Register callbacks
const paymentCallbacks = {
    onReadyForServerApproval,
    onReadyForServerCompletion,
    onCancel,
    onError
};

// Create payment function
const createPayment = (Pi) => {
    Pi.createPayment(paymentData, paymentCallbacks)
        .then(payment => console.log('Payment:', payment))
        .catch(error => console.error('Payment Error:', error));
};

module.exports = { createPayment };
