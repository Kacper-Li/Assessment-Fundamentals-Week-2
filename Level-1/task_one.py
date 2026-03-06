from datetime import date


class Assessment:
    """Assessment framework."""

    def __init__(self, name: str, type: str, score: float) -> None:
        self.name = name
        self.type = type
        self.validate_type()
        self.score = score
        self.validate_score()

    def validate_type(self):
        """Validates assessment's type upon initialisation."""
        valid = ['multiple-choice', 'technical', 'presentation']
        if self.type not in valid:
            raise ValueError("Assessment type not valid.")

    def validate_score(self):
        """Validates assessment's score upon initialisation."""
        if self.score not in range(0, 101):
            raise ValueError("Score outside of valid range 0-100")


class Trainee:
    """Trainee framework."""

    def __init__(self, name: str, email: str, date_of_birth: date, assessments: list[Assessment]) -> None:
        """initialises a trainee with relevant details nad assesments done."""
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = assessments

    def get_age(self) -> int:
        """Gets age from date_of_birth."""
        today = date.today()
        age = today - self.date_of_birth
        return age.days//365

    def add_assessment(self, assessment: Assessment) -> None:
        """Adds an assessment to trainees list of assessments."""
        if not isinstance(assessment, Assessment):
            raise TypeError("Needs to be an Assessment instance.")
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """returns the `Assessment` object that has the name given"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
