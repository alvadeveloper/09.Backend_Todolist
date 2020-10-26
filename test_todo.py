import os
import unittest
import json
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS


from models import setup_db, User, Lists, Task

a = os.environ.get('TEST_API')

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
            'https://todolist-udacity2020.herokuapp.com/task/delete/11', headers=headers)

        self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
