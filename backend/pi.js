import { Pi } from 'pi-backend';

const pi = new Pi({
  apiKey: process.env.PI_API_KEY,
  apiSecret: process.env.PI_API_SECRET,
  sandbox: process.env.PI_SANDBOX === "true"
});

// Verify frontend-signed payment and approve
export async function approvePayment(paymentData) {
  // Validate paymentData using Pi SDK
  const { paymentId } = paymentData;
  const payment = await pi.getPayment(paymentId);

  // Perform your own business logic checks here (optional)
  if (payment.status !== "INCOMPLETE") {
    throw new Error("Payment is not in an incomplete state.");
  }

  // Optionally: check metadata, user, etc.

  await pi.approvePayment(paymentId);
  return payment;
}

// Complete payment after blockchain confirmation
export async function completePayment(paymentId, txid) {
  // Confirm txid is valid and matches payment
  await pi.completePayment(paymentId, txid);
}

export async function getPayment(paymentId) {
  return await pi.getPayment(paymentId);
}
