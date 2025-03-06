/**
 * Form validation utility functions for CV form components
 */

/**
 * Validates an email address
 * @param {string} email - The email to validate
 * @returns {boolean} - Whether the email is valid
 */
export const isValidEmail = (email) => {
  if (!email) return false;
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

/**
 * Validates a phone number (basic validation)
 * @param {string} phone - The phone number to validate
 * @returns {boolean} - Whether the phone number is valid
 */
export const isValidPhone = (phone) => {
  if (!phone) return false;
  // Allow digits, spaces, parentheses, hyphens, and plus sign
  const phoneRegex = /^[+]?[(]?[0-9]{1,4}[)]?[-\s./0-9]*$/;
  return phoneRegex.test(phone) && phone.replace(/\D/g, '').length >= 7;
};

/**
 * Validates a URL
 * @param {string} url - The URL to validate
 * @returns {boolean} - Whether the URL is valid
 */
export const isValidUrl = (url) => {
  if (!url) return true; // URLs are often optional
  try {
    new URL(url);
    return true;
  } catch (e) {
    return false;
  }
};

/**
 * Checks if a string is empty or only contains whitespace
 * @param {string} value - The string to check
 * @returns {boolean} - Whether the string is empty or only whitespace
 */
export const isEmpty = (value) => {
  return value === null || value === undefined || value.trim() === '';
};

/**
 * Validates personal information form data
 * @param {Object} data - The personal information form data
 * @returns {Object} - Validation result with isValid flag and errors object
 */
export const validatePersonalInfo = (data) => {
  const errors = {};
  
  if (isEmpty(data.firstName)) {
    errors.firstName = 'First name is required';
  }
  
  if (isEmpty(data.lastName)) {
    errors.lastName = 'Last name is required';
  }
  
  if (isEmpty(data.email)) {
    errors.email = 'Email is required';
  } else if (!isValidEmail(data.email)) {
    errors.email = 'Please enter a valid email address';
  }
  
  if (!isEmpty(data.phone) && !isValidPhone(data.phone)) {
    errors.phone = 'Please enter a valid phone number';
  }
  
  if (isEmpty(data.jobTitle)) {
    errors.jobTitle = 'Job title is required';
  }
  
  return {
    isValid: Object.keys(errors).length === 0,
    errors
  };
};

/**
 * Validates work experience block data
 * @param {Object} data - The work experience block data
 * @returns {Object} - Validation result with isValid flag and errors object
 */
export const validateWorkExperience = (data) => {
  const errors = {};
  
  if (isEmpty(data.title)) {
    errors.title = 'Job title is required';
  }
  
  if (isEmpty(data.company)) {
    errors.company = 'Company name is required';
  }
  
  if (isEmpty(data.startDate)) {
    errors.startDate = 'Start date is required';
  }
  
  return {
    isValid: Object.keys(errors).length === 0,
    errors
  };
};

/**
 * Validates education block data
 * @param {Object} data - The education block data
 * @returns {Object} - Validation result with isValid flag and errors object
 */
export const validateEducation = (data) => {
  const errors = {};
  
  if (isEmpty(data.degree)) {
    errors.degree = 'Degree is required';
  }
  
  if (isEmpty(data.institution)) {
    errors.institution = 'Institution name is required';
  }
  
  return {
    isValid: Object.keys(errors).length === 0,
    errors
  };
};

/**
 * Sanitizes user input to prevent XSS attacks
 * @param {string} input - The user input to sanitize
 * @returns {string} - The sanitized input
 */
export const sanitizeInput = (input) => {
  if (!input) return '';
  return input
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
};
