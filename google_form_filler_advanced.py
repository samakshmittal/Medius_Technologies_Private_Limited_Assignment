"""
Google Form Auto-Filler - Advanced Version
Includes configuration support, logging, and advanced features
"""

import time
import random
import os
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Import configuration
try:
    from config import *
except ImportError:
    print("⚠️ Config file not found. Using default settings.")
    # Default settings
    class Config:
        BROWSER_SETTINGS = {'headless': False, 'maximize': True, 'wait_time': 10}
        DELAYS = {'between_fields': 0.5, 'after_click': 0.3, 'page_load': 2, 'before_submit': 2, 'after_submit': 3}
        SAMPLE_NAMES = ["Raj Kumar", "Priya Sharma", "Amit Patel"]
        SAMPLE_EMAILS_DOMAIN = "example.com"
        EMAIL_PREFIX = "testuser"
        PHONE_MIN = 6000000000
        PHONE_MAX = 9999999999
        AGE_MIN = 18
        AGE_MAX = 99
        SAMPLE_SHORT_TEXTS = ["Sample Answer", "Test Response"]
        SAMPLE_LONG_TEXTS = ["This is a detailed response."]
        CHECKBOX_MIN_SELECT = 1
        CHECKBOX_MAX_SELECT = 3
        AUTO_SUBMIT = True
        VERBOSE = True
        CONTINUE_ON_ERROR = True
        SCREENSHOT_ON_ERROR = False
    
    BROWSER_SETTINGS = Config.BROWSER_SETTINGS
    DELAYS = Config.DELAYS
    SAMPLE_NAMES = Config.SAMPLE_NAMES
    SAMPLE_EMAILS_DOMAIN = Config.SAMPLE_EMAILS_DOMAIN
    EMAIL_PREFIX = Config.EMAIL_PREFIX
    PHONE_MIN = Config.PHONE_MIN
    PHONE_MAX = Config.PHONE_MAX
    AGE_MIN = Config.AGE_MIN
    AGE_MAX = Config.AGE_MAX
    SAMPLE_SHORT_TEXTS = Config.SAMPLE_SHORT_TEXTS
    SAMPLE_LONG_TEXTS = Config.SAMPLE_LONG_TEXTS
    CHECKBOX_MIN_SELECT = Config.CHECKBOX_MIN_SELECT
    CHECKBOX_MAX_SELECT = Config.CHECKBOX_MAX_SELECT
    AUTO_SUBMIT = Config.AUTO_SUBMIT
    VERBOSE = Config.VERBOSE
    CONTINUE_ON_ERROR = Config.CONTINUE_ON_ERROR
    SCREENSHOT_ON_ERROR = Config.SCREENSHOT_ON_ERROR


class GoogleFormFillerAdvanced:
    def __init__(self, form_url, config=None):
        self.form_url = form_url
        self.driver = None
        self.filled_fields = 0
        self.errors = []
        self.start_time = None
        
    def log(self, message, level="INFO"):
        """Log messages with timestamp"""
        if VERBOSE or level == "ERROR":
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] {level}: {message}")
            
    def take_screenshot(self, name="error"):
        """Take screenshot for debugging"""
        if self.driver:
            try:
                filename = f"screenshot_{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                self.driver.save_screenshot(filename)
                self.log(f"Screenshot saved: {filename}", "INFO")
            except Exception as e:
                self.log(f"Failed to take screenshot: {e}", "ERROR")
                
    def setup_driver(self):
        """Setup Chrome driver with custom options"""
        self.log("Setting up browser...", "INFO")
        chrome_options = Options()
        
        if BROWSER_SETTINGS.get('headless', False):
            chrome_options.add_argument('--headless')
            self.log("Running in headless mode", "INFO")
            
        if BROWSER_SETTINGS.get('maximize', True):
            chrome_options.add_argument('--start-maximized')
            
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            self.log("Browser setup complete", "INFO")
        except Exception as e:
            self.log(f"Failed to setup browser: {e}", "ERROR")
            raise
            
    def open_form(self):
        """Open the Google Form"""
        self.log(f"Opening form: {self.form_url}", "INFO")
        try:
            self.driver.get(self.form_url)
            time.sleep(DELAYS['page_load'])
            self.log("Form loaded successfully", "INFO")
        except Exception as e:
            self.log(f"Failed to open form: {e}", "ERROR")
            raise
            
    def generate_email(self):
        """Generate random email"""
        domains = globals().get('EMAIL_DOMAINS', ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com'])
        return f"{globals().get('EMAIL_PREFIX', 'user')}{random.randint(1, 99999)}@{random.choice(domains)}"
        
    def generate_random_name(self):
        """Generate random name"""
        first_names = globals().get('FIRST_NAMES', ['Raj', 'Priya', 'Amit', 'Sneha'])
        last_names = globals().get('LAST_NAMES', ['Kumar', 'Sharma', 'Patel', 'Singh'])
        return f"{random.choice(first_names)} {random.choice(last_names)}"
        
    def generate_random_short_text(self):
        """Generate random short text"""
        prefixes = globals().get('SHORT_TEXT_PREFIXES', ['Response', 'Answer', 'Reply'])
        suffixes = globals().get('SHORT_TEXT_SUFFIXES', ['123', '456', '789'])
        return f"{random.choice(prefixes)}{random.choice(suffixes)}{random.randint(1, 999)}"
        
    def generate_random_paragraph(self):
        """Generate random paragraph"""
        words = globals().get('RANDOM_WORDS', ['This', 'is', 'a', 'test', 'response'])
        return ' '.join(random.choices(words, k=random.randint(15, 30)))
        
    def generate_phone(self):
        """Generate random phone number"""
        phone = str(random.randint(PHONE_MIN, PHONE_MAX))
        if 'PHONE_PREFIX' in globals() and PHONE_PREFIX:
            phone = PHONE_PREFIX + phone
        return phone
        
    def generate_age(self):
        """Generate random age"""
        return str(random.randint(AGE_MIN, AGE_MAX))
        
    def fill_text_fields(self):
        """Fill all text input fields"""
        try:
            text_inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
            self.log(f"Found {len(text_inputs)} text input fields", "INFO")
            
            for idx, input_field in enumerate(text_inputs):
                try:
                    if input_field.is_displayed() and input_field.is_enabled():
                        # Get question context
                        try:
                            parent = input_field.find_element(By.XPATH, './ancestor::div[contains(@class, "Qr7Oae")]')
                            question = parent.text.lower()
                        except:
                            question = ""
                        
                        # Smart filling based on question
                        if 'email' in question or 'mail' in question or 'e-mail' in question:
                            text = self.generate_email()
                        elif 'phone' in question or 'mobile' in question or 'contact' in question or 'number' in question:
                            text = self.generate_phone()
                        elif 'name' in question:
                            text = self.generate_random_name()
                        elif 'age' in question:
                            text = self.generate_age()
                        else:
                            text = self.generate_random_short_text()
                        
                        input_field.clear()
                        input_field.send_keys(text)
                        self.filled_fields += 1
                        self.log(f"✅ Filled text field {idx + 1}: {text[:30]}", "INFO")
                        time.sleep(DELAYS['between_fields'])
                        
                except Exception as e:
                    error_msg = f"Failed to fill text field {idx + 1}: {str(e)}"
                    self.log(error_msg, "ERROR")
                    self.errors.append(error_msg)
                    if SCREENSHOT_ON_ERROR:
                        self.take_screenshot(f"text_field_{idx}")
                    if not CONTINUE_ON_ERROR:
                        raise
                        
        except Exception as e:
            self.log(f"Error in fill_text_fields: {str(e)}", "ERROR")
            if not CONTINUE_ON_ERROR:
                raise
                
    def fill_textarea_fields(self):
        """Fill all textarea fields"""
        try:
            textareas = self.driver.find_elements(By.CSS_SELECTOR, 'textarea')
            self.log(f"Found {len(textareas)} textarea fields", "INFO")
            
            for idx, textarea in enumerate(textareas):
                try:
                    if textarea.is_displayed() and textarea.is_enabled():
                        text = self.generate_random_paragraph()
                        textarea.clear()
                        textarea.send_keys(text)
                        self.filled_fields += 1
                        self.log(f"✅ Filled textarea {idx + 1}", "INFO")
                        time.sleep(DELAYS['between_fields'])
                        
                except Exception as e:
                    error_msg = f"Failed to fill textarea {idx + 1}: {str(e)}"
                    self.log(error_msg, "ERROR")
                    self.errors.append(error_msg)
                    if SCREENSHOT_ON_ERROR:
                        self.take_screenshot(f"textarea_{idx}")
                    if not CONTINUE_ON_ERROR:
                        raise
                        
        except Exception as e:
            self.log(f"Error in fill_textarea_fields: {str(e)}", "ERROR")
            if not CONTINUE_ON_ERROR:
                raise
                
    def select_radio_buttons(self):
        """Select radio button options"""
        try:
            radio_groups = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"]')
            self.log(f"Found {len(radio_groups)} radio button groups", "INFO")
            
            for idx, group in enumerate(radio_groups):
                try:
                    radio_options = group.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
                    
                    if radio_options:
                        selected_option = random.choice(radio_options)
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", selected_option)
                        time.sleep(DELAYS['after_click'])
                        selected_option.click()
                        self.filled_fields += 1
                        self.log(f"✅ Selected radio option in group {idx + 1}", "INFO")
                        time.sleep(DELAYS['between_fields'])
                        
                except Exception as e:
                    error_msg = f"Failed to select radio in group {idx + 1}: {str(e)}"
                    self.log(error_msg, "ERROR")
                    self.errors.append(error_msg)
                    if SCREENSHOT_ON_ERROR:
                        self.take_screenshot(f"radio_{idx}")
                    if not CONTINUE_ON_ERROR:
                        raise
                        
        except Exception as e:
            self.log(f"Error in select_radio_buttons: {str(e)}", "ERROR")
            if not CONTINUE_ON_ERROR:
                raise
                
    def select_checkboxes(self):
        """Select checkbox options"""
        try:
            checkbox_groups = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="list"]')
            self.log(f"Found {len(checkbox_groups)} checkbox groups", "INFO")
            
            for idx, group in enumerate(checkbox_groups):
                try:
                    checkboxes = group.find_elements(By.CSS_SELECTOR, 'div[role="checkbox"]')
                    
                    if checkboxes:
                        num_to_select = random.randint(
                            CHECKBOX_MIN_SELECT, 
                            min(CHECKBOX_MAX_SELECT, len(checkboxes))
                        )
                        selected_boxes = random.sample(checkboxes, num_to_select)
                        
                        for checkbox in selected_boxes:
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
                            time.sleep(DELAYS['after_click'])
                            checkbox.click()
                            time.sleep(DELAYS['after_click'])
                        
                        self.filled_fields += 1
                        self.log(f"✅ Selected {num_to_select} checkbox(es) in group {idx + 1}", "INFO")
                        time.sleep(DELAYS['between_fields'])
                        
                except Exception as e:
                    error_msg = f"Failed to select checkboxes in group {idx + 1}: {str(e)}"
                    self.log(error_msg, "ERROR")
                    self.errors.append(error_msg)
                    if SCREENSHOT_ON_ERROR:
                        self.take_screenshot(f"checkbox_{idx}")
                    if not CONTINUE_ON_ERROR:
                        raise
                        
        except Exception as e:
            self.log(f"Error in select_checkboxes: {str(e)}", "ERROR")
            if not CONTINUE_ON_ERROR:
                raise
                
    def select_dropdowns(self):
        """Select dropdown options"""
        try:
            dropdowns = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="listbox"]')
            self.log(f"Found {len(dropdowns)} dropdown menus", "INFO")
            
            for idx, dropdown in enumerate(dropdowns):
                try:
                    if dropdown.is_displayed():
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
                        time.sleep(DELAYS['after_click'])
                        dropdown.click()
                        time.sleep(DELAYS['between_fields'])
                        
                        options = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="option"]')
                        
                        if len(options) > 1:
                            # Skip first option if configured
                            start_idx = 1 if globals().get('SKIP_FIRST_OPTION', True) else 0
                            selected_option = random.choice(options[start_idx:])
                            selected_option.click()
                            self.filled_fields += 1
                            self.log(f"✅ Selected dropdown option in dropdown {idx + 1}", "INFO")
                            time.sleep(DELAYS['between_fields'])
                            
                except Exception as e:
                    error_msg = f"Failed to select dropdown {idx + 1}: {str(e)}"
                    self.log(error_msg, "ERROR")
                    self.errors.append(error_msg)
                    if SCREENSHOT_ON_ERROR:
                        self.take_screenshot(f"dropdown_{idx}")
                    if not CONTINUE_ON_ERROR:
                        raise
                        
        except Exception as e:
            self.log(f"Error in select_dropdowns: {str(e)}", "ERROR")
            if not CONTINUE_ON_ERROR:
                raise
                
    def fill_linear_scale(self):
        """Fill linear scale questions"""
        try:
            scale_groups = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"].lLfZXe')
            self.log(f"Found {len(scale_groups)} linear scale questions", "INFO")
            
            for idx, scale in enumerate(scale_groups):
                try:
                    scale_options = scale.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
                    
                    if scale_options:
                        selected_option = random.choice(scale_options)
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", selected_option)
                        time.sleep(DELAYS['after_click'])
                        selected_option.click()
                        self.filled_fields += 1
                        self.log(f"✅ Selected linear scale option {idx + 1}", "INFO")
                        time.sleep(DELAYS['between_fields'])
                        
                except Exception as e:
                    error_msg = f"Failed to select scale option {idx + 1}: {str(e)}"
                    self.log(error_msg, "ERROR")
                    self.errors.append(error_msg)
                    if SCREENSHOT_ON_ERROR:
                        self.take_screenshot(f"scale_{idx}")
                    if not CONTINUE_ON_ERROR:
                        raise
                        
        except Exception as e:
            self.log(f"Error in fill_linear_scale: {str(e)}", "ERROR")
            if not CONTINUE_ON_ERROR:
                raise
                
    def fill_date_fields(self):
        """Fill date input fields"""
        try:
            date_inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="date"]')
            self.log(f"Found {len(date_inputs)} date input fields", "INFO")
            
            for idx, date_input in enumerate(date_inputs):
                try:
                    if date_input.is_displayed() and date_input.is_enabled():
                        # Generate a random date within the configured range
                        start_date = datetime.now() - timedelta(days=365*globals().get('DATE_RANGE_YEARS', 5))
                        end_date = datetime.now() + timedelta(days=globals().get('DATE_START_OFFSET_DAYS', 0))
                        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
                        
                        # Format date as MM/DD/YYYY for Google Forms
                        date_string = random_date.strftime("%m/%d/%Y")
                        
                        # Clear and fill the date field
                        date_input.clear()
                        date_input.send_keys(date_string)
                        self.filled_fields += 1
                        self.log(f"✅ Filled date field {idx + 1}: {date_string}", "INFO")
                        time.sleep(DELAYS['between_fields'])
                        
                except Exception as e:
                    error_msg = f"Failed to fill date field {idx + 1}: {str(e)}"
                    self.log(error_msg, "ERROR")
                    self.errors.append(error_msg)
                    if SCREENSHOT_ON_ERROR:
                        self.take_screenshot(f"date_field_{idx}")
                    if not CONTINUE_ON_ERROR:
                        raise
                        
        except Exception as e:
            self.log(f"Error in fill_date_fields: {str(e)}", "ERROR")
            if not CONTINUE_ON_ERROR:
                raise
                
    def fill_time_fields(self):
        """Fill time input fields"""
        try:
            time_inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="time"]')
            self.log(f"Found {len(time_inputs)} time input fields", "INFO")
            
            for idx, time_input in enumerate(time_inputs):
                try:
                    if time_input.is_displayed() and time_input.is_enabled():
                        # Generate a random time using configuration
                        hour = random.randint(
                            globals().get('TIME_START_HOUR', 9), 
                            globals().get('TIME_END_HOUR', 18)
                        )
                        minute = random.choice(globals().get('TIME_MINUTES', [0, 15, 30, 45]))
                        
                        # Format time as HH:MM for HTML time input
                        time_string = f"{hour:02d}:{minute:02d}"
                        
                        # Clear and fill the time field
                        time_input.clear()
                        time_input.send_keys(time_string)
                        self.filled_fields += 1
                        self.log(f"✅ Filled time field {idx + 1}: {time_string}", "INFO")
                        time.sleep(DELAYS['between_fields'])
                        
                except Exception as e:
                    error_msg = f"Failed to fill time field {idx + 1}: {str(e)}"
                    self.log(error_msg, "ERROR")
                    self.errors.append(error_msg)
                    if SCREENSHOT_ON_ERROR:
                        self.take_screenshot(f"time_field_{idx}")
                    if not CONTINUE_ON_ERROR:
                        raise
                        
        except Exception as e:
            self.log(f"Error in fill_time_fields: {str(e)}", "ERROR")
            if not CONTINUE_ON_ERROR:
                raise
                
    def fill_datetime_fields(self):
        """Fill datetime-local input fields"""
        try:
            datetime_inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="datetime-local"]')
            self.log(f"Found {len(datetime_inputs)} datetime input fields", "INFO")
            
            for idx, datetime_input in enumerate(datetime_inputs):
                try:
                    if datetime_input.is_displayed() and datetime_input.is_enabled():
                        # Generate a random datetime within the configured range
                        start_date = datetime.now() - timedelta(days=365*globals().get('DATETIME_RANGE_YEARS', 2))
                        end_date = datetime.now()
                        random_datetime = start_date + timedelta(
                            days=random.randint(0, (end_date - start_date).days),
                            hours=random.randint(
                                globals().get('TIME_START_HOUR', 9), 
                                globals().get('TIME_END_HOUR', 18)
                            ),
                            minutes=random.choice(globals().get('TIME_MINUTES', [0, 15, 30, 45]))
                        )
                        
                        # Format datetime as MM/DD/YYYY HH:MM for Google Forms
                        datetime_string = random_datetime.strftime("%m/%d/%Y %H:%M")
                        
                        # Clear and fill the datetime field
                        datetime_input.clear()
                        datetime_input.send_keys(datetime_string)
                        self.filled_fields += 1
                        self.log(f"✅ Filled datetime field {idx + 1}: {datetime_string}", "INFO")
                        time.sleep(DELAYS['between_fields'])
                        
                except Exception as e:
                    error_msg = f"Failed to fill datetime field {idx + 1}: {str(e)}"
                    self.log(error_msg, "ERROR")
                    self.errors.append(error_msg)
                    if SCREENSHOT_ON_ERROR:
                        self.take_screenshot(f"datetime_field_{idx}")
                    if not CONTINUE_ON_ERROR:
                        raise
                        
        except Exception as e:
            self.log(f"Error in fill_datetime_fields: {str(e)}", "ERROR")
            if not CONTINUE_ON_ERROR:
                raise
                
    def submit_form(self):
        """Submit the form"""
        if not AUTO_SUBMIT:
            self.log("Auto-submit disabled. Skipping submission.", "INFO")
            return False
            
        try:
            self.log("Attempting to submit form...", "INFO")
            time.sleep(DELAYS['before_submit'])
            
            # Try multiple selectors for submit button
            submit_selectors = [
                'span[jsname="V67aGc"]',
                'div[role="button"][jsname="M2UYVd"]',
                'span.uArJ5e.UQuaGc.Y5sE8d.VkkpIf.NqnGTe',
            ]
            
            submit_button = None
            for selector in submit_selectors:
                try:
                    buttons = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for button in buttons:
                        if button.is_displayed() and button.is_enabled():
                            submit_button = button
                            break
                    if submit_button:
                        break
                except:
                    continue
                    
            if submit_button:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
                time.sleep(1)
                submit_button.click()
                self.log("✅ Form submitted successfully!", "INFO")
                time.sleep(DELAYS['after_submit'])
                
                # Check for confirmation
                try:
                    confirmation = self.driver.find_element(By.CSS_SELECTOR, 'div.vHW8K')
                    self.log(f"Confirmation: {confirmation.text}", "INFO")
                except:
                    self.log("Form submitted (confirmation not detected)", "INFO")
                    
                return True
            else:
                self.log("Submit button not found", "ERROR")
                if SCREENSHOT_ON_ERROR:
                    self.take_screenshot("submit_not_found")
                return False
                
        except Exception as e:
            error_msg = f"Error submitting form: {str(e)}"
            self.log(error_msg, "ERROR")
            self.errors.append(error_msg)
            if SCREENSHOT_ON_ERROR:
                self.take_screenshot("submit_error")
            return False
            
    def print_summary(self):
        """Print execution summary"""
        duration = time.time() - self.start_time
        print("\n" + "="*60)
        print("📊 EXECUTION SUMMARY")
        print("="*60)
        print(f"⏱️  Duration: {duration:.2f} seconds")
        print(f"✅ Fields Filled: {self.filled_fields}")
        print(f"❌ Errors: {len(self.errors)}")
        if self.errors:
            print("\n🔍 Error Details:")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. {error}")
        print("="*60 + "\n")
        
    def fill_form(self):
        """Main method to fill the entire form"""
        self.start_time = time.time()
        
        try:
            self.setup_driver()
            self.open_form()
            
            print("\n" + "="*60)
            print("📋 STARTING FORM FILLING PROCESS")
            print("="*60 + "\n")
            
            # Fill different types of fields
            self.fill_text_fields()
            self.fill_textarea_fields()
            self.select_radio_buttons()
            self.select_checkboxes()
            self.select_dropdowns()
            self.fill_linear_scale()
            self.fill_date_fields()
            self.fill_time_fields()
            self.fill_datetime_fields()
            
            print("\n" + "="*60)
            print("✅ Form filling completed!")
            print("="*60 + "\n")
            
            # Submit form
            self.submit_form()
            
            # Print summary
            self.print_summary()
            
            self.log("Process completed successfully!", "INFO")
            print("Browser will close in 5 seconds...")
            time.sleep(5)
            
        except Exception as e:
            self.log(f"Fatal error occurred: {str(e)}", "ERROR")
            if SCREENSHOT_ON_ERROR:
                self.take_screenshot("fatal_error")
            self.print_summary()
            print("Browser will remain open for 10 seconds for inspection...")
            time.sleep(10)
            
        finally:
            if self.driver:
                self.driver.quit()
                self.log("Browser closed.", "INFO")


def main():
    print("="*60)
    print("🤖 Google Form Auto-Filler (Advanced)")
    print("="*60)
    print()
    
    # Display configuration
    print("⚙️  Configuration:")
    print(f"  - Headless mode: {BROWSER_SETTINGS.get('headless', False)}")
    print(f"  - Auto-submit: {AUTO_SUBMIT}")
    print(f"  - Screenshot on error: {SCREENSHOT_ON_ERROR}")
    print(f"  - Continue on error: {CONTINUE_ON_ERROR}")
    print()
    
    # Get form URL
    form_url = input("📝 Enter Google Form URL: ").strip()
    
    if not form_url:
        print("❌ URL cannot be empty!")
        return
        
    # Check for valid Google Form URL patterns
    valid_patterns = ['docs.google.com/forms', 'forms.gle']
    is_valid_form = any(pattern in form_url for pattern in valid_patterns)
    
    if not is_valid_form:
        print("⚠️ Warning: This doesn't look like a Google Form URL")
        print("Supported patterns:")
        print("  - docs.google.com/forms/...")
        print("  - forms.gle/...")
        proceed = input("Continue anyway? (y/n): ").lower()
        if proceed != 'y':
            return
            
    print("\n🚀 Starting form filling process...\n")
    
    # Create filler instance and fill form
    filler = GoogleFormFillerAdvanced(form_url)
    filler.fill_form()
    
    print("\n✅ All done! Thank you for using Google Form Auto-Filler.")


if __name__ == "__main__":
    main()


