from tests import SignupTests, LoginTests
from playwright.sync_api import sync_playwright

if __name__ == "__main__":
    with sync_playwright() as playwright:

        print("\n\n-----------------------------------------\nRunning Sign Up tests for Mentee...\n-------------------------------\n\n")
        signup_mentee_tests = SignupTests(playwright, "mentee")
        print("\n\n-----------------------------------------\nRunning test_signup...\n-------------------------------\n\n")
        signup_mentee_tests.test_signup()
        print("\n\n-----------------------------------------\nRunning test_signup_with_google...\n-------------------------------\n\n")
        signup_mentee_tests.test_signup_with_google()
        print("\n\n-----------------------------------------\nRunning test_signup_with_linkedin...\n-------------------------------\n\n")
        signup_mentee_tests.test_signup_with_linkedin()

        print("\n\n-----------------------------------------\nRunning Sign Up tests for Mentor...\n-------------------------------\n\n")
        signup_mentor_tests = SignupTests(playwright, "mentor")
        print("\n\n-----------------------------------------\nRunning test_signup...\n-------------------------------\n\n")
        signup_mentor_tests.test_signup()
        print("\n\n-----------------------------------------\nRunning test_signup_with_google...\n-------------------------------\n\n")
        signup_mentor_tests.test_signup_with_google()
        print("\n\n-----------------------------------------\nRunning test_signup_with_linkedin...\n-------------------------------\n\n")
        signup_mentor_tests.test_signup_with_linkedin()
        
        
        print("\n\n-----------------------------------------\nRunning LogIn tests for Mentee...\n-------------------------------\n\n")
        login_mentee_tests = LoginTests(playwright)
        print("\n\n-----------------------------------------\nRunning test_login...\n-------------------------------\n\n")
        login_mentee_tests.test_login()
        print("\n\n-----------------------------------------\nRunning signout...\n-------------------------------\n\n")
        login_mentee_tests.signout()
        print("\n\n-----------------------------------------\nRunning test_login_with_google...\n-------------------------------\n\n")
        login_mentee_tests.test_login_with_google()
        print("\n\n-----------------------------------------\nRunning test_login_with_linkedin...\n-------------------------------\n\n")
        login_mentee_tests.test_login_with_linkedin()

        print("\n\n-----------------------------------------\nRunning LogIn tests for Mentor...\n-------------------------------\n\n")
        login_mentor_tests = LoginTests(playwright)
        print("\n\n-----------------------------------------\nRunning test_login...\n-------------------------------\n\n")
        login_mentor_tests.test_login()
        print("\n\n-----------------------------------------\nRunning test_login_with_google...\n-------------------------------\n\n")
        login_mentor_tests.test_login_with_google()
        print("\n\n-----------------------------------------\nRunning test_login_with_linkedin...\n-------------------------------\n\n")
        login_mentor_tests.test_login_with_linkedin()   
