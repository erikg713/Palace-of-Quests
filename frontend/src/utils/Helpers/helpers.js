/**
 * Converts an input date value to a formatted date string.
 * If the input is invalid or missing, returns an empty string.
 *
 * @param {string|Date} value - The date input to format.
 * @param {Object} options - Intl.DateTimeFormat options.
 * @param {string} locale - BCP 47 language tag.
 * @returns {string} Formatted date string or empty string for invalid input.
 */
export function formatDate(
  value,
  options = { year: 'numeric', month: 'long', day: 'numeric' },
  locale = 'en-US'
) {
  if (!value) return '';
  const date = value instanceof Date ? value : new Date(value);
  if (isNaN(date.getTime())) return '';
  return date.toLocaleDateString(locale, options);
}
