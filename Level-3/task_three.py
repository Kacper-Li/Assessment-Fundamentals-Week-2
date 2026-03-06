from datetime import date

#####
#
# COPY YOUR CODE FROM LEVEL 2 BELOW
#
#####


class Assessment:
    """Assessment framework."""

    def __init__(self, name: str, type: str, score: float) -> None:
        """Takes specific type and score between 0-100."""
        self.name = name
        self.type = type
        self.validate_type()
        self.score = score
        self.validate_score()

    def validate_type(self) -> None:
        """Validates assessment's type upon initialisation."""
        valid = ['multiple-choice', 'technical', 'presentation']
        if self.type.lower() not in valid:
            raise ValueError("Assessment type not valid.")

    def validate_score(self) -> None:
        """Validates assessment's score upon initialisation."""
        if (self.score < 0) or (self.score > 100):
            raise ValueError("Score outside of valid range 0-100")

    def __str__(self) -> str:
        """Human readable version string representation for Assessment object."""
        return f"{self.name} of type {self.type}. Score: {self.score}"


class MultipleChoiceAssessment(Assessment):
    """Subclass of Assessment"""

    def __init__(self, name: str, score: float | int) -> None:
        """score cannot be a float or int just float, thought tests were weird."""
        super().__init__(name, "multiple-choice", score)
        self.weight = 0.7

    def calculate_score(self) -> float:
        """Calculates specific score for weighting."""
        return self.score * self.weight


class TechnicalAssessment(Assessment):
    """Subclass of Assessment"""

    def __init__(self, name: str, score: float | int) -> None:
        """Name and score required, type inferred"""
        super().__init__(name, "technical", score)
        self.weight = 1

    def calculate_score(self) -> float:
        """Calculates specific score for weighting."""
        return self.score


class PresentationAssessment(Assessment):
    """Subclass of Assessment"""

    def __init__(self, name: str, score: float | int) -> None:
        """Name and score required, type inferred"""
        super().__init__(name, "presentation", score)
        self.weight = 0.6

    def calculate_score(self) -> float:
        """Calculates specific score for weighting."""
        return self.score * self.weight


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

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """Returns list of all assessments of given `type`"""
        valid_assessments = []
        for assessment in self.assessments:
            if assessment.type == type:
                valid_assessments.append(assessment)
        return valid_assessments

    def __str__(self) -> str:
        """Human readable object string representation."""
        return f"{self.name} trainee object"


#####
#
# COPY YOUR CODE FROM LEVEL 2 ABOVE
#
#####


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        pass


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
