import axios from "axios";

// Use environment variable for backend URL, fallback to localhost for development
const BASE_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000";

if (!process.env.REACT_APP_BACKEND_URL && process.env.NODE_ENV !== "development") {
  console.warn("REACT_APP_BACKEND_URL is not defined. Using localhost for development.");
}

// Create Axios instance
const api = axios.create({
  baseURL: BASE_URL,
  headers: { "Content-Type": "application/json" },
});

// Centralized error handler for API responses
const handleApiError = (error) => {
  const status = error?.response?.status;
  const message =
    error?.response?.data?.message ||
    error?.response?.data?.error ||
    error?.message ||
    "An unknown error occurred";

  if (process.env.NODE_ENV === "development") {
    console.error(`Error [${status}]:`, error);
  } else {
    console.error(`Error [${status}]: ${message}`);
  }
  throw new Error(`Error [${status}]: ${message}`);
};

/**
 * Generic API call utility
 * @param {string} method - HTTP method ('post', 'get', etc.)
 * @param {string} url - API endpoint
 * @param {object} [data] - Payload for POST/PUT
 * @returns {Promise<object>} - Server response data
 */
const callApi = async (method, url, data = {}) => {
  try {
    const response = await api[method](url, data);
    return response.data;
  } catch (error) {
    handleApiError(error);
  }
};

/**
 * Initiate a Pi Network subscription payment.
 * @returns {Promise<object>} - Payment initiation response
 */
export const initiateSubscription = async () => {
  return callApi("post", "/payment/subscribe");
};

/**
 * Verify a Pi Network payment by its ID.
 * @param {string} paymentId - The Pi payment ID
 * @returns {Promise<object>} - Verification response
 */
export const verifyPayment = async (paymentId) => {
  return callApi("post", "/payment/verify", { payment_id: paymentId });
};
