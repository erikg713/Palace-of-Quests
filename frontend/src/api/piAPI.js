import axios from 'axios';

// Helper function to authenticate with Pi SDK
export const authenticateUser = async () => {
  const scopes = ["username", "payments"];
  
  try {
    // Initiate Pi SDK authentication
    const authResult = await window.Pi.authenticate(scopes, onIncompletePaymentFound);
    await axios.post("/signin", { authResult });
    return authResult.user;
  } catch (error) {
    console.error("Authentication Error:", error);
    alert("Failed to authenticate with Pi Network.");
  }
};

// Handles incomplete payments found during authentication
const onIncompletePaymentFound = (payment) => {
  console.log("Incomplete Payment Found:", payment);
  return axios.post("/incomplete", { payment });
};
