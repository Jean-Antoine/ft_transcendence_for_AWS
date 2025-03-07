import { loadUserProfile } from "./actions/profile.js";
import { send2faEmail } from "./actions/validate2faEmail.js";
import { loadQRCode } from "./actions/validate2faApp.js";
import { loadUserStats } from "./actions/dashboard.js";

// Table de routage : associe chaque route à sa fonction d'initialisation
export const onRouteLoad = {
  profile: loadUserProfile,
  validation2faEmail: send2faEmail,
  validation2faApp: loadQRCode,
  dashboard: loadUserStats,
};

export default onRouteLoad;
