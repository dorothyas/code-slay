import unittest
from users import Users, Comments
class Test_user(unittest.TestCase):

  def test_login(self):
    user = Users('Boli', '12345678', 'user')
    user.create_user()
    self.assertEqual(user.login('Boli','12345678'),"Logged in successfully")

  def test_comment(self):
    user = Users('Boli', '12345678', 'user')
    user.login('Boli','12345678')
    user.create_user()
    comment = Comments('What is github?')
    self.assertEqual(comment.make_comment(),"comment successfully added")

  def test_edit_comment(self):
    user = Users('Boli', '12345678', 'user')
    user.login('Boli','12345678')
    user.create_user()
    comment = Comments('What is github?')
    self.assertEqual(comment.edit_comment('Me no understand this', 1),"comment edited successfully")

  def test_delete_comment(self):
    user = Users('Boli', '12345678', 'user')
    user.login('Boli','12345678')
    user.create_user()
    comment = Comments('What is github?')
    user.logout()
    admin_user = Users('Mike', 'admin', 'admin')
    admin_user.create_user()
    admin_user.login('Mike', 'admin')
    
    self.assertEqual(comment.delete_comment(1),"comment deleted successfully")