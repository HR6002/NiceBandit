import unittest
from LoginScreen import*
class LoginScreenCheck(unittest.TestCase):
    def test_binary_search(self):
        self.assertFalse(binary_search(store_10k(), "verycomplexpasssswourd22"))
        self.assertTrue(binary_search(store_10k(), "qwertyui"))
        self.assertFalse(binary_search(store_10k(), "complexpassword"))
        self.assertFalse(binary_search(store_10k(), "complespassword"))
    def test_check_password(self):
        self.assertFalse(check_password("password"))
        self.assertFalse(check_password("complespassword"))
        self.assertFalse(check_password("complespassword!"))
        self.assertFalse(check_password("complespassword!132"))
        self.assertTrue(check_password("Complespassword!124876"))
        self.assertFalse(check_password("Complespassword!123"))
    def test_format_password(self):
        self.assertEqual(format_password("password123!!^*&^&*^"),"password")
        self.assertEqual(format_password("123passw33213ord123!!^*&^&*^"),"password")
    def test_consecutive_numbers(self):
        self.assertTrue(check_consequitivenumbers("password1234"))
        self.assertTrue(check_consequitivenumbers("password6789"))
        self.assertTrue(check_consequitivenumbers("1234password"))
        self.assertTrue(check_consequitivenumbers("password9999"))

















if __name__ == '__main__':
    unittest.main()