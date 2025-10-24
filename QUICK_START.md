# ⚡ Quick Start Guide / शुरुआती गाइड

## English Version

### 3 Simple Steps:

**Step 1: Install** 
```bash
pip install -r requirements.txt
```
OR double-click `install.bat` (Windows)

**Step 2: Run**
```bash
python google_form_filler.py
```
OR double-click `run.bat` (Windows)

**Step 3: Enter URL**
```
📝 Enter Google Form URL: [paste your form URL here]
```

That's it! ✅

---

## Hindi/Hinglish Version

### 3 Aasan Steps:

**Step 1: Install karein**
```bash
pip install -r requirements.txt
```
Ya phir `install.bat` par double-click karein (Windows mein)

**Step 2: Run karein**
```bash
python google_form_filler.py
```
Ya phir `run.bat` par double-click karein (Windows mein)

**Step 3: Form ka URL daalein**
```
📝 Enter Google Form URL: [yahan apna form ka link paste karein]
```

Bas ho gaya! ✅

---

## What You Need / Kya Chahiye

✅ Python 3.7+ installed
✅ Google Chrome browser
✅ Internet connection
✅ Google Form ka link

---

## Files Overview / Files ka Overview

### Basic Files (Zaroori Files):
- `google_form_filler.py` - Main script (simple version)
- `requirements.txt` - Dependencies list
- `install.bat` - Windows installation helper
- `run.bat` - Windows run helper

### Advanced Files (Advanced Features):
- `google_form_filler_advanced.py` - Advanced version with logging
- `config.py` - Configuration file (customize settings)
- `test_installation.py` - Test if everything is working

### Documentation (Guide Files):
- `README.md` - Complete documentation
- `USAGE_GUIDE.md` - Detailed usage guide
- `EXAMPLES.md` - Examples and use cases
- `QUICK_START.md` - This file

---

## Troubleshooting / Agar Problem Ho

### Problem: "pip is not recognized"
**Solution:** 
```bash
python -m pip install -r requirements.txt
```

### Problem: Chrome browser nahi mil raha
**Solution:** Google Chrome install karein - https://www.google.com/chrome/

### Problem: Form submit nahi ho raha
**Solution:** 
- Check karein form mein required fields filled hain ya nahi
- Manually submit button pe click karein
- Error message console mein dekhein

### Problem: Script slow chal raha hai
**Solution:** 
Advanced version use karein with headless mode:
```python
# config.py mein change karein:
BROWSER_SETTINGS = {'headless': True}
```

---

## Quick Tips / Jaldi Tips

💡 **Tip 1:** Pahli baar test karein apne khud ke form par
💡 **Tip 2:** Data customize karna hai toh `config.py` edit karein
💡 **Tip 3:** Auto-submit off karna hai toh `config.py` mein `AUTO_SUBMIT = False`
💡 **Tip 4:** Errors ka screenshot chahiye toh `SCREENSHOT_ON_ERROR = True`
💡 **Tip 5:** Fast execution ke liye headless mode use karein

---

## Examples / Examples

### Example 1: Basic Form
```bash
python google_form_filler.py
# Enter: https://docs.google.com/forms/d/e/your-form/viewform
# Form automatically fill ho jayega aur submit bhi
```

### Example 2: Without Auto-Submit
```bash
# Pehle config.py edit karein:
# AUTO_SUBMIT = False

python google_form_filler_advanced.py
# Form fill hoga but submit nahi hoga
# Aap manually check kar sakte hain
```

### Example 3: Custom Data
```bash
# config.py edit karein:
# SAMPLE_NAMES = ["Aapka Naam", "Dusra Naam"]
# SAMPLE_EMAILS_DOMAIN = "yourcompany.com"

python google_form_filler_advanced.py
# Ab custom data use hoga
```

---

## Support / Help

### English:
- Read `README.md` for complete documentation
- Check `EXAMPLES.md` for more examples
- Run `python test_installation.py` to test setup

### Hindi/Hinglish:
- Poora documentation ke liye `README.md` padhein
- Zyada examples ke liye `EXAMPLES.md` dekhein
- Setup test karne ke liye `python test_installation.py` run karein

---

## Important Notes / Important Baatein

⚠️ **Dhyan dein:**
- Sirf testing purpose ke liye use karein
- Apne khud ke forms par pehle test karein
- Spam mat karein
- Google ki Terms of Service follow karein
- Responsible use karein

---

## Next Steps / Aage Kya Karein

1. ✅ Installation test karein: `python test_installation.py`
2. ✅ Basic script run karein: `python google_form_filler.py`
3. ✅ Apne form ka URL daalein
4. ✅ Dekhein kaise automatically fill hota hai
5. ✅ Config customize karein apni zaroorat ke hisaab se

---

## Version Comparison / Versions Ka Comparison

| Feature | Basic Version | Advanced Version |
|---------|--------------|------------------|
| Auto-fill all fields | ✅ | ✅ |
| Auto-submit | ✅ | ✅ (configurable) |
| Smart field detection | ✅ | ✅ |
| Configuration file | ❌ | ✅ |
| Detailed logging | ❌ | ✅ |
| Error screenshots | ❌ | ✅ |
| Execution summary | ❌ | ✅ |
| Headless mode | ❌ | ✅ |

**Recommendation / Suggestion:**
- Beginners → Use `google_form_filler.py`
- Advanced users → Use `google_form_filler_advanced.py`

---

## Contact / Sampark

Agar koi problem hai ya questions hain, toh:
1. Documentation files padhein
2. Error messages dhyan se dekhein
3. `test_installation.py` run karein

---

**Happy Coding! / Khush Rahein! 🚀**

**Made with ❤️ for automation**



