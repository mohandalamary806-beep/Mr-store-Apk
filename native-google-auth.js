import { GoogleAuth } from '@codetrix-studio/capacitor-google-auth';
try { GoogleAuth.initialize({ scopes: ['profile', 'email'], grantOfflineAccess: true }); } catch (error) { console.warn('Google Auth initialization:', error); }
window.MRGoogleAuth = GoogleAuth;
