import re
from config import Config
from utils.test_utils import ValidationHelper
from tests.basetest import BaseTest
from playwright.sync_api import TimeoutError


class LoginTests(BaseTest):
    def __init__(self, playwright):
        self.playwright = playwright
        super().setup()

    def signout(self):
        
        signout_button = self.page.get_by_role(
                "button", name=re.compile(r"Sign Out", re.I)
            ).first
        if signout_button:
            signout_button.click()
            print("[action] Clicked Sign Out button")
            input("Press Enter to continue...")
        else:
            print("[debug] Sign Out button not found")

    def test_login(self):
        try:
            self.page.goto(Config.baseUrl, timeout=60000)
            self.page.click("text=Login")
            print("[action] Clicked Login link")
            self.page.fill("input[name='email']",Config.email)
            print(f"[action] Entered email: {Config.email}")
            self.page.fill("input[name='password']",Config.password)
            print(f"[action] Entered password: {Config.password}")

            self.page.click("button[type='submit']")

            required_fields = [
                "input[name='email']",
                "input[name='password']"
            ]
            ValidationHelper.check_required_validations(self.page, required_fields)

            self.page.wait_for_timeout(30000)
            role_locator = self.page.locator("div[role='status'], [aria-live]")
            for i in range(role_locator.count()):
                text = role_locator.nth(i).inner_text().strip()
                if text:
                    print(f"[notification] {text}")
            if "dashboard" in self.page.url.lower():
                print("[success] Login successful and redirected to dashboard")
                print("\n-----Signning out--------\n")
                self.signout()
            else:    
                "Login failed or did not redirect to dashboard"        
                print(f"[debug] Current URL after login: {self.page.url}")
            
        except TimeoutError as e:
            print(f"[error] Timeout occurred: {e}")
            print(f"[debug] Current URL at timeout: {self.page.url}")


    def test_login_with_google(self):
        try:
            self.page.goto(Config.baseUrl, timeout=60000)
            self.page.click("text=Login")
            google_button = self.page.get_by_role(
                "button", name=re.compile(r"Sign in with Google", re.I)
            ).first
            google_button.click()
            print("[action] Clicked Sign in with Google button")

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
            if "dashboard" in self.page.url.lower():
                print("[success] Login successful and redirected to dashboard")
                print("\n-----Signning out--------\n")
                self.signout()
            else:    
                "Login failed or did not redirect to dashboard"        
                print(f"[debug] Current URL after login: {self.page.url}")
            

        except TimeoutError as e:
            print(f"[error] Timeout occurred: {e}")
            print(f"[debug] Current URL at timeout: {self.page.url}")
        except Exception as e:
            print(f"[error] An error occurred: {e}")
            print(f"[debug] Current URL at error: {self.page.url}")

    def test_login_with_linkedin(self):
        try:
            self.page.goto(Config.baseUrl, timeout=60000)
            self.page.click("text=Sign Up")
            if self.role == "mentor":
                mentor_button = self.page.get_by_role(
                    "button", name=re.compile(r"^mentor$", re.I)
                ).first
                mentor_button.click()

            linkedin_button = self.page.get_by_role(
                "button", name=re.compile(r"login with linkedin", re.I)
            ).first
            linkedin_button.click()
            print("[action] Clicked login with LinkedIn button")

            self.page.wait_for_url("**/www.linkedin.com/**", timeout=50000)
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
            if "dashboard" in self.page.url.lower():
                print("[success] Login successful and redirected to dashboard")
                print("\n-----Signning out--------\n")
                self.signout()
            else:    
                "Login failed or did not redirect to dashboard"        
                print(f"[debug] Current URL after login: {self.page.url}")
            

        except TimeoutError as e:
            print(f"[error] Timeout occurred: {e}")
            print(f"[debug] Current URL at timeout: {self.page.url}")
        except Exception as e:
            print(f"[error] An error occurred: {e}")
            print(f"[debug] Current URL at error: {self.page.url}")
       
    def __del__(self):
        super().teardown()
