import StudentRow from "./StudentRow";

function StudentTable({
  students,
  onEdit,
  onDelete,
}) {
  return (
    <table className="student-table">

      <thead>

        <tr>
          <th>PIN</th>
          <th>Name</th>
          <th>Email</th>
          <th>Track</th>
          <th>Skill</th>
          <th>Actions</th>
        </tr>

      </thead>

      <tbody>

        {students.length > 0 ? (

          students.map((student) => (

            <StudentRow
              key={student.id}
              student={student}
              onEdit={onEdit}
              onDelete={onDelete}
            />

          ))

        ) : (

          <tr>
            <td colSpan="6" className="no-data">
              No Students Found
            </td>
          </tr>

        )}

      </tbody>

    </table>
  );
}

export default StudentTable;