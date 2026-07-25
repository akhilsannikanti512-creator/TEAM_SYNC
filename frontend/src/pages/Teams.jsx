import { useEffect, useState } from "react";
import { toast } from "react-hot-toast";

import api from "../services/api";
import TeamToolbar from "../components/team/TeamToolbar";
import TeamTable from "../components/team/TeamTable";

import "../styles/Teams.css";

function Teams() {
  const [teams, setTeams] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchTeams();
  }, []);

  // ==========================
  // Fetch Teams
  // ==========================
  const fetchTeams = async () => {
    try {
      const token = localStorage.getItem("token");

      const response = await api.get("/teams/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      setTeams(response.data);
    } catch (error) {
      console.error(error);
      toast.error("Failed to load teams");
    }
  };

  // ==========================
  // Generate Teams
  // ==========================
  const generateTeams = async () => {
    try {
      setLoading(true);

      const token = localStorage.getItem("token");

      await api.post(
        "/teams/generate",
        {},
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      toast.success("Teams generated successfully!");

      fetchTeams();

    } catch (error) {

      console.error(error);

      toast.error(
        error.response?.data?.detail || "Failed to generate teams"
      );

    } finally {

      setLoading(false);

    }
  };

  // ==========================
  // Search
  // ==========================
  const filteredTeams = teams.filter(
    (team) =>
      team.team_name.toLowerCase().includes(search.toLowerCase()) ||
      team.members.some((member) =>
        member.name.toLowerCase().includes(search.toLowerCase())
      )
  );

  return (
    <div className="teams-container">

      <h1>Teams</h1>

      <TeamToolbar
        search={search}
        setSearch={setSearch}
        onGenerate={generateTeams}
        loading={loading}
      />

      {filteredTeams.length > 0 ? (
        filteredTeams.map((team, index) => (
          <TeamTable
            key={team.id}
            team={team}
            teamNumber={index + 1}
          />
        ))
      ) : (
        <div
          style={{
            textAlign: "center",
            marginTop: "60px",
            color: "#6b7280",
          }}
        >
          <h2>No Teams Generated</h2>
          <p>
            Click the <strong>Generate Teams</strong> button to create balanced
            teams.
          </p>
        </div>
      )}

    </div>
  );
}

export default Teams;