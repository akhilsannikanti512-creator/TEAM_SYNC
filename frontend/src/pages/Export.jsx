import { useState } from "react";
import api from "../services/api";
import "../styles/Export.css";

function Export() {

  const [loading, setLoading] = useState(false);

  const handleExport = async () => {

    try {

      setLoading(true);

      const token = localStorage.getItem("token");

      const response = await api.get(
        "/excel/export",
        {
          responseType: "blob",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      const url = window.URL.createObjectURL(
        new Blob([response.data])
      );

      const link = document.createElement("a");

      link.href = url;
      link.setAttribute("download", "teams.xlsx");

      document.body.appendChild(link);

      link.click();

      link.remove();

      window.URL.revokeObjectURL(url);

      alert("✅ Excel exported successfully!");

    } catch (error) {

      console.error(error);

      alert("❌ Failed to export Excel.");

    } finally {

      setLoading(false);

    }

  };

  return (
    <div className="export-container">

      <div className="export-card">

        <h1>Export Teams</h1>

        <p>
          Download all generated teams as an Excel file.
        </p>

        <button
          className="export-btn"
          onClick={handleExport}
          disabled={loading}
        >
          {loading ? "Exporting..." : "Download Excel"}
        </button>

      </div>

    </div>
  );
}

export default Export;