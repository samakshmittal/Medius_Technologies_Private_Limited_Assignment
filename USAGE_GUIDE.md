# 📖 Usage Guide - Google Form Auto-Filler

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies
**Windows:**
```bash
# Double-click install.bat
OR
# Run in terminal:
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
pip install -r requirements.txt
```

### Step 2: Get Your Form URL
1. Open any Google Form
2. Copy the URL from browser address bar
3. Example: `https://docs.google.com/forms/d/e/1FAIpQLSc.../viewform`

### Step 3: Run the Script
**Windows:**
```bash
# Double-click run.bat
OR
# Run in terminal:
python google_form_filler.py
```

**Linux/Mac:**
```bash
python google_form_filler.py
```

---

## 🎯 What Happens Step-by-Step

### 1. Browser Opens
```
🚀 Setting up browser...
```
- Chrome browser launches automatically
- No need to download ChromeDriver manually
- Browser configured to avoid detection

### 2. Form Opens
```
📝 Opening form: [your-url]
```
- Navigates to your Google Form
- Waits for page to load completely

### 3. Fields Get Filled
```
📋 Starting to fill the form...

✅ Filled text field 1: Raj Kumar
✅ Filled text field 2: testuser456@example.com
✅ Selected radio option in group 1
✅ Selected 2 checkbox(es) in group 1
```

The script automatically detects and fills:
- **Name fields** → Random Indian names (Raj Kumar, Priya Sharma, etc.)
- **Email fields** → Random email (testuser123@example.com)
- **Phone fields** → Random 10-digit numbers (9876543210)
- **Age fields** → Random age between 18-60
- **Radio buttons** → Selects one random option
- **Checkboxes** → Selects 1-3 random options
- **Dropdowns** → Selects random option (skips "Choose" option)
- **Text areas** → Detailed paragraph responses
- **Linear scales** → Random rating

### 4. Form Submission
```
📤 Attempting to submit form...
✅ Form submitted successfully!
✅ Confirmation message: Your response has been recorded
```

### 5. Completion
```
✅ Process completed successfully!
Browser will close in 5 seconds...
🔒 Browser closed.
```

---

## 🎨 Example Output

```
==================================================
🤖 Google Form Auto-Filler
==================================================

📝 Enter Google Form URL: https://docs.google.com/forms/d/e/1FAIpQLSc.../viewform

🚀 Starting form filling process...

🚀 Setting up browser...
📝 Opening form: https://docs.google.com/forms/d/e/1FAIpQLSc.../viewform

📋 Starting to fill the form...

✅ Filled text field 1: Amit Patel
✅ Filled text field 2: testuser789@example.com
✅ Filled text field 3: 9123456789
✅ Filled textarea 1
✅ Selected radio option in group 1
✅ Selected radio option in group 2
✅ Selected 2 checkbox(es) in group 1
✅ Selected dropdown option in dropdown 1
✅ Selected linear scale option 1

==================================================
Form filling completed!
==================================================

📤 Attempting to submit form...
✅ Form submitted successfully!
✅ Confirmation message: Your response has been recorded.

✅ Process completed successfully!
Browser will close in 5 seconds...
🔒 Browser closed.

✅ All done! Thank you for using Google Form Auto-Filler.
```

---

## 🔧 Customization

### Change Fill Data

Edit `google_form_filler.py` and modify these sections:

**Text Inputs:**
```python
sample_texts = [
    "Your Custom Text",
    "Another Option",
    # Add more...
]
```

**Names:**
```python
text = random.choice(["Your Name", "Another Name"])
```

**Email Pattern:**
```python
text = f"yourprefix{random.randint(1, 1000)}@yourdomain.com"
```

**Phone Pattern:**
```python
text = f"+91{random.randint(6000000000, 9999999999)}"
```

---

## ⚠️ Common Issues & Solutions

### Issue 1: "pip is not recognized"
**Solution:** Install Python with "Add to PATH" option
OR
```bash
python -m pip install -r requirements.txt
```

### Issue 2: "Chrome not found"
**Solution:** Install Google Chrome browser

### Issue 3: Form not filling completely
**Reason:** Some fields may have custom implementations
**Solution:** Script will skip problematic fields and continue with others

### Issue 4: Submit button not found
**Reason:** Form may use custom submit button
**Solution:** The script tries multiple selectors. Manual submission may be needed.

### Issue 5: "Access Denied" or CAPTCHA
**Reason:** Form has security measures
**Solution:** These forms cannot be automated (by design)

---

## 🎓 Understanding the Code

### Main Components:

1. **GoogleFormFiller Class**
   - `setup_driver()` → Initializes Chrome
   - `open_form()` → Opens the form URL
   - `fill_text_fields()` → Handles text inputs
   - `fill_textarea_fields()` → Handles long answers
   - `select_radio_buttons()` → Handles multiple choice
   - `select_checkboxes()` → Handles checkboxes
   - `select_dropdowns()` → Handles dropdown menus
   - `fill_linear_scale()` → Handles rating scales
   - `submit_form()` → Submits the form

2. **Smart Detection**
   ```python
   if 'email' in question:
       text = "testuser@example.com"
   elif 'phone' in question:
       text = "9876543210"
   ```

3. **Human-like Delays**
   ```python
   time.sleep(0.5)  # Wait between actions
   ```

---

## 🚨 Important Warnings

1. **Legal Use Only**: Use this tool responsibly
2. **Testing Purpose**: Designed for testing your own forms
3. **Rate Limiting**: Don't spam forms repeatedly
4. **Privacy**: Be careful with sensitive forms
5. **Terms of Service**: Respect Google's ToS

---

## 📞 Need Help?

1. Check error messages in console
2. Read the README.md file
3. Verify your Python version: `python --version` (should be 3.7+)
4. Verify Chrome is installed: Open Chrome browser manually
5. Check internet connection

---

## 🎉 Tips for Best Results

✅ **DO:**
- Use on your own test forms first
- Check form preview after filling
- Use for legitimate testing purposes
- Keep script updated

❌ **DON'T:**
- Spam public forms
- Use for malicious purposes
- Bypass CAPTCHAs
- Violate Terms of Service

---

**Happy Automated Form Filling! 🚀**



