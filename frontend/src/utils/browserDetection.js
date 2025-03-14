/**
 * Browser detection utility for cross-browser compatibility
 */

// Define browser detection variables first
export let browser = null;
export let crossbrowserName = null;
export let REMOTE_CONFIG_KEYS = {
  ENABLE_DOWNLOAD: 'enable_download',
  DEBUG_MODE: 'debug_mode'
};
export let webextApi = {};

/**
 * Determines the user's browser type and version
 * @returns {string} The detected browser name
 */
export function determineBrowser() {
  const userAgent = navigator.userAgent;
  
  // Detect Chrome
  if (userAgent.indexOf("Chrome") > -1) {
    browser = "chrome";
    crossbrowserName = "chrome";
    return "chrome";
  }
  // Detect Firefox
  else if (userAgent.indexOf("Firefox") > -1) {
    browser = "firefox";
    crossbrowserName = "firefox";
    return "firefox";
  }
  // Detect Safari
  else if (userAgent.indexOf("Safari") > -1) {
    browser = "safari";
    crossbrowserName = "safari";
    return "safari";
  }
  // Detect Edge
  else if (userAgent.indexOf("Edg") > -1) {
    browser = "edge";
    crossbrowserName = "edge";
    return "edge";
  }
  // Detect IE (not recommended for modern web apps)
  else if (userAgent.indexOf("MSIE") > -1 || !!document.documentMode) {
    browser = "ie";
    crossbrowserName = "ie";
    return "ie";
  }
  // Default to chrome-like behavior
  else {
    browser = "chrome";
    crossbrowserName = "chrome";
    return "chrome";
  }
}

/**
 * Initialize browser-related variables
 */
export function initBrowserVariables() {
  determineBrowser();
}

// Run initialization immediately
initBrowserVariables();

// Define a global window.browser and related variables to support legacy code
// This ensures variables are available globally across scripts
if (typeof window !== 'undefined') {
  window.browser = browser;
  window.crossbrowserName = crossbrowserName;
  window.REMOTE_CONFIG_KEYS = REMOTE_CONFIG_KEYS;
  window.webextApi = webextApi;
}

export default {
  browser,
  crossbrowserName,
  REMOTE_CONFIG_KEYS,
  webextApi,
  determineBrowser
};
