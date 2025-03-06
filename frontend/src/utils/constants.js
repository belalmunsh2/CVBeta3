/**
 * Global constants for the application
 */

import { crossbrowserName } from './browserDetection';

// Browser-related constants
export const BROWSER_CONFIG = {
  isChrome: crossbrowserName === 'chrome',
  isSafari: crossbrowserName === 'safari',
  isFirefox: crossbrowserName === 'firefox',
  isEdge: crossbrowserName === 'edge'
};

// Feature flags
export const FEATURES = {
  ENABLE_ANALYTICS: true,
  ENABLE_SOCIAL_SHARING: true
};

// API endpoints configuration
export const API_CONFIG = {
  RETRY_ATTEMPTS: 3,
  TIMEOUT_MS: 10000
};

export default {
  BROWSER_CONFIG,
  FEATURES,
  API_CONFIG
};
