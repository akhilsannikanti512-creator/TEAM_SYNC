import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  FaUserGraduate,
  FaUsers,
  FaUserFriends,
  FaTrashAlt,
} from "react-icons/fa";

import api from "../services/api";
import StatCard from "../components/cards/StatCard";

import "../styles/Dashboard.css";

function Dashboard() {

  const navigate = useNavigate();

  const [stats, setStats] = useState({
    total_students: 0,
    total_teams: 0,
    total_team_members: 0,
  });

  useEffect(() => {
    fetchDashboard();
  }, []);

  // ==========================
  // Dashboard Data
  // ==========================
  const fetchDashboard = async () => {

    try {

      const token = localStorage.getItem("token");

      const response = await api.get("/dashboard/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setStats(response.data);

    } catch (error) {

      console.error(error);

      if (error.response?.status === 401) {
        localStorage.removeItem("token");
        navigate("/");
      }

    }

  };

  // ==========================
  // Reset Project
  // ==========================
  const resetProject = async () => {

    const confirmReset = window.confirm(
      "⚠️ This will delete all Students, Teams and Team Members.\n\nDo you want to continue?"
    );

    if (!confirmReset) return;

    try {

      const token = localStorage.getItem("token");

      await api.delete("/teams/reset", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      alert("✅ Project reset successfully!");

      fetchDashboard();

    } catch (error) {

      console.error(error);

      alert("❌ Failed to reset project.");

    }

  };

  return (
    <div className="dashboard-page">

      <div className="dashboard-header">

        <div>
          <h1>Dashboard</h1>
          <p>Welcome back, Admin</p>
        </div>

        <button
          className="reset-btn"
          onClick={resetProject}
        >
          <FaTrashAlt />
          Reset Project
        </button>

      </div>

      <div className="dashboard-cards">

        <StatCard
          title="Total Students"
          value={stats.total_students}
          icon={<FaUserGraduate />}
          color="#2563eb"
        />

        <StatCard
          title="Total Teams"
          value={stats.total_teams}
          icon={<FaUsers />}
          color="#10b981"
        />

        <StatCard
          title="Team Members"
          value={stats.total_team_members}
          icon={<FaUserFriends />}
          color="#ef4444"
        />

      </div>

    </div>
  );
}

export default Dashboard;