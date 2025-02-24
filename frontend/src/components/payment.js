const axiosClient = axios.create({
    baseURL: 'https://api.example.com',
    headers: {
        'Content-Type': 'application/json'
    }
});

const paymentData = {
    amount: 123.45, // Amount being transacted
    memo: "Payment for services rendered",
    metadata: { specialInfo: 1234 }
};

// Callbacks implementation
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

// Registering the callbacks
const paymentCallbacks = {
    onReadyForServerApproval,
    onReadyForServerCompletion,
    onCancel,
    onError
};

// Creating the payment
Pi.createPayment(paymentData, paymentCallbacks)
    .then(payment => console.log('Payment:', payment))
    .catch(error => console.error('Payment Error:', error));
