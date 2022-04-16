# import datetime
# from os import getenv
#
#
# def test_context_variables_environment(client):
#     """This test checks if the environment is printed"""
#     response = client.get("/")
#     env = getenv('FLASK_ENV', None)
#     test_string = f"Environment: {env}"
#     content = bytes(test_string, 'utf-8')
#     assert response.status_code == 200
#     assert content in response.data
#
#
# def test_context_variables_year(client):
#     """This tests checks if the copyright and current year are printed"""
#     response = client.get("/")
#     current_date_time = datetime.datetime.now()
#     date = current_date_time.date()
#     year = date.strftime("%Y")
#     test_string = f"Copyright: {year}"
#     content = bytes(test_string, 'utf-8')
#     assert response.status_code == 200
#     assert content in response.data
#
#
# def test_context_currency_format(client):
#     """This tests checks if the copyright and current year are printed"""
#     response = client.get("/")
#     test_string = f"$100"
#     content = bytes(test_string, 'utf-8')
#     assert response.status_code == 200
#     assert content in response.data
#

# def test_registration_form(client):
#     response = client.get('/auth/templates/register')
#     assert response.status_code == 200
#     html = response.get_data(as_text=True)
#
#     # make sure all the fields are included
#     assert 'name="email"' in html
#     assert 'name="password"' in html
#     assert 'name="confirm"' in html
#     assert 'name="submit"' in html
