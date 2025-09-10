from tests import SignupTests
from playwright.sync_api import sync_playwright

if __name__ == "__main__":
    with sync_playwright() as playwright:
        print("\n\n-----------------------------------------\nRunning tests for Mentee...\n-------------------------------\n\n")
        tests = SignupTests(playwright, "mentee")
        print("\n\n-----------------------------------------\nRunning test_signup...\n-------------------------------\n\n")
        tests.test_signup()
        print("\n\n-----------------------------------------\nRunning test_signup_with_google...\n-------------------------------\n\n")
        tests.test_signup_with_google()
        print("\n\n-----------------------------------------\nRunning test_signup_with_linkedin...\n-------------------------------\n\n")
        tests.test_signup_with_linkedin()

        print("\n\n-----------------------------------------\nRunning tests for Mentor...\n-------------------------------\n\n")
        tests = SignupTests(playwright, "mentor")
        print("\n\n-----------------------------------------\nRunning test_signup...\n-------------------------------\n\n")
        tests.test_signup()
        print("\n\n-----------------------------------------\nRunning test_signup_with_google...\n-------------------------------\n\n")
        tests.test_signup_with_google()
        print("\n\n-----------------------------------------\nRunning test_signup_with_linkedin...\n-------------------------------\n\n")
        tests.test_signup_with_linkedin()
