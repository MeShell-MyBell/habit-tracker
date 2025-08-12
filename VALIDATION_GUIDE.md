# Quick Validation Testing Guide

## HTML Validation
1. **Visit**: https://validator.w3.org/
2. **Method**: "Validate by URI"
3. **Test URLs**:
   - `http://127.0.0.1:8000/` (Dashboard)
   - `http://127.0.0.1:8000/login/` (Login)
   - `http://127.0.0.1:8000/signup/` (Registration)
4. **Screenshot results** and save as `screenshots/html-validation.png`

## CSS Validation  
1. **Visit**: https://jigsaw.w3.org/css-validator/
2. **Method**: "By URI"
3. **Test**: `http://127.0.0.1:8000/static/css/style.css`
4. **Screenshot results** and save as `screenshots/css-validation.png`

## Quick Accessibility Check
1. **Browser**: Right-click → "Inspect" → "Lighthouse" tab
2. **Run audit**: Accessibility only
3. **Screenshot score** and save as `screenshots/accessibility-audit.png`

## Expected Results
- **HTML**: Should pass with minimal warnings (Bootstrap CSS may generate some)
- **CSS**: Should pass cleanly 
- **Accessibility**: Aim for 90+ score

These validation tests demonstrate code quality and accessibility compliance for your assessment.