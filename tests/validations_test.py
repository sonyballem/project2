# import unittest
# from flask import current_app
# from flask_login import current_user
#
# from app import create_app, User
#
#
# class TestWebApp(unittest.TestCase):
#     def setUp(self):
#         self.application = create_app()
#         self.appctx = self.application.app_context()
#         self.appctx.push()
#
#     def tearDown(self):
#         self.appctx.pop()
#         self.application = None
#         self.appctx = None
#
#     def test_app(self):
#         assert self.application is not None
#         assert current_app == self.application
#
#
# # def test_successful_registration(client):
# #     response = client.post('/register', data={'email': 'test@test.com',
# #                                               'password': 'Testing',
# #                                               'confirm': 'Testing'}, follow_redirects=True)
# #     assert response.status_code == 200
# #     print(response.status_code)
#
# def test_successful_login(client):
#     response = client.post('/login', data={'email': 'test@test.com',
#                                            'password': 'Testing'}, follow_redirects=True)
#     assert response.status_code == 200
#     assert 'success'.encode('utf-8') in response.data
#
#
# def test_bad_email_login(client):
#     response = client.post('/login', data={'email': 'test@fake.com',
#                                            'password': 'Testing'}, follow_redirects=True)
#     assert response.status_code == 200
#     # print(response.data)
#     assert 'Invalid email'.encode('utf-8') in response.data
#
#
# def test_bad_password_login(client):
#     response = client.post('/login', data={'email': 'test@test.com',
#                                            'password': 'odfsdfmsdl'}, follow_redirects=True)
#     assert response.status_code == 200
#     assert 'Invalid password'.encode('utf-8') in response.data
#
#
# def test_short_password_login(client):
#     response = client.post('/login', data={'email': 'test@test.com',
#                                            'password': 'otp'}, follow_redirects=True)
#     assert response.status_code == 200
#     # print(response.data)
#     assert 'Field must be between 6 and 35 characters'.encode('utf-8') in response.data
#
#
# def test_check_registration(client):
#     response = client.post('/register', data={'email': 'newuser@gmail.com',
#                                            'password': 'Testing',
#                                             'confirm' : 'Testing'}, follow_redirects=True)
#     assert ' Already Registered'.encode('utf-8') in response.data
#
#
# def test_password_criteria_registration(client):
#     response = client.post('/register', data={'email': 'xyz@gmail.com',
#                                            'password': 'Tes',
#                                             'confirm' : 'Tes'}, follow_redirects=True)
#     assert 'Field must be between 6 and 35 characters'.encode('utf-8') in response.data
#
# def test_password_match_registration(client):
#     response = client.post('/register', data={'email': 'xyz@gmail.com',
#                                            'password': 'Testing',
#                                             'confirm' : 'random'}, follow_redirects=True)
#     assert 'Passwords must match'.encode('utf-8') in response.data
#
#
# def test_email_criteria_registration(client):
#     response = client.post('/register', data={'email': 'xyz',
#                                            'password': 'Testing',
#                                             'confirm' : 'Testing'})
#     assert 'Invalid email address'.encode('utf-8') in response.data
#
#
# def test_dashboard_allow_access(client):
#     response = client.post('/login', data={'email': 'test@test.com',
#                                            'password': 'Testing'}, follow_redirects=True)
#     assert 'Dashboard'.encode('utf-8') in response.data
#
#
# def test_dashboard_deny_access(client):
#
#     response = client.get('/dashboard', follow_redirects=True)
#     assert ' Please log in to access this page.'.encode('utf-8') in response.data
