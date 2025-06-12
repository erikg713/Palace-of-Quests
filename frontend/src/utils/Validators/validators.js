// Utility Validators

/**
 * Validates if the given string is a valid email address.
 * 
 * @param {string} email - The email address to validate.
 * @returns {boolean} - Returns true if valid, otherwise false.
 */
export const isValidEmail = (email) => {
  if (typeof email !== 'string') {
    console.error('Invalid input: Email must be a string');
    return false;
  }

  // Updated regex for improved email validation
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return regex.test(email);
};
