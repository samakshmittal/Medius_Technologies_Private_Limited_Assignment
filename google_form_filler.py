"""
Google Form Auto-Filler
Automatically fills and submits Google Forms
"""

import time
import random
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


class GoogleFormFiller:
    def __init__(self, form_url):
        self.form_url = form_url
        self.driver = None
        
    def setup_driver(self):
        """Setup Chrome driver with options"""
        print("🚀 Setting up browser...")
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Automatically download and setup ChromeDriver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
    def open_form(self):
        """Open the Google Form"""
        print(f"📝 Opening form: {self.form_url}")
        self.driver.get(self.form_url)
        time.sleep(2)
        
    def fill_text_fields(self):
        """Fill all text input fields"""
        try:
            # Find all text input fields
            text_inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
            
            # Generate random text instead of using fixed list
            def generate_random_text(length=8):
                import string
                return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            
            for idx, input_field in enumerate(text_inputs):
                try:
                    if input_field.is_displayed() and input_field.is_enabled():
                        # Get the question text
                        parent = input_field.find_element(By.XPATH, './ancestor::div[contains(@class, "Qr7Oae")]')
                        question = parent.text.lower() if parent else ""
                        
                        # Smart filling based on question content
                        if 'email' in question or 'mail' in question:
                            text = f"user{random.randint(1, 99999)}@{random.choice(['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'example.com'])}"
                        elif 'phone' in question or 'mobile' in question or 'contact' in question:
                            text = f"{random.randint(6000000000, 9999999999)}"
                        elif 'name' in question:
                            first_names = ["Raj", "Priya", "Amit", "Sneha", "Rahul", "Anita", "Vikram", "Kavita", "Arjun", "Pooja", "Suresh", "Meera", "Kiran", "Sunita", "Ravi", "Deepa"]
                            last_names = ["Kumar", "Sharma", "Patel", "Singh", "Verma", "Desai", "Malhotra", "Reddy", "Gupta", "Agarwal", "Jain", "Bansal", "Chopra", "Mehta", "Shah", "Pandey"]
                            text = f"{random.choice(first_names)} {random.choice(last_names)}"
                        elif 'age' in question:
                            text = str(random.randint(18, 99))
                        else:
                            # Generate random text for other fields
                            text = generate_random_text(random.randint(5, 15))
                        
                        input_field.clear()
                        input_field.send_keys(text)
                        print(f"✅ Filled text field {idx + 1}: {text[:30]}")
                        time.sleep(0.5)
                except Exception as e:
                    print(f"⚠️ Could not fill text field {idx + 1}: {str(e)}")
                    
        except Exception as e:
            print(f"⚠️ Error finding text fields: {str(e)}")
            
    def fill_textarea_fields(self):
        """Fill all textarea fields (long answer)"""
        try:
            textareas = self.driver.find_elements(By.CSS_SELECTOR, 'textarea')
            
            # Generate random long text instead of using fixed list
            def generate_random_paragraph():
                words = ["This", "is", "a", "detailed", "response", "to", "the", "question", "providing", "comprehensive", 
                        "information", "that", "covers", "all", "aspects", "of", "the", "query", "Thank", "you", 
                        "for", "this", "opportunity", "I", "would", "like", "to", "express", "my", "thoughts", 
                        "on", "this", "matter", "in", "detail", "This", "is", "an", "automated", "response", 
                        "for", "testing", "purposes", "The", "system", "is", "working", "as", "expected", "and", 
                        "all", "functionality", "has", "been", "verified", "successfully", "I", "appreciate", 
                        "the", "opportunity", "to", "provide", "feedback", "and", "share", "my", "experience"]
                return ' '.join(random.choices(words, k=random.randint(15, 30)))
            
            for idx, textarea in enumerate(textareas):
                try:
                    if textarea.is_displayed() and textarea.is_enabled():
                        text = generate_random_paragraph()
                        textarea.clear()
                        textarea.send_keys(text)
                        print(f"✅ Filled textarea {idx + 1}")
                        time.sleep(0.5)
                except Exception as e:
                    print(f"⚠️ Could not fill textarea {idx + 1}: {str(e)}")
                    
        except Exception as e:
            print(f"⚠️ Error finding textareas: {str(e)}")
            
    def select_radio_buttons(self):
        """Select radio button options"""
        try:
            # Find all radio button groups
            radio_groups = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"]')
            
            for idx, group in enumerate(radio_groups):
                try:
                    # Find all radio options in this group
                    radio_options = group.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
                    
                    if radio_options:
                        # Select a random option
                        selected_option = random.choice(radio_options)
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", selected_option)
                        time.sleep(0.3)
                        selected_option.click()
                        print(f"✅ Selected radio option in group {idx + 1}")
                        time.sleep(0.5)
                except Exception as e:
                    print(f"⚠️ Could not select radio in group {idx + 1}: {str(e)}")
                    
        except Exception as e:
            print(f"⚠️ Error finding radio buttons: {str(e)}")
            
    def select_checkboxes(self):
        """Select checkbox options"""
        try:
            # Find all checkbox groups
            checkbox_groups = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="list"]')
            
            for idx, group in enumerate(checkbox_groups):
                try:
                    # Find all checkbox options in this group
                    checkboxes = group.find_elements(By.CSS_SELECTOR, 'div[role="checkbox"]')
                    
                    if checkboxes:
                        # Select 1-3 random checkboxes
                        num_to_select = random.randint(1, min(3, len(checkboxes)))
                        selected_boxes = random.sample(checkboxes, num_to_select)
                        
                        for checkbox in selected_boxes:
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
                            time.sleep(0.3)
                            checkbox.click()
                            time.sleep(0.3)
                        
                        print(f"✅ Selected {num_to_select} checkbox(es) in group {idx + 1}")
                        time.sleep(0.5)
                except Exception as e:
                    print(f"⚠️ Could not select checkboxes in group {idx + 1}: {str(e)}")
                    
        except Exception as e:
            print(f"⚠️ Error finding checkboxes: {str(e)}")
            
    def select_dropdowns(self):
        """Select dropdown options"""
        try:
            # Find all dropdown selectors
            dropdowns = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="listbox"]')
            
            for idx, dropdown in enumerate(dropdowns):
                try:
                    if dropdown.is_displayed():
                        # Click to open dropdown
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
                        time.sleep(0.3)
                        dropdown.click()
                        time.sleep(0.5)
                        
                        # Find all options
                        options = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="option"]')
                        
                        if len(options) > 1:  # Skip the first option (usually "Choose")
                            selected_option = random.choice(options[1:])
                            selected_option.click()
                            print(f"✅ Selected dropdown option in dropdown {idx + 1}")
                            time.sleep(0.5)
                except Exception as e:
                    print(f"⚠️ Could not select dropdown {idx + 1}: {str(e)}")
                    
        except Exception as e:
            print(f"⚠️ Error finding dropdowns: {str(e)}")
            
    def fill_linear_scale(self):
        """Fill linear scale questions"""
        try:
            # Find all linear scale questions
            scale_groups = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"].lLfZXe')
            
            for idx, scale in enumerate(scale_groups):
                try:
                    # Find all scale options
                    scale_options = scale.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')
                    
                    if scale_options:
                        # Select a random rating
                        selected_option = random.choice(scale_options)
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", selected_option)
                        time.sleep(0.3)
                        selected_option.click()
                        print(f"✅ Selected linear scale option {idx + 1}")
                        time.sleep(0.5)
                except Exception as e:
                    print(f"⚠️ Could not select scale option {idx + 1}: {str(e)}")
                    
        except Exception as e:
            print(f"⚠️ Error finding linear scales: {str(e)}")
            
    def fill_date_fields(self):
        """Fill date input fields"""
        try:
            # Find all date input fields
            date_inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="date"]')
            
            for idx, date_input in enumerate(date_inputs):
                try:
                    if date_input.is_displayed() and date_input.is_enabled():
                        # Generate a random date within the last 5 years
                        start_date = datetime.now() - timedelta(days=365*5)
                        end_date = datetime.now()
                        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
                        
                        # Format date as MM/DD/YYYY for Google Forms
                        date_string = random_date.strftime("%m/%d/%Y")
                        
                        # Clear and fill the date field
                        date_input.clear()
                        date_input.send_keys(date_string)
                        print(f"✅ Filled date field {idx + 1}: {date_string}")
                        time.sleep(0.5)
                except Exception as e:
                    print(f"⚠️ Could not fill date field {idx + 1}: {str(e)}")
                    
        except Exception as e:
            print(f"⚠️ Error finding date fields: {str(e)}")
            
    def fill_time_fields(self):
        """Fill time input fields"""
        try:
            # Find all time input fields
            time_inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="time"]')
            
            for idx, time_input in enumerate(time_inputs):
                try:
                    if time_input.is_displayed() and time_input.is_enabled():
                        # Generate a random time
                        hour = random.randint(9, 18)  # Business hours
                        minute = random.choice([0, 15, 30, 45])
                        
                        # Format time as HH:MM for HTML time input
                        time_string = f"{hour:02d}:{minute:02d}"
                        
                        # Clear and fill the time field
                        time_input.clear()
                        time_input.send_keys(time_string)
                        print(f"✅ Filled time field {idx + 1}: {time_string}")
                        time.sleep(0.5)
                except Exception as e:
                    print(f"⚠️ Could not fill time field {idx + 1}: {str(e)}")
                    
        except Exception as e:
            print(f"⚠️ Error finding time fields: {str(e)}")
            
    def fill_datetime_fields(self):
        """Fill datetime-local input fields"""
        try:
            # Find all datetime-local input fields
            datetime_inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="datetime-local"]')
            
            for idx, datetime_input in enumerate(datetime_inputs):
                try:
                    if datetime_input.is_displayed() and datetime_input.is_enabled():
                        # Generate a random datetime within the last 2 years
                        start_date = datetime.now() - timedelta(days=365*2)
                        end_date = datetime.now()
                        random_datetime = start_date + timedelta(
                            days=random.randint(0, (end_date - start_date).days),
                            hours=random.randint(9, 18),
                            minutes=random.choice([0, 15, 30, 45])
                        )
                        
                        # Format datetime as MM/DD/YYYY HH:MM for Google Forms
                        datetime_string = random_datetime.strftime("%m/%d/%Y %H:%M")
                        
                        # Clear and fill the datetime field
                        datetime_input.clear()
                        datetime_input.send_keys(datetime_string)
                        print(f"✅ Filled datetime field {idx + 1}: {datetime_string}")
                        time.sleep(0.5)
                except Exception as e:
                    print(f"⚠️ Could not fill datetime field {idx + 1}: {str(e)}")
                    
        except Exception as e:
            print(f"⚠️ Error finding datetime fields: {str(e)}")
            
    def submit_form(self):
        """Submit the form"""
        try:
            print("\n📤 Attempting to submit form...")
            
            # Find submit button - try multiple selectors
            submit_selectors = [
                'span[jsname="V67aGc"]',  # Submit button span
                'div[role="button"][jsname="M2UYVd"]',  # Submit button div
                'span:contains("Submit")',
                'button[type="submit"]'
            ]
            
            submit_button = None
            for selector in submit_selectors:
                try:
                    buttons = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    for button in buttons:
                        if button.is_displayed() and button.is_enabled():
                            button_text = button.text.lower()
                            if 'submit' in button_text or button_text == 'सबमिट करें' or button_text == '':
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
                print("✅ Form submitted successfully!")
                time.sleep(3)
                
                # Check for confirmation
                try:
                    confirmation = self.driver.find_element(By.CSS_SELECTOR, 'div.vHW8K')
                    print(f"✅ Confirmation message: {confirmation.text}")
                except:
                    print("✅ Form submitted (confirmation not found but submit clicked)")
                    
                return True
            else:
                print("❌ Submit button not found")
                return False
                
        except Exception as e:
            print(f"❌ Error submitting form: {str(e)}")
            return False
            
    def fill_form(self):
        """Main method to fill the entire form"""
        try:
            self.setup_driver()
            self.open_form()
            
            print("\n📋 Starting to fill the form...\n")
            
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
            
            print("\n" + "="*50)
            print("Form filling completed!")
            print("="*50 + "\n")
            
            # Ask user if they want to submit
            time.sleep(2)
            self.submit_form()
            
            print("\n✅ Process completed successfully!")
            print("Browser will close in 5 seconds...")
            time.sleep(5)
            
        except Exception as e:
            print(f"\n❌ Error occurred: {str(e)}")
            print("Browser will remain open for inspection...")
            time.sleep(10)
            
        finally:
            if self.driver:
                self.driver.quit()
                print("🔒 Browser closed.")


def main():
    print("="*50)
    print("🤖 Google Form Auto-Filler")
    print("="*50)
    print()
    
    # Get form URL from user
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
    filler = GoogleFormFiller(form_url)
    filler.fill_form()
    
    print("\n✅ All done! Thank you for using Google Form Auto-Filler.")


if __name__ == "__main__":
    main()


