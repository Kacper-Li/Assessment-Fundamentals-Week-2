"""Task 3 of Technical Assessment. Kinda uses previous levels (not really)"""
from datetime import date

#####
#
# COPY YOUR CODE FROM LEVEL 2 BELOW
#
#####


class Assessment:
    """Assessment framework."""

    def __init__(self, name: str, given_type: str, score: float) -> None:
        """Takes specific given_type and score between 0-100."""
        self.name = name
        self.given_type = given_type
        self.validate_type()
        self.score = score
        self.validate_score()

    def validate_type(self) -> None:
        """Validates assessment's given_type upon initialisation."""
        valid = ['multiple-choice', 'technical', 'presentation']
        if self.given_type.lower() not in valid:
            raise ValueError("Assessment given_type not valid.")

    def validate_score(self) -> None:
        """Validates assessment's score upon initialisation."""
        if (self.score < 0) or (self.score > 100):
            raise ValueError("Score outside of valid range 0-100")

    def __str__(self) -> str:
        """Human readable version string representation for Assessment object."""
        return f"{self.name} of given_type {self.given_type}. Score: {self.score}"


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
        """Name and score required, given_type inferred"""
        super().__init__(name, "technical", score)
        self.weight = 1

    def calculate_score(self) -> float:
        """Calculates specific score for weighting."""
        return self.score


class PresentationAssessment(Assessment):
    """Subclass of Assessment"""

    def __init__(self, name: str, score: float | int) -> None:
        """Name and score required, given_type inferred"""
        super().__init__(name, "presentation", score)
        self.weight = 0.6

    def calculate_score(self) -> float:
        """Calculates specific score for weighting."""
        return self.score * self.weight


class Trainee:
    """Trainee framework."""

    def __init__(
        self,
        name: str,
        email: str,
        date_of_birth: date,
        assessments: list[Assessment] = None
    ) -> None:
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

    def get_assessment_of_type(self, given_type: str) -> list[Assessment]:
        """Returns list of all assessments of given `given_type`"""
        valid_assessments = []
        for assessment in self.assessments:
            if assessment.given_type == given_type:
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
    """Question object that stores questions and answers"""

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        """Completely different to what we made before, but another way to store questions."""
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer
        self.validate_question()
        self.validate_chosen_answer()
        self.validate_correct_answer()

    def validate_question(self) -> None:
        """Validates that question is a string"""
        if not isinstance(self.question, str):
            raise TypeError("Question is required to be a string.")

    def validate_chosen_answer(self) -> None:
        """Validates that chosen_answer is a string"""
        if not isinstance(self.question, str):
            raise TypeError("Chosen answer is required to be a string.")

    def validate_correct_answer(self) -> None:
        """Validates that correct_answer is a string"""
        if not isinstance(self.question, str):
            raise TypeError("Correct answer is required to be a string.")


class Quiz:
    """Quiz template that handles questions"""

    def __init__(self, questions: list[Question], name: str, given_type: str):
        """Takes values to describe specific quiz given_type."""
        self.questions = questions
        self.name = name
        self.given_type = given_type
        self.validate_questions()

    def validate_name_and_type(self):
        """Ensures both are str"""
        if not isinstance(self.name, str):
            raise TypeError("Name should be a string.")
        if not isinstance(self.given_type, str):
            raise TypeError("Type value needs to be a string.")

    def validate_questions(self):
        """Bounds question list between 0 and 100"""
        num_of_questions = len(self.questions)
        if num_of_questions < 0:
            raise ValueError("Uhh... less than 0 questions... input?")
        if num_of_questions > 100:
            raise ValueError("The quiz is simply too big, add less questions.")


class Marking:
    """Controls marking of a quiz."""

    def __init__(self, quiz: Quiz) -> None:
        """Initialises the quiz for marking."""
        self._quiz = quiz

    def mark(self) -> int:
        """Returns total score for assessment as %."""
        points = 0
        questions = self._quiz.questions
        if questions == []:
            return 0
        num_of_questions = len(questions)
        for question in questions:
            if question.chosen_answer == question.correct_answer:
                points += 1
        return int(points * 100 / num_of_questions)

    def generate_assessment(self) -> Assessment:
        """Generates proper assessment given_type from quiz."""
        quiz = self._quiz
        if quiz.given_type == "presentation":
            ass = PresentationAssessment(quiz.name, self.mark())
        elif quiz.given_type == "multiple-choice":
            ass = MultipleChoiceAssessment(quiz.name, self.mark())
        elif quiz.given_type == "technical":
            ass = TechnicalAssessment(quiz.name, self.mark())
        else:
            raise ValueError(
                "We don't know how, but you managed to slip an invalid given_type through.")
        return ass


if __name__ == "__main__":
    # Example questions and quiz
    questions1 = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz1 = Quiz(questions1, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
