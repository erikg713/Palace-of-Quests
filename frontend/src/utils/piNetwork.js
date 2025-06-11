import axios from "axios";

// Use environment variable for backend URL, fallback to localhost for dev
const BASE_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000";

// Create a reusable Axios instance for all API calls
const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json"
  }
});

/**
 * Attach Authorization header to the Axios instance.
 * @param {string} token - JWT authentication token
 */
const setAuthHeader = (token) => {
  if (token) {
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  } else {
    delete api.defaults.headers.common["Authorization"];
  }
};

/**
 * Standardized error handler for API requests.
 * @param {object} error - Axios error object
 * @throws {Error}
 */
const handleApiError = (error) => {
  // Fallbacks in case response/data/message are missing
  const msg =
    error?.response?.data?.message ||
    error?.response?.data?.error ||
    error?.message ||
    "An unknown error occurred";
  // Avoid leaking sensitive details in production logs
  if (process.env.NODE_ENV === "development") {
    // Only log stack in development
    console.error(error);
  } else {
    console.error(msg);
  }
  throw new Error(msg);
};

/**
 * Initiates a subscription payment for the authenticated user.
 * @param {string} token - JWT authentication token
 * @returns {Promise<object>} - Response data from server
 */
export const initiateSubscription = async (token) => {
  setAuthHeader(token);
  try {
    const res = await api.post("/payment/subscribe");
    return res.data;
  } catch (err) {
    handleApiError(err);
  }
};

/**
 * Verifies a payment using its ID for the authenticated user.
 * @param {string} paymentId - Payment identifier
 * @param {string} token - JWT authentication token
 * @returns {Promise<object>} - Response data from server
 */
export const verifyPayment = async (paymentId, token) => {
  setAuthHeader(token);
  try {
    const res = await api.post("/payment/verify", { payment_id: paymentId });
    return res.data;
  } catch (err) {
    handleApiError(err);
  }
};
