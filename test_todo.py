import os
import unittest
import json
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS


from models import setup_db, User, Lists, Task

a = ["eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFwZ0VGZXgzN21LUVc0YUI4QlRBaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1ycDVoaC02ei5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4MzA0NGRjOWE1NWIwMDZmMTJhN2UyIiwiYXVkIjoidG9kbyIsImlhdCI6MTYwMjg0OTczMCwiZXhwIjoxNjAyODU2OTMwLCJhenAiOiIyTWRPU2VUMXg2YUdLZHRRUGZQR2JDOWk2cjk5SWhvcSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmxpc3QiLCJnZXQ6bGlzdCIsInBhdGNoOmxpc3QiLCJwb3N0Omxpc3QiXX0.yMJfhKk2eeBJlQCBQBvPxWC7KmgG3HtxkxkJA2DqH-8Y4Cl0rb_wp-4-xQAcP1LkLnc80EuBV-JSvGcu6YZ04ANSWHSOpNpP0skL6PQyey1kzvn5GecJ_tNGxz9R1Zy-ZAAnI2UOmicUgOQkFpuBJFiUEn6gwCHkQEFqMB_OiSEA1OtPfGEkZro98ZZRLNl3tYVZOjcvlqwZ0pqr8rZAo3gnSESMLQJtNoDooEhhnW4pmqdlqgVp2w0mDjqLXv-itzFvA3e5v5Oe3vzGZRGnchfn_8CLTH2aZZFD3XQxLyY7pkF0P-ZsnUH6j3TcRnECauoWH0l6FqqnKPJodGpVmA"]

headers = {
        'Authorization': 'Bearer {}'.format(a[0]),
        'Content-Type': 'application/json'
          }

test_taskdata = {
    "content": "Test Content",
    "status": "True",
    "list_id": 27

}

patch_taskdata = {
    "content": "Changed",
    "status": "False"
}

class TodoTest(unittest.TestCase):


    def test_getlist_success(self):
        res = requests.get('http://127.0.0.1:5000/list', headers=headers)

        self.assertEqual(res.status_code, 200)

    def test_getlist_error(self):
        res = requests.get('http://127.0.0.1:5000/list', headers=headers)

        self.assertEqual(res.status_code, 500)

    def test_gettask_success(self):
        res = requests.get('http://127.0.0.1:5000/task', headers=headers)

        self.assertEqual(res.status_code, 200)

    def test_gettask_error(self):
        res = requests.get('http://127.0.0.1:5000/task', headers=headers)

        self.assertEqual(res.status_code, 500)

    def test_addtask_success(self):
        res = requests.post('http://127.0.0.1:5000/addtask', json=test_taskdata, headers=headers)

        self.assertEqual(res.status_code, 200)

    def test_addtask_error(self):
        res = requests.post('http://127.0.0.1:5000/addtask', json=test_taskdata, headers=headers)

        self.assertEqual(res.status_code, 500)

    def test_patchtask_success(self):
        res = requests.patch('http://127.0.0.1:5000/task/update/1', json=patch_taskdata, headers=headers)

        self.assertEqual(res.status_code, 200)

    def test_patchtask_error(self):
        res = requests.patch('http://127.0.0.1:5000/task/update/1', json=patch_taskdata, headers=headers)

        self.assertEqual(res.status_code, 500)

    def test_deletetask_success(self):
        res = requests.delete('http://127.0.0.1:5000/task/delete/11',headers=headers)

        self.assertEqual(res.status_code, 200)

    def test_deletetask_error(self):
        res = requests.delete('http://127.0.0.1:5000/task/delete/11',headers=headers)

        self.assertEqual(res.status_code, 500)


    # def test_categories_withid(self):
    #     res = self.client().get('/categories/1/questions')
    #     data = json.loads(res.data)


    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(len(data['categories']))

    # # please change id to test delete function

    # def test_delete_book(self):
    #     res = self.client().delete('/questions/1')
    #     data = json.loads(res.data)
        
    #     question = Question.query.filter(Question.id == 1).one_or_none()

    #     print (data)

    #     self.assertEqual(res.status_code,200)
    #     self.assertEqual(question, None)

    # def test_create_new_question(self):
    #     res = self.client().post('/questions/create', json=self.new_question)
    #     data = json.loads(res.data)
            
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['created'])

    # def test_return_searchresult(self):
    #     res = self.client().post('/questions', json={"question" : "who"})
    #     data = json.loads(res.data)
            
    #     self.assertEqual(res.status_code, 200)


    # def test_questions_randomsearch(self):
    #     res = self.client().post('/questions/randomsearch', json={"category" : "1"})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(len(data['data']))


    # def test_quizzes(self):
    #     res = self.client().post('/quizzes', json=self.quizquestion)
    #     data = json.loads(res.data)


    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data['question']) 
        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()