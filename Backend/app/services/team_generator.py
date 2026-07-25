"""
team_generator.py

Pure Python service responsible for generating balanced, mixed-track
student teams for the TeamSync platform.

This module is intentionally decoupled from any persistence layer
(SQLAlchemy, databases, ORMs) and from any web framework (FastAPI).
It operates exclusively on the Student objects passed into it and
in-memory data structures, making it fully unit-testable in isolation.
"""

from typing import Any, List, Tuple

# Type alias for readability. The actual Student type is defined by
# the project's existing model (e.g. SQLAlchemy ORM model) and is
# intentionally not redefined or imported here.
Student = Any


class TeamGenerator:
    """
    Generates balanced, mixed-track teams of students according to
    TeamSync's Version 1.0 allocation rules.

    Team composition rule (fixed team size = 5):
        - 2 Full Stack students
        - 2 DevOps students
        - 1 Gen AI student

    Each team is built by combining students across all three tracks
    at once, so every generated team is mixed (never single-track).
    The generator never mutates the database and never performs I/O.
    It keeps track of unassigned students after team creation.
    """

    # Track identifiers as expected in Student.track
    TRACK_FULL_STACK = "Full Stack"
    TRACK_DEVOPS = "DevOps"
    TRACK_GENAI = "Gen AI"

    # Required composition for a single complete team
    REQUIRED_FULL_STACK = 2
    REQUIRED_DEVOPS = 2
    REQUIRED_GENAI = 1
    MAX_TEAM_SIZE = REQUIRED_FULL_STACK + REQUIRED_DEVOPS + REQUIRED_GENAI

    def __init__(self) -> None:
        """Initialize the generator with an empty pool of unassigned students."""
        self._remaining_students: List[Student] = []

    def separate_students_by_track(
        self, students: List[Student]
    ) -> Tuple[List[Student], List[Student], List[Student]]:
        """
        Split a flat list of students into three lists based on track.

        Args:
            students: List of Student objects to categorize.

        Returns:
            A tuple of (full_stack, devops, genai) student lists.
        """
        full_stack = [s for s in students if s.track == self.TRACK_FULL_STACK]
        devops = [s for s in students if s.track == self.TRACK_DEVOPS]
        genai = [s for s in students if s.track == self.TRACK_GENAI]

        return full_stack, devops, genai

    def create_balanced_teams(self, students: List[Student]) -> List[List[Student]]:
        """
        Generate complete, mixed-track teams from the given student pool.

        Each team strictly follows the required composition:
        2 Full Stack + 2 DevOps + 1 Gen AI (total size = 5).
        Students are pulled from all three tracks simultaneously for
        every team, so no single-track team is ever produced.
        Incomplete teams are never created. Any students that cannot
        be placed into a complete team are stored internally and can
        be retrieved via get_remaining_students().

        Args:
            students: Full list of students available for allocation.

        Returns:
            A list of teams, where each team is a list of exactly
            MAX_TEAM_SIZE Student objects.
        """
        full_stack, devops, genai = self.separate_students_by_track(students)

        teams: List[List[Student]] = []

        # Keep building teams while there are enough students left in
        # each track to satisfy one full, mixed team.
        while (
            len(full_stack) >= self.REQUIRED_FULL_STACK
            and len(devops) >= self.REQUIRED_DEVOPS
            and len(genai) >= self.REQUIRED_GENAI
        ):
            team: List[Student] = []

            # Pull required members from each track for this single team.
            for _ in range(self.REQUIRED_FULL_STACK):
                team.append(full_stack.pop(0))

            for _ in range(self.REQUIRED_DEVOPS):
                team.append(devops.pop(0))

            for _ in range(self.REQUIRED_GENAI):
                team.append(genai.pop(0))

            teams.append(team)

        # Whatever remains in each track (not enough to form another
        # complete team) stays unassigned.
        self._remaining_students = full_stack + devops + genai

        return teams

    def get_remaining_students(self) -> List[Student]:
        """
        Retrieve students who could not be assigned to a complete team.

        Must be called after create_teams(); otherwise it returns an
        empty list since no allocation has occurred yet.

        Returns:
            List of unassigned Student objects.
        """
        return self._remaining_students