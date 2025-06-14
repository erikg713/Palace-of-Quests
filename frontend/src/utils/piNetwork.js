import axios from "axios";

// Use environment variable for backend URL, fallback to localhost for dev
const BASE_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000";

if (!process.env.REACT_APP_BACKEND_URL && process.env.NODE_ENV !== "development") {
  throw new Error("REACT_APP_BACKEND_URL is not defined in environment variables");
}

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
    // eslint-disable-next-line no-console
    console.error(`Error [${status}]:`, error);
  } else {
    // eslint-disable-next-line no-console
    console.error(`Error [${status}]: ${message}`);
  }
  throw new Error(`Error [${status}]: ${message}`);
};

/**
 * Generic API call utility (no authentication required)
 * @param {string} method - HTTP method ('post', 'get', etc.)
 * @param {string} url - API endpoint
 * @param {object} [data] - Payload for POST/PUT
 * @returns {Promise<object>} - Server response data
 */
const callApi = (method, url, data = {}) =>
  api[method](url, data).then((res) => res.data).catch(handleApiError);

/**
 * Initiate a Pi Network subscription payment.
 * @returns {Promise<object>} - Payment initiation response
 */
export const initiateSubscription = () => callApi("post", "/payment/subscribe");

/**
 * Verify a Pi Network payment by its ID.
 * @param {string} paymentId - The Pi payment ID
 * @returns {Promise<object>} - Verification response
 */
export const verifyPayment = (paymentId) =>
  callApi("post", "/payment/verify", { payment_id: paymentId });

import axios from "axios";

const BASE_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000";
const api = axios.create({
  baseURL: BASE_URL,
  headers: { "Content-Type": "application/json" }
});

const handleApiError = (error) => {
  const msg =
    error?.response?.data?.message ||
    error?.response?.data?.error ||
    error?.message ||
    "An unknown error occurred";
  if (process.env.NODE_ENV === "development") {
    console.error(error);
  } else {
    console.error(msg);
  }
  throw new Error(msg);
};

export const initiateSubscription = async () => {
  try {
    const res = await api.post("/payment/subscribe");
    return res.data;
  } catch (err) {
    handleApiError(err);
  }
};

export const verifyPayment = async (paymentId) => {
  try {
    const res = await api.post("/payment/verify", { payment_id: paymentId });
    return res.data;
  } catch (err) {
    handleApiError(err);
  }
};
import axios from "axios";

// Use environment variable for backend URL, fallback to localhost for development
const BASE_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000";

if (!process.env.REACT_APP_BACKEND_URL && process.env.NODE_ENV !== "development") {
  console.warn("REACT_APP_BACKEND_URL is not defined. Using localhost for development.");
}

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
export const initiateSubscription = () => callApi("post", "/payment/subscribe");

/**
 * Verify a Pi Network payment by its ID.
 * @param {string} paymentId - The Pi payment ID
 * @returns {Promise<object>} - Verification response
 */
export const verifyPayment = (paymentId) => callApi("post", "/payment/verify", { payment_id: paymentId });
