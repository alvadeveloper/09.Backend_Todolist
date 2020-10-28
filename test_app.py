import os
import unittest
import json
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS


from models import setup_db, User, Lists, Task

user = ['eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFwZ0VGZXgzN21LUVc0YUI4QlRBaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1ycDVoaC02ei5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4MzA0NGRjOWE1NWIwMDZmMTJhN2UyIiwiYXVkIjoidG9kbyIsImlhdCI6MTYwMzg4OTE0NCwiZXhwIjoxNjAzOTc1NTQ0LCJhenAiOiIyTWRPU2VUMXg2YUdLZHRRUGZQR2JDOWk2cjk5SWhvcSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmxpc3QiLCJnZXQ6bGlzdCIsInBhdGNoOmxpc3QiLCJwb3N0Omxpc3QiXX0.DE27X3XD1JcGPdAstD6Phc-8K1KCg0hi0eQkvkaCt5yVvoU76oQolrt8T5_PSf4qixGXUzGVJKC-a6HjoDn9IHogzWEDjOcdit99mPu51GtTmJVce6dlIj-9CyEgJ4gIbOw5Q1mmk5FaLwatdorfJFLdYueK1ZMafAX3GfyKmxgMiDbE4qOOXk1_URLbmDd7mZYDabhT8Q_VVFb939UYJoLjWJUX8X6X9Uy3bQKUgfzznW7qfUcw6poyN2erISTa_oUgdq44C7oFyy9V6Fr_xojMovopVFpJu_BDep-xHESmE20pE3S_AMrMX4E4cGxJSEtLB-PpymnzBolez5WNZg']
admin = ['eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFwZ0VGZXgzN21LUVc0YUI4QlRBaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1ycDVoaC02ei5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3NTllOGIxMjEzYmEwMDZmYTlhODM1IiwiYXVkIjoidG9kbyIsImlhdCI6MTYwMzg4OTIyOSwiZXhwIjoxNjAzOTc1NjI5LCJhenAiOiIyTWRPU2VUMXg2YUdLZHRRUGZQR2JDOWk2cjk5SWhvcSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0Omxpc3QiXX0.M3xEpgEB72yeOHkp82lp6ZVoPdZqcMqx8KTIqDfi9-9eekU0NKpQmMNxQvQ0Fex4OMKbDvaPDUlHIpVLjgXGu8cIuTiUneSYnJGUmjEt5lBQpZ0Y_lFtUhaopyxXxbgt7D_PzSTYIj9cLbt1GI3GE4nzryTaM4dcZWtVr894Gk4MAQUHWkpFd6NqPjGciyignjXfqtT6ichZakoAMAfmBsePf5FXgyTnYNa6qon9Lko22POMs19iCSId53WK44-xbUMEGSdoBTAfAhxfgRx44fgbCyaljfZpDUj5b1jjyoXvOdeJRSedwDLPp5WZ_EMDrzlkN23XjJhOej6gmw4j9A']

userheader = {
    'Authorization': 'Bearer {}'.format(user[0]),
    'Content-Type': 'application/json'
}

adminheader = {
    'Authorization': 'Bearer {}'.format(admin[0]),
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

    # Test for User Role behavior

    def testuser_getlist_success(self):
        res = requests.get(
            'https://todolist-udacity2020.herokuapp.com/list', headers=userheader)

        self.assertEqual(res.status_code, 200)

    def testuser_gettask_success(self):
        res = requests.get(
            'https://todolist-udacity2020.herokuapp.com/task', headers=userheader)

        self.assertEqual(res.status_code, 200)

    def testuser_addtask_success(self):
        res = requests.post('https://todolist-udacity2020.herokuapp.com/addtask',
                            json=test_taskdata, headers=userheader)

        self.assertEqual(res.status_code, 200)

    def testuser_patchtask_success(self):
        res = requests.patch('https://todolist-udacity2020.herokuapp.com/task/update/1',
                             json=patch_taskdata, headers=userheader)

        self.assertEqual(res.status_code, 200)

    # Request Error Behaviors in User Role

    def testuser_deletetask_failure(self):
        res = requests.delete(
            'https://todolist-udacity2020.herokuapp.com/task/delete/220', headers=userheader)

        self.assertEqual(res.status_code, 404)

    # Test for Admin Role Behavior

    def testadmin_getlist_success(self):
        res = requests.get(
            'https://todolist-udacity2020.herokuapp.com/list', headers=adminheader)

        self.assertEqual(res.status_code, 200)

    def testadmin_gettask_success(self):
        res = requests.get(
            'https://todolist-udacity2020.herokuapp.com/task', headers=adminheader)

        self.assertEqual(res.status_code, 200)

    # Request Error Behaviors in Admin Role

    def testadmin_addtask_failure(self):
        res = requests.post('https://todolist-udacity2020.herokuapp.com/addtask',
                            json=test_taskdata, headers=adminheader)

        self.assertEqual(res.status_code, 500)

    def testadmin_patchtask_failure(self):
        res = requests.patch('https://todolist-udacity2020.herokuapp.com/task/update/1',
                             json=patch_taskdata, headers=adminheader)

        self.assertEqual(res.status_code, 500)

    def testadmin_deletetask_failure(self):
        res = requests.delete(
            'https://todolist-udacity2020.herokuapp.com/task/delete/1', headers=adminheader)

        self.assertEqual(res.status_code, 500)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
