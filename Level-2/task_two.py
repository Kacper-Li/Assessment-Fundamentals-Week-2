from datetime import date


#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####

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
        if (self.score < 0) or (self.score > 100):
            raise ValueError("Score outside of valid range 0-100")

    def __str__(self):
        """Human readable version string representation for Assessment object."""
        return f"{self.name} of type {self.type}. Score: {self.score}"


class Trainee:
    """Trainee framework."""

    def __init__(self, name: str, email: str, date_of_birth: date, assessments: list[Assessment] = None) -> None:
        """initialises a trainee with relevant details nad assesments done."""
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = assessments if assessments else []

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

    def __str__(self):
        """Human readable object string representation."""
        return f"{self.name} trainee object"


#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
