// src/components/Payment.js
import React from 'react';
import { Pi } from 'pi-network-sdk'; // Replace with actual import method if different
import { createPayment } from '../services/paymentProcessing';

const Payment = () => {
    const handlePayment = () => {
        createPayment(Pi);
    };

    return (
        <div>
            <button onClick={handlePayment}>Make Payment</button>
        </div>
    );
};

export default Payment;
