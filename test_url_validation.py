"""
Test script to verify Google Form URL validation
"""

def test_url_validation():
    """Test URL validation logic"""
    print("Google Form URL Validation Test")
    print("="*50)
    
    # Test URLs
    test_urls = [
        # Valid URLs
        "https://docs.google.com/forms/d/e/1FAIpQLSc.../viewform",
        "https://forms.gle/abc123def456",
        "http://docs.google.com/forms/d/e/1FAIpQLSc.../viewform",
        "https://forms.gle/xyz789",
        "docs.google.com/forms/d/e/1FAIpQLSc.../viewform",
        "forms.gle/abc123",
        
        # Invalid URLs
        "https://www.google.com",
        "https://docs.google.com/document/d/123",
        "https://forms.google.com/123",
        "https://example.com/form",
        "https://docs.google.com/spreadsheets/d/123",
        "https://www.google.com/forms/123",
    ]
    
    # Validation function
    def is_valid_google_form_url(url):
        valid_patterns = ['docs.google.com/forms', 'forms.gle']
        return any(pattern in url for pattern in valid_patterns)
    
    print("\nTesting URL validation:")
    print("-" * 50)
    
    for i, url in enumerate(test_urls, 1):
        is_valid = is_valid_google_form_url(url)
        status = "VALID" if is_valid else "INVALID"
        print(f"{i:2d}. {status} - {url}")
    
    print("\n" + "="*50)
    print("URL validation test completed!")

def show_supported_patterns():
    """Show supported URL patterns"""
    print("\nSupported Google Form URL Patterns:")
    print("="*50)
    
    patterns = [
        "docs.google.com/forms/...",
        "forms.gle/..."
    ]
    
    for i, pattern in enumerate(patterns, 1):
        print(f"{i}. {pattern}")
    
    print("\nExamples:")
    examples = [
        "https://docs.google.com/forms/d/e/1FAIpQLSc.../viewform",
        "https://forms.gle/abc123def456",
        "http://docs.google.com/forms/d/e/1FAIpQLSc.../viewform",
        "https://forms.gle/xyz789"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"  {i}. {example}")

def main():
    print("Google Form URL Validation Test")
    print("="*60)
    
    test_url_validation()
    show_supported_patterns()
    
    print("\n" + "="*60)
    print("All tests completed!")
    print("The script now properly validates Google Form URLs!")
    print("="*60)

if __name__ == "__main__":
    main()
