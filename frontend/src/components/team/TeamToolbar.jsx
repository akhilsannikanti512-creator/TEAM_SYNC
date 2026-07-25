function TeamToolbar({
  search,
  setSearch,
  onGenerate,
}) {
  return (
    <div className="teams-header">

      <input
        type="text"
        placeholder="Search Team..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <button onClick={onGenerate}>
        Generate Teams
      </button>

    </div>
  );
}

export default TeamToolbar;