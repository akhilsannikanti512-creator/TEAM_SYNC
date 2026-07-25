function TeamRow({ member }) {
  return (
    <tr>

      <td>{member.name}</td>

      <td>{member.track}</td>

      <td>
        <span
          className={`skill-badge ${member.skill.toLowerCase()}`}
        >
          {member.skill}
        </span>
      </td>

    </tr>
  );
}

export default TeamRow;