import { Navigate } from "react-router-dom";

function PrivateRoute({ children }) {
  const isAuthenticated = !!localStorage.getItem("token"); // or however you store auth
  return isAuthenticated ? children : <Navigate to="/login" replace />;
}

export default PrivateRoute;
