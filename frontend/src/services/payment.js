// src/services/payment.js

const axios = require('axios');
// payment.js
document.getElementById("payBtn").addEventListener("click", initiateA2UPayment);

// Configure Axios client
const axiosClient = axios.create({
    baseURL: process.env.API_BASE_URL || 'https://api.example.com',
    headers: {
        'Content-Type': 'application/json',
    },
});

/**
 * Logs and throws an error.
 * @param {Error} error - Error object.
 */
const handleError = (error) => {
    console.error('Error:', error.message, error.response?.data || '');
    throw error;
};

/**
 * Approves payment on the server.
 * @param {string} paymentId - Payment ID.
 */
const onReadyForServerApproval = async (paymentId) => {
    console.log('onReadyForServerApproval', paymentId);
    try {
        const response = await axiosClient.post('/payments/approve', { paymentId });
        console.log('Approved:', response.data);
    } catch (error) {
        handleError(error);
    }
};

/**
 * Completes payment on the server.
 * @param {string} paymentId - Payment ID.
 * @param {string} txid - Transaction ID.
 */
const onReadyForServerCompletion = async (paymentId, txid) => {
    console.log('onReadyForServerCompletion', paymentId, txid);
    try {
        const response = await axiosClient.post('/payments/complete', { paymentId, txid });
        console.log('Completed:', response.data);
    } catch (error) {
        handleError(error);
    }
};

/**
 * Logs payment cancellation.
 */
const onCancel = () => {
    console.log('Payment cancelled');
};

/**
 * Logs payment error.
 * @param {Error} error - Error object.
 */
const onError = (error) => {
    console.error('Payment error:', error.message);
};

// Payment callbacks
const paymentCallbacks = {
    onReadyForServerApproval,
    onReadyForServerCompletion,
    onCancel,
    onError,
};

/**
 * Creates a new payment.
 * @param {Object} Pi - Payment interface.
 * @param {number} amount - Payment amount.
 * @param {string} memo - Payment memo.
 * @param {Object} metadata - Additional payment metadata.
 */
const createPayment = async (Pi, amount, memo, metadata) => {
    const paymentData = { amount, memo, metadata };
    try {
        const payment = await Pi.createPayment(paymentData, paymentCallbacks);
        console.log('Payment:', payment);
    } catch (error) {
        handleError(error);
    }
};

module.exports = { createPayment, onReadyForServerApproval, onReadyForServerCompletion, onCancel, onError };
