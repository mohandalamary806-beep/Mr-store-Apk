import { GoogleAuth } from '@codetrix-studio/capacitor-google-auth';

// Google Sign-In on Android must request the ID token for the Web OAuth client.
// The Android OAuth client remains registered in Google Cloud with package + SHA-1.
const MR_STORE_WEB_CLIENT_ID =
  '443646227114-vbstcio2leo5l5ene86mtmd9cv6djdln.apps.googleusercontent.com';

try {
  const initResult = GoogleAuth.initialize({
    clientId: MR_STORE_WEB_CLIENT_ID,
    scopes: ['profile', 'email'],
    // MR Store only needs the ID token in the app; no server auth-code flow.
    grantOfflineAccess: false,
  });

  if (initResult && typeof initResult.catch === 'function') {
    initResult.catch((error) => {
      console.error('MR Store Google Auth initialization failed:', error);
    });
  }
} catch (error) {
  console.error('MR Store Google Auth initialization failed:', error);
}

window.MRGoogleAuth = GoogleAuth;
