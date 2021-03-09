import html

import requests


def get_bool(bool_str: str):
    return bool_str.lower() == 'true'


class QuizBrain:
    TRIVIA_API = 'https://opentdb.com/api.php?amount=20&type=boolean'

    def __init__(self):
        self.current_quiz_no = -1
        self.score = 0
        self.quiz = []

    def get_quiz(self):
        print('getting quiz...')
        response = requests.get(url=self.TRIVIA_API)
        response.raise_for_status()
        questions = response.json()['results']
        self.quiz = [{"question": html.unescape(ques["question"]), "answer": get_bool(ques['correct_answer'])} for ques
                     in
                     questions]

    def get_current_question(self):
        self.current_quiz_no += 1
        if self.current_quiz_no >= len(self.quiz):
            raise ValueError('No More Questions Left')
        ques = self.quiz[self.current_quiz_no]
        return ques

    def increment_score(self):
        self.score += 1

    def reset(self):
        self.current_quiz_no = -1
        self.score = 0

    def check_current_answer(self, answer):
        print(answer)
        print(self.current_quiz_no)
        # if self.current_quiz_no >= len(self.quiz):
        #     return answer == self.quiz[-1]['answer']
        return answer == self.quiz[self.current_quiz_no]['answer']

