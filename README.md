# 🤖 Google Form Auto-Filler

Automatically fill and submit Google Forms using Python and Selenium.

## 📋 Features

- ✅ Automatically detects and fills all form field types:
  - Text inputs (short answer)
  - Text areas (long answer/paragraph)
  - Radio buttons (multiple choice)
  - Checkboxes
  - Dropdowns
  - Linear scales
  - Date fields
  - Time fields
  - DateTime fields
  
- 🧠 Smart field detection (email, phone, name, age, etc.)
- 🎯 Random but realistic data generation
- 📤 Automatic form submission
- 🔒 Human-like behavior simulation
- ⚡ Fast and efficient

## 🚀 Installation

1. **Install Python** (3.7 or higher)

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Chrome Browser** must be installed (ChromeDriver will be installed automatically)

## 💻 Usage

1. **Run the script:**
```bash
python google_form_filler.py
```

2. **Enter the Google Form URL** when prompted
   - Supports: `docs.google.com/forms/...` and `forms.gle/...`
   - The script will validate the URL format

3. **Sit back and watch** as the form gets filled automatically!

## 📝 Example

```
🤖 Google Form Auto-Filler
==================================================

📝 Enter Google Form URL: https://docs.google.com/forms/d/e/your-form-id/viewform

🚀 Starting form filling process...

🚀 Setting up browser...
📝 Opening form: https://docs.google.com/forms/d/e/your-form-id/viewform

📋 Starting to fill the form...

✅ Filled text field 1: Raj Kumar
✅ Filled text field 2: testuser123@example.com
✅ Selected radio option in group 1
✅ Selected 2 checkbox(es) in group 1
✅ Filled textarea 1

📤 Attempting to submit form...
✅ Form submitted successfully!

✅ Process completed successfully!
```

## ⚙️ How It Works

1. **Setup**: Initializes Chrome browser with anti-detection settings
2. **Open Form**: Navigates to the provided Google Form URL
3. **Field Detection**: Identifies all form fields using CSS selectors
4. **Smart Filling**: 
   - Email fields get email addresses
   - Phone fields get phone numbers
   - Name fields get realistic names
   - Other fields get random appropriate data
5. **Submit**: Clicks the submit button and verifies submission

## 🎯 Supported Field Types

| Field Type | Support | Notes |
|------------|---------|-------|
| Short Answer | ✅ | Smart detection for email, phone, name, age |
| Paragraph | ✅ | Long text responses |
| Multiple Choice | ✅ | Random selection |
| Checkboxes | ✅ | Selects 1-3 random options |
| Dropdown | ✅ | Random selection |
| Linear Scale | ✅ | Random rating selection |
| Date Fields | ✅ | Random dates within configurable range |
| Time Fields | ✅ | Random times in business hours |
| DateTime Fields | ✅ | Random date and time combinations |
| File Upload | ❌ | Not supported |

## ⚠️ Important Notes

- This tool is for **testing and educational purposes only**
- Respect Google's Terms of Service
- Don't use for spam or malicious purposes
- Some forms may have CAPTCHA or other protections
- The script will automatically install ChromeDriver

## 🐛 Troubleshooting

**Issue**: ChromeDriver not found
- **Solution**: The script uses webdriver-manager which auto-downloads ChromeDriver

**Issue**: Form not submitting
- **Solution**: Some forms may have required fields or validation. Check console output.

**Issue**: Browser closes immediately
- **Solution**: Check error messages in console. Browser stays open on errors for debugging.

## 📄 License

This project is for educational purposes only. Use responsibly!

## 🤝 Contributing

Feel free to improve this script and add more features!

## 📧 Contact

For issues or questions, please create an issue in the repository.


