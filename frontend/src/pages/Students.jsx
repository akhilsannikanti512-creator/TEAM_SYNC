import { useEffect, useState } from "react";
import api from "../services/api";
import StudentToolbar from "../components/student/StudentToolbar";
import StudentTable from "../components/student/StudentTable";
import StudentModal from "../components/modal/StudentModal";
import "../styles/Students.css";

function Students() {
  const [students, setStudents] = useState([]);
  const [search, setSearch] = useState("");
  const [modalOpen, setModalOpen] = useState(false);
  const [selectedStudent, setSelectedStudent] = useState(null);

  useEffect(() => {
    fetchStudents();
  }, []);

  const fetchStudents = async () => {
    const token = localStorage.getItem("token");
    const response = await api.get("/students/", {
      headers: { Authorization: `Bearer ${token}` },
    });
    setStudents(response.data);
  };

  const handleSave = async (formData) => {
    const token = localStorage.getItem("token");

    if (selectedStudent) {
      await api.put(`/students/${selectedStudent.id}`, formData, {
        headers: { Authorization: `Bearer ${token}` },
      });
    } else {
      await api.post("/students/", formData, {
        headers: { Authorization: `Bearer ${token}` },
      });
    }

    setModalOpen(false);
    fetchStudents();
  };

  const handleDelete = async (id) => {
    if (!window.confirm("Delete this student?")) return;

    const token = localStorage.getItem("token");

    await api.delete(`/students/${id}`, {
      headers: { Authorization: `Bearer ${token}` },
    });

    fetchStudents();
  };

  const filteredStudents = students.filter((student) =>
    student.name.toLowerCase().includes(search.toLowerCase()) ||
    student.pin.toLowerCase().includes(search.toLowerCase()) ||
    student.email.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="students-container">
      <StudentToolbar
        search={search}
        setSearch={setSearch}
        onAdd={() => {
          setSelectedStudent(null);
          setModalOpen(true);
        }}
      />

      <StudentTable
        students={filteredStudents}
        onEdit={(student) => {
          setSelectedStudent(student);
          setModalOpen(true);
        }}
        onDelete={handleDelete}
      />

      <StudentModal
        isOpen={modalOpen}
        onClose={() => setModalOpen(false)}
        onSave={handleSave}
        student={selectedStudent}
      />
    </div>
  );
}

export default Students;
