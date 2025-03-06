/**
 * Globals initialization script
 * 
 * This file ensures that all global variables required by external scripts
 * are properly defined before those scripts are executed.
 */

// Define all required globals to prevent reference errors
window.browser = window.browser || 'chrome';
window.crossbrowserName = window.crossbrowserName || 'chrome';
window.REMOTE_CONFIG_KEYS = window.REMOTE_CONFIG_KEYS || {
  ENABLE_DOWNLOAD: 'enable_download',
  DEBUG_MODE: 'debug_mode'
};
window.webextApi = window.webextApi || {
  download: (options) => {
    console.log('Download requested:', options);
    return true;
  }
};

export default {
  // Exported for reference but primarily intended for global use
  browser: window.browser,
  crossbrowserName: window.crossbrowserName,
  REMOTE_CONFIG_KEYS: window.REMOTE_CONFIG_KEYS,
  webextApi: window.webextApi
};
