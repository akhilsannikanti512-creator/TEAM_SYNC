function StudentRow({
  student,
  onEdit,
  onDelete,
}) {
  return (
    <tr>

      <td>{student.pin}</td>

      <td>{student.name}</td>

      <td>{student.email}</td>

      <td>
        <span className="track-badge">
          {student.track}
        </span>
      </td>

      <td>
        <span
          className={`skill-badge ${
            student.skill.toLowerCase()
          }`}
        >
          {student.skill}
        </span>
      </td>

      <td>

        <button
          className="edit-btn"
          onClick={() => onEdit(student)}
        >
          Edit
        </button>

        <button
          className="delete-btn"
          onClick={() => onDelete(student.id)}
        >
          Delete
        </button>

      </td>

    </tr>
  );
}

export default StudentRow;