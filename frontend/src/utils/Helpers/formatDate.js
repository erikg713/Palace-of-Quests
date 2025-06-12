/**
 * Formats a given date into a readable string with specified options and locale.
 *
 * @param {string | Date} value - The date input to format. Can be a Date object or a date string.
 * @param {Intl.DateTimeFormatOptions} [options={ year: 'numeric', month: 'long', day: 'numeric' }] - Formatting options.
 * @param {string} [locale='en-US'] - Locale for formatting (e.g., 'en-US', 'fr-FR').
 * @returns {string} - Formatted date string. Returns an empty string if the input is invalid.
 *
 * @example
 * formatDate('2025-06-12'); // June 12, 2025
 * formatDate(new Date(), { month: 'short', day: 'numeric' }, 'en-GB'); // 12 Jun
 */
export function formatDate(
  value,
  options = { year: 'numeric', month: 'long', day: 'numeric' },
  locale = 'en-US'
) {
  try {
    if (!value) return '';
    const date = value instanceof Date ? value : new Date(value);

    if (isNaN(date.getTime())) {
      console.error('Invalid date input:', value);
      return '';
    }

    const formatter = new Intl.DateTimeFormat(locale, options);
    return formatter.format(date);
  } catch (error) {
    console.error('Error formatting date:', error);
    return '';
  }
}
