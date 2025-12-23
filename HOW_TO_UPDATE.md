# How to Update Pricing & Delivery Info

## ⚠️ IMPORTANT: Edit ONLY ONE Place!

All pricing and delivery information is in **ONE DOCUMENT** in the knowledge base.

---

## Step-by-Step Instructions

### 1. Open the File
- Go to: `streamlit-deploy/knowledge_base.json`
- Open in any text editor (VS Code, Notepad++, etc.)

### 2. Find the Section (Line 12-16)
Look for this section near the top:

```json
"description": "IMPORTANT: This is the official and most up-to-date product information..."
```

### 3. Edit What You Need

#### To Change Pricing:
Find these lines and change the numbers:
```
1. DOSTBIN BASIC - ₹19,999 (inclusive of GST)
2. DOSTBIN POPULAR - ₹24,999 (inclusive of GST)
3. DOSTBIN PREMIUM - ₹34,999 (inclusive of GST)
```

#### To Change Delivery Time:
Find this line and change the days:
```
- Delivery Time: 20-25 business days across PAN India
```

#### To Change Capacity:
Find this line and change the amount:
```
- All variants (Basic, Popular, Premium): Up to 5 Kg/day
```

### 4. Save the File
- Press Ctrl+S to save

### 5. Validate JSON (IMPORTANT!)
- Go to: https://jsonlint.com/
- Copy-paste your ENTIRE file
- Click "Validate JSON"
- If errors, fix them before uploading

### 6. Upload to GitHub
- Commit the file
- Push to GitHub
- Wait 5-10 minutes for Streamlit to redeploy

---

## ✅ That's It!

You edited **ONE place** and the entire chatbot is updated!

---

## ⚠️ Common Mistakes

1. **Don't use Microsoft Word** - It will corrupt the file
2. **Don't remove quotes or commas** - JSON is strict about syntax
3. **Always validate** before uploading
4. **Use straight quotes** (" ") not smart quotes (" ")

---

## Current Values (as of cleanup)

- **DOSTBIN BASIC**: ₹19,999
- **DOSTBIN POPULAR**: ₹24,999
- **DOSTBIN PREMIUM**: ₹34,999
- **Delivery**: 20-25 business days
- **Capacity**: Up to 5 Kg/day

