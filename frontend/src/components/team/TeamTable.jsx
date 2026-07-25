import TeamRow from "./TeamRow";

function TeamTable({ team, teamNumber }) {
  return (
    <div className="team-table-container">

      <h2 className="team-title">
        Team {teamNumber}
      </h2>

      <table className="team-table">

        <thead>
          <tr>
            <th>Name</th>
            <th>Track</th>
            <th>Skill</th>
          </tr>
        </thead>

        <tbody>

          {team.members.map((member) => (
            <TeamRow
              key={member.id}
              member={member}
            />
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default TeamTable;