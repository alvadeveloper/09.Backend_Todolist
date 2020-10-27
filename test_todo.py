import os
import unittest
import json
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS


from models import setup_db, User, Lists, Task

a = ['eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFwZ0VGZXgzN21LUVc0YUI4QlRBaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1ycDVoaC02ei5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY4MzA0NGRjOWE1NWIwMDZmMTJhN2UyIiwiYXVkIjoidG9kbyIsImlhdCI6MTYwMzgwMzUxOSwiZXhwIjoxNjAzODg5OTE5LCJhenAiOiIyTWRPU2VUMXg2YUdLZHRRUGZQR2JDOWk2cjk5SWhvcSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmxpc3QiLCJnZXQ6bGlzdCIsInBhdGNoOmxpc3QiLCJwb3N0Omxpc3QiXX0.JU887UjzvnHqnO-WigqKBGOSbN3xUr_HZoJsHlTlfMy4eqkq7TMVENb_Uy_6teyvU-_1ULi34o5sZaOTDg9pOL1uA4tGt-kzXw1AsrkbHKKYYUoeUCHUa7jnqxhRxG4_1e2cMUQfeDLXwNnQzNceLA73LcOP2TZEnGwvmxqi7Wh_-r_0hLGzRrm5YjsrWonZgy9h4S_n8PhNFh1lk_UGrPnYVXZKBUZpYXdehc3cAtrrQ29g0ToojkpZyelH11jwEp4KvrVcbfetm1y9nf4m8jPxg1QK4ffNO4J_4hTmwNQERE8dAHLNR51HoemM_QVmkGoAeVaPFpwL2DYlTBlGeg']

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
        res = requests.get('https://todolist-udacity2020.herokuapp.com/list', headers=headers)

        self.assertEqual(res.status_code, 200)


    def test_gettask_success(self):
        res = requests.get('https://todolist-udacity2020.herokuapp.com/task', headers=headers)

        self.assertEqual(res.status_code, 200)


    def test_addtask_success(self):
        res = requests.post('https://todolist-udacity2020.herokuapp.com/addtask',
                            json=test_taskdata, headers=headers)

        self.assertEqual(res.status_code, 200)


    def test_patchtask_success(self):
        res = requests.patch('https://todolist-udacity2020.herokuapp.com/task/update/1',
                             json=patch_taskdata, headers=headers)

        self.assertEqual(res.status_code, 200)

    def test_deletetask_success(self):
        res = requests.delete(
            'https://todolist-udacity2020.herokuapp.com/task/delete/15', headers=headers)

        self.assertEqual(res.status_code, 200)





# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
