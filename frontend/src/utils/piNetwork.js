import axios from "axios";

// Use environment variable for backend URL, fallback to localhost for dev
const BASE_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000";

if (!process.env.REACT_APP_BACKEND_URL && process.env.NODE_ENV !== "development") {
  throw new Error("REACT_APP_BACKEND_URL is not defined in environment variables");
}

// Create a reusable Axios instance for all API calls
const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add interceptors for handling common scenarios
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      console.error("Unauthorized! Token may have expired.");
      // Optionally redirect to login or refresh token
    }
    return Promise.reject(error);
  }
);

/**
 * Sets Authorization header for API requests.
 * @param {string} token - JWT token for authentication.
 */
const setAuthHeader = (token) => {
  if (token) {
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  } else {
    delete api.defaults.headers.common["Authorization"];
  }
};

/**
 * Handles API errors and provides detailed messages.
 * @param {object} error - Axios error object.
 * @throws {Error} - Standardized error with status code and message.
 */
const handleApiError = (error) => {
  const status = error?.response?.status;
  const msg =
    error?.response?.data?.message ||
    error?.response?.data?.error ||
    error?.message ||
    "An unknown error occurred";

  if (process.env.NODE_ENV === "development") {
    console.error(`Error [${status}]:`, error);
  } else {
    console.error(`Error [${status}]: ${msg}`);
  }
  throw new Error(`Error [${status}]: ${msg}`);
};

/**
 * Wrapper for API calls with automatic token management.
 * @param {string} method - HTTP method (e.g., 'post').
 * @param {string} url - API endpoint.
 * @param {object} data - Request payload (default: {}).
 * @param {string} token - JWT token for authentication.
 * @returns {Promise<object>} - Response data from the server.
 */
const withAuth = (method, url, data = {}, token) => {
  setAuthHeader(token);
  return api[method](url, data).then((res) => res.data).catch(handleApiError);
};

/**
 * Initiates a subscription payment for the authenticated user.
 * @param {string} token - JWT authentication token.
 * @returns {Promise<object>} - Response data from server.
 */
export const initiateSubscription = (token) => withAuth("post", "/payment/subscribe", {}, token);

/**
 * Verifies a payment using its ID for the authenticated user.
 * @param {string} paymentId - Payment identifier.
 * @param {string} token - JWT authentication token.
 * @returns {Promise<object>} - Response data from server.
 */
export const verifyPayment = (paymentId, token) =>
  withAuth("post", "/payment/verify", { payment_id: paymentId }, token);
