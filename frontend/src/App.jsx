import { Routes, Route } from "react-router-dom";

import MainLayout from "./layouts/MainLayout";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Students from "./pages/Students";
import Teams from "./pages/Teams";
import CSVImport from "./pages/CSVImport";
import Export from "./pages/Export";

function App() {
  return (
    <Routes>
      {/* Login Page */}
      <Route path="/" element={<Login />} />

      {/* Dashboard */}
      <Route
        path="/dashboard"
        element={
          <MainLayout>
            <Dashboard />
          </MainLayout>
        }
      />

      {/* Students */}
      <Route
        path="/students"
        element={
          <MainLayout>
            <Students />
          </MainLayout>
        }
      />

      {/* Teams */}
      <Route
        path="/teams"
        element={
          <MainLayout>
            <Teams />
          </MainLayout>
        }
      />

      {/* CSV Import */}
      <Route
        path="/csv"
        element={
          <MainLayout>
            <CSVImport />
          </MainLayout>
        }
      />

      {/* Export */}
      <Route
        path="/export"
        element={
          <MainLayout>
            <Export />
          </MainLayout>
        }
      />
    </Routes>
  );
}

export default App;