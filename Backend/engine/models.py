from dataclasses import dataclass


@dataclass
class Student:
    pin: str
    name: str
    email: str
    track: str
    skill: str


@dataclass
class Team:
    team_number: int
    students: list