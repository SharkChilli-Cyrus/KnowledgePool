import sys
import os
import unittest

# def get_formatted_name(firstName, lastName, middleName=''):
#     """
#     Generate a neatly formatted full name
#     """
#     if middleName:
#         fullName = "{0} {1} {2}".format(firstName, middleName, lastName)
#     else:
#         fullName = "{0} {1}".format(firstName, lastName)
#     return fullName.title()


# class NamesTestCase(unittest.TestCase):
#     """This is a description"""

#     def test_first_last_name(self):
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')
    
#     def test_first_last_middle_name(self):
#         formatted_name = get_formatted_name('woldgang', 'mozart', 'amadeus')
#         self.assertEqual(formatted_name, 'Woldgang Amadeus Mozart')

# unittest.main()
# ----------------------------------------------------------------------------------------------------

class AnonymousSurvey():
    """This is a class description"""

    def __init__(self, question):
        self.question = question
        self.responses = []
    
    def show_question(self):
        print(self.question)
    
    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_results(self):
        print("Survey Results:")
        for response in self.responses:
            print('- {0}'.format(response))


# question = "What language did you first learn to speak?"
# mySurvey = AnonymousSurvey(question)
# mySurvey.show_question()

# print("Enter 'q' at any time to quit.\n")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     else:
#         pass
#     mySurvey.store_response(response)

# print("\nThank you to everyone who participated in the survey!")
# mySurvey.show_results()

# class TestAnonmyousSurvey(unittest.TestCase):
#     """This is a class description"""

#     def test_store_single_response(self):
#         question = "What language did you first learn to speak?"
#         mySurvey = AnonymousSurvey(question)
#         mySurvey.store_response('English')

#         self.assertIn('English', mySurvey.responses)
    
#     def test_store_three_responses(self):
#         question = "What language did you first learn to speak?"
#         mySurvey = AnonymousSurvey(question)
#         responses = ['English', 'Spanish', 'Mandarin']
#         for response in responses:
#             mySurvey.store_response(response)
        
#         for response in responses:
#             self.assertIn(response, mySurvey.responses)

class TestAnonmyousSurvey(unittest.TestCase):
    """This is a class description"""

    def setUp(self):
        question = "What language did you first learn to speak?"
        self.mySurvey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        self.mySurvey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.mySurvey.responses)
    
    def test_store_three_responses(self):
        for response in self.responses:
            self.mySurvey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.mySurvey.responses)


unittest.main()