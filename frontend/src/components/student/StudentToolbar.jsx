function StudentToolbar({
  search,
  setSearch,
  onAdd,
}) {
  return (
    <div className="students-header">

      <input
        type="text"
        placeholder="Search students..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <button onClick={onAdd}>
        + Add Student
      </button>

    </div>
  );
}

export default StudentToolbar;