"""
Configuration file for Google Form Auto-Filler
Customize these settings according to your needs
"""

# Browser Settings
BROWSER_SETTINGS = {
    'headless': False,  # Set to True to run browser in background (no window)
    'maximize': True,   # Maximize browser window
    'wait_time': 10,    # Maximum wait time for elements (seconds)
}

# Delay Settings (in seconds)
DELAYS = {
    'between_fields': 0.5,      # Delay between filling each field
    'after_click': 0.3,         # Delay after clicking elements
    'page_load': 2,             # Delay after page load
    'before_submit': 2,         # Delay before clicking submit
    'after_submit': 3,          # Delay after submission
}

# Sample Data for Text Fields - Now generates random data
# Names will be generated randomly from first and last name lists
FIRST_NAMES = [
    "Raj", "Priya", "Amit", "Sneha", "Rahul", "Anita", "Vikram", "Kavita", "Arjun", "Pooja",
    "Suresh", "Meera", "Kiran", "Sunita", "Ravi", "Deepa", "Manoj", "Shilpa", "Rohit", "Neha",
    "Vishal", "Pooja", "Nikhil", "Ritu", "Sandeep", "Kavya", "Rohit", "Anjali", "Pankaj", "Suman",
    "Akshay", "Divya", "Rohit", "Priyanka", "Sachin", "Kavita", "Rahul", "Sneha", "Vikram", "Anita"
]

LAST_NAMES = [
    "Kumar", "Sharma", "Patel", "Singh", "Verma", "Desai", "Malhotra", "Reddy", "Gupta", "Agarwal",
    "Jain", "Bansal", "Chopra", "Mehta", "Shah", "Pandey", "Tiwari", "Mishra", "Yadav", "Joshi",
    "Nair", "Iyer", "Menon", "Krishnan", "Raman", "Srinivasan", "Venkatesh", "Raghavan", "Subramanian", "Reddy"
]

# Email domains for random selection
EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "example.com", "test.com", "demo.com"]
EMAIL_PREFIX = "user"  # Prefix for generated emails

# Phone Number Settings
PHONE_MIN = 6000000000  # Minimum phone number
PHONE_MAX = 9999999999  # Maximum phone number
PHONE_PREFIX = ""       # Add country code like "+91" if needed

# Age Range
AGE_MIN = 18
AGE_MAX = 60

# Date Settings
DATE_RANGE_YEARS = 5  # How many years back to generate dates
DATE_START_OFFSET_DAYS = 0  # Days to add to start date (0 = today)

# Time Settings
TIME_START_HOUR = 9  # Start hour for business hours
TIME_END_HOUR = 18   # End hour for business hours
TIME_MINUTES = [0, 15, 30, 45]  # Available minute options

# DateTime Settings
DATETIME_RANGE_YEARS = 2  # How many years back for datetime fields

# Random Text Generation - No more fixed lists!
# The script will now generate random text instead of using fixed lists

# Words for random text generation
RANDOM_WORDS = [
    "This", "is", "a", "detailed", "response", "to", "the", "question", "providing", "comprehensive", 
    "information", "that", "covers", "all", "aspects", "of", "the", "query", "Thank", "you", 
    "for", "this", "opportunity", "I", "would", "like", "to", "express", "my", "thoughts", 
    "on", "this", "matter", "in", "detail", "This", "is", "an", "automated", "response", 
    "for", "testing", "purposes", "The", "system", "is", "working", "as", "expected", "and", 
    "all", "functionality", "has", "been", "verified", "successfully", "I", "appreciate", 
    "the", "opportunity", "to", "provide", "feedback", "and", "share", "my", "experience",
    "with", "this", "platform", "It", "has", "been", "very", "helpful", "and", "informative",
    "I", "look", "forward", "to", "future", "interactions", "and", "opportunities", "to", "contribute"
]

# Short text responses (will be generated randomly)
SHORT_TEXT_PREFIXES = ["Response", "Answer", "Reply", "Comment", "Feedback", "Input", "Data", "Info", "Note", "Update"]
SHORT_TEXT_SUFFIXES = ["123", "456", "789", "ABC", "XYZ", "Test", "Demo", "Sample", "Random", "Auto"]

# Checkbox Selection
CHECKBOX_MIN_SELECT = 1  # Minimum number of checkboxes to select
CHECKBOX_MAX_SELECT = 3  # Maximum number of checkboxes to select

# Dropdown Settings
SKIP_FIRST_OPTION = True  # Skip first dropdown option (usually "Choose")

# Linear Scale Settings
LINEAR_SCALE_RANDOM = True  # True = random selection, False = always select middle

# Form Submission
AUTO_SUBMIT = True  # Automatically submit form after filling

# Console Output
VERBOSE = True  # Show detailed logs
SHOW_EMOJIS = True  # Show emojis in console output

# Error Handling
CONTINUE_ON_ERROR = True  # Continue filling form even if some fields fail
SCREENSHOT_ON_ERROR = False  # Take screenshot when error occurs


