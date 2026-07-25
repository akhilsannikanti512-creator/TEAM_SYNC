import { NavLink, useNavigate } from "react-router-dom";
import {
  FaHome,
  FaUserGraduate,
  FaUsers,
  FaLayerGroup,
  FaFileImport,
  FaFileExport,
  FaSignOutAlt,
} from "react-icons/fa";

import "../styles/Sidebar.css";

function Sidebar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <div className="sidebar">

      <div className="logo">
        <h2>TeamSync</h2>
        <p>Automated Team Allocation</p>
      </div>

      <nav>

        <NavLink to="/dashboard" className="nav-item">
          <FaHome />
          <span>Dashboard</span>
        </NavLink>

        <NavLink to="/students" className="nav-item">
          <FaUserGraduate />
          <span>Students</span>
        </NavLink>

        <NavLink to="/teams" className="nav-item">
          <FaUsers />
          <span>Teams</span>
        </NavLink>

        <NavLink to="/csv" className="nav-item">
          <FaFileImport />
          <span>CSV Import</span>
        </NavLink>

        <NavLink to="/export" className="nav-item">
          <FaFileExport />
          <span>Export</span>
        </NavLink>

      </nav>

      <div className="logout">
        <button
          className="logout-btn"
          onClick={handleLogout}
        >
          <FaSignOutAlt />
          <span>Logout</span>
        </button>
      </div>

    </div>
  );
}

export default Sidebar;