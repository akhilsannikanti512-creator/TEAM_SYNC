import { useEffect, useState } from "react";
import "./StudentModal.css";

function StudentModal({
  isOpen,
  onClose,
  onSave,
  student = null,
}) {
  const [formData, setFormData] = useState({
    pin: "",
    name: "",
    email: "",
    track: "Gen AI",
    skill: "Average",
  });

  useEffect(() => {
    if (student) {
      setFormData(student);
    } else {
      setFormData({
        pin: "",
        name: "",
        email: "",
        track: "Gen AI",
        skill: "Average",
      });
    }
  }, [student]);

  if (!isOpen) return null;

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = () => {
    onSave(formData);
  };

  return (
    <div className="modal-overlay">

      <div className="modal">

        <h2>
          {student ? "Edit Student" : "Add Student"}
        </h2>

        <input
          name="pin"
          placeholder="PIN"
          value={formData.pin}
          onChange={handleChange}
        />

        <input
          name="name"
          placeholder="Student Name"
          value={formData.name}
          onChange={handleChange}
        />

        <input
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
        />

        <select
          name="track"
          value={formData.track}
          onChange={handleChange}
        >
          <option>Gen AI</option>
          <option>Full Stack</option>
          <option>DevOps</option>
        </select>

        <select
          name="skill"
          value={formData.skill}
          onChange={handleChange}
        >
          <option>Good</option>
          <option>Average</option>
          <option>Beginner</option>
        </select>

        <div className="modal-buttons">

          <button
            className="cancel-btn"
            onClick={onClose}
          >
            Cancel
          </button>

          <button
            className="save-btn"
            onClick={handleSubmit}
          >
            Save
          </button>

        </div>

      </div>

    </div>
  );
}

export default StudentModal;