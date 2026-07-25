import { useState } from "react";
import api from "../services/api";

function CSVImport() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImport = async () => {
    if (!file) {
      alert("Please select a CSV file.");
      return;
    }

    try {
      setLoading(true);

      const formData = new FormData();
      formData.append("file", file);

      const token = localStorage.getItem("token");

      const response = await api.post("/csv/import", formData, {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "multipart/form-data",
        },
      });

      alert(
        `${response.data.message}\nImported: ${response.data.count} students`
      );

      setFile(null);
    } catch (error) {
      console.error(error);
      alert(error.response?.data?.detail || "CSV import failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "30px" }}>
      <h1>CSV Import</h1>

      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={handleImport} disabled={loading}>
        {loading ? "Importing..." : "Import CSV"}
      </button>
    </div>
  );
}

export default CSVImport;