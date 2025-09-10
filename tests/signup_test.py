import re
from config import Config
from utils.test_utils import ValidationHelper
from tests.basetest import BaseTest
from playwright.sync_api import TimeoutError


class SignupTests(BaseTest):
    def __init__(self, playwright, role):
        self.playwright = playwright
        super().setup()
        self.role = role

    def test_signup(self):
        try:
            self.page.goto(Config.baseUrl)
            self.page.click("text=Sign Up")
            if self.role == "mentor":
                mentor_button = self.page.get_by_role(
                    "button", name=re.compile(r"^mentor$", re.I)
                ).first
                mentor_button.click()

            self.page.fill("input[name='first_name']",Config.firstName)
            self.page.fill("input[name='last_name']",Config.lastName)
            self.page.fill("input[name='email']",Config.email)
            self.page.fill("input[name='password']",Config.password)

            self.page.click("button[type='submit']")

            required_fields = [
                "input[name='first_name']",
                "input[name='last_name']",
                "input[name='email']",
                "input[name='password']"
            ]
            ValidationHelper.check_required_validations(self.page, required_fields)

            self.page.wait_for_timeout(3000)
            role_locator = self.page.locator("div[role='status'], [aria-live]")
            for i in range(role_locator.count()):
                text = role_locator.nth(i).inner_text().strip()
                if text:
                    print(f"[notification] {text}")

        except TimeoutError as e:
            print(f"[error] Timeout occurred: {e}")
            print(f"[debug] Current URL at timeout: {self.page.url}")


    def test_signup_with_google(self):
        try:
            self.page.goto(Config.baseUrl)
            self.page.click("text=Sign Up")
            if self.role == "mentor":
                mentor_button = self.page.get_by_role(
                    "button", name=re.compile(r"^mentor$", re.I)
                ).first
                mentor_button.click()

            google_button = self.page.get_by_role(
                "button", name=re.compile(r"signup with google", re.I)
            ).first
            google_button.click()
            print("[action] Clicked Signup with Google button")

            self.page.wait_for_url("**/accounts.google.com/**", timeout=100000)
            print("[debug] Navigated to Google login page")

            email_input = self.page.locator('input[type="email"]')
            email_input.wait_for(timeout=5000)
            email_input.fill(Config.gmail)
            print(f"[action] Entered email: {Config.gmail}")

            next_button = self.page.locator('button:has-text("Next")').first
            next_button.click()
            print("[action] Clicked Next button")

            self.page.wait_for_timeout(2000)

            password_input = self.page.locator('input[type="password"]')
            password_input.wait_for(timeout=5000)
            password_input.fill(Config.google_password)
            print("[action] Entered password")

            password_next_button = self.page.locator('button:has-text("Next")').first
            password_next_button.click()
            print("[action] Clicked Next button after password")

            self.page.wait_for_timeout(5000)

            current_url = self.page.url
            print(f"[debug] Current URL after login: {current_url}")

            if "accounts.google.com" in current_url and "consent" in current_url:
                print("[debug] On Google consent screen")
                try:
                    continue_button = self.page.locator(
                        'button:has-text("Continue"), button:has-text("Allow")'
                    ).first
                    continue_button.click()
                    print("[action] Clicked consent button")
                except:
                    print("[debug] No consent button found")

            self.page.wait_for_timeout(5000)
            print(f"[debug] Final URL: {self.page.url}")

        except TimeoutError as e:
            print(f"[error] Timeout occurred: {e}")
            print(f"[debug] Current URL at timeout: {self.page.url}")
        except Exception as e:
            print(f"[error] An error occurred: {e}")
            print(f"[debug] Current URL at error: {self.page.url}")

    def test_signup_with_linkedin(self):
        try:
            self.page.goto(Config.baseUrl)
            self.page.click("text=Sign Up")
            if self.role == "mentor":
                mentor_button = self.page.get_by_role(
                    "button", name=re.compile(r"^mentor$", re.I)
                ).first
                mentor_button.click()

            linkedin_button = self.page.get_by_role(
                "button", name=re.compile(r"signup with linkedin", re.I)
            ).first
            linkedin_button.click()
            print("[action] Clicked Signup with LinkedIn button")

            self.page.wait_for_url("**/www.linkedin.com/**", timeout=10000)
            print("[debug] Navigated to LinkedIn login page")

            email_input = self.page.locator('input[id="username"]')
            email_input.wait_for(timeout=5000)
            email_input.fill(Config.linkedin_email)
            print(f"[action] Entered email: {Config.linkedin_email}")

            password_input = self.page.locator('input[id="password"]')
            password_input.wait_for(timeout=5000)
            password_input.fill(Config.linkedin_password)
            print("[action] Entered password")

            next_button = self.page.locator('button:has-text("Sign in")').first
            next_button.click()
            print("[action] Clicked \"Sign in\" button after password")

            self.page.wait_for_timeout(5000)
            current_url = self.page.url
            print(f"[debug] Current URL after login: {current_url}")

            if "accounts.google.com" in current_url and "consent" in current_url:
                print("[debug] On Google consent screen")
                try:
                    continue_button = self.page.locator(
                        'button:has-text("Continue"), button:has-text("Allow")'
                    ).first
                    continue_button.click()
                    print("[action] Clicked consent button")
                except:
                    print("[debug] No consent button found")

            self.page.wait_for_timeout(5000)
            print(f"[debug] Final URL: {self.page.url}")

        except TimeoutError as e:
            print(f"[error] Timeout occurred: {e}")
            print(f"[debug] Current URL at timeout: {self.page.url}")
        except Exception as e:
            print(f"[error] An error occurred: {e}")
            print(f"[debug] Current URL at error: {self.page.url}")
       
    def __del__(self):
        super().teardown()
