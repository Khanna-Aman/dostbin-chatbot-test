

                    KNOWLEDGE BASE UPDATE GUIDE
                How to Update Chatbot Information (Step-by-Step)


This guide explains how to update the chatbot when you need to:
   • Add new Dostbin products
   • Change pricing
   • Add offers/discounts
   • Update contact information
   • Add new FAQs

________________________________________________________________________________


QUICK OVERVIEW

What you need to update: knowledge_base.json file
Where it's located: Root folder of the project
Tools needed: Any text editor (Notepad, VS Code, Notepad++)
Time required: 5-15 minutes per update

________________________________________________________________________________


STEP-BY-STEP INSTRUCTIONS


SCENARIO 1: Changing Product Pricing

Example: Premium model price changed from ₹29,999 to ₹32,999

Steps:

1. Open the knowledge_base.json file
   • Right-click knowledge_base.json → Open with → Notepad (or any text editor)

2. Press Ctrl+F to search
   • Search for: 29999 or Premium or the old price

3. Update the price
   • Find the pricing section
   • Change the old price to new price
   • Example: "price": "₹32,999"

4. Save the file
   • Press Ctrl+S
   • Close the editor

5. Restart the chatbot
   • Stop the running chatbot (close the browser tab and terminal)
   • Run again: python -m streamlit run streamlit-deploy/app.py

6. Test the update
   • Ask: "What is the price of Premium Dostbin?"
   • Verify the new price appears

________________________________________________________________________________


SCENARIO 2: Adding a New Product

Example: Adding "Dostbin XL" model

Steps:

1. Open knowledge_base.json

2. Find the "products" section
   • Search for: "products":
   • You'll see existing products like Basic, Popular, Premium

3. Copy an existing product entry
   • Copy the entire block of one product (from { to })

4. Paste and modify
   • Paste it after the last product
   • Add a comma , after the previous product
   • Update the details with new product information

5. Save and restart (same as Scenario 1)

6. Test
   • Ask: "Tell me about Dostbin XL"

________________________________________________________________________________


SCENARIO 3: Adding Offers/Discounts

Example: "Diwali Offer - 15% off on all models"

Steps:

1. Open knowledge_base.json

2. Find the "plans_pricing" section
   • Search for: "plans_pricing":

3. Add offer information
   • Add a new entry with offer details:
     - Title: "Diwali Offer 2025"
     - Description: "Get 15% off on all Dostbin models. Valid till December 31, 2025."
     - Discount: "15%"
     - Applicable products: "All models - Basic, Popular, Premium"
     - Validity: "Valid till 31st December 2025"

4. Save and restart

5. Test
   • Ask: "Do you have any offers?"
   • Ask: "What discounts are available?"

________________________________________________________________________________


SCENARIO 4: Updating Contact Information

Example: New phone number or email

Steps:

1. Open knowledge_base.json

2. Search for "support_articles" or "company_socials"
   • Press Ctrl+F → Search: info@dostbin.com (old email)

3. Update contact details
   • Replace old email/phone with new one
   • Example: "email": "support@dostbin.com"

4. Save and restart

5. Test
   • Ask: "How do I contact support?"

________________________________________________________________________________


SCENARIO 5: Adding New FAQs

Example: "Can Dostbin handle meat waste?"

Steps:

1. Open knowledge_base.json

2. Find the "faqs" section
   • Search for: "faqs":

3. Add new FAQ entry
   • Question: "Can Dostbin handle meat waste?"
   • Answer: "No, Dostbin is designed for vegetable and fruit waste only. Meat,
     bones, and dairy products should not be added as they attract pests and
     create odor."
   • Category: "Usage"

4. Save and restart

5. Test
   • Ask: "Can I put meat in Dostbin?"

________________________________________________________________________________


IMPORTANT TIPS

DO's:
   ✓ Always make a backup copy of knowledge_base.json before editing
   ✓ Use a proper text editor (Notepad++, VS Code) - NOT Microsoft Word
   ✓ Maintain the JSON format (commas, quotes, brackets)
   ✓ Test the chatbot after every update
   ✓ Keep information accurate and up-to-date

DON'Ts:
   ✗ Don't use Microsoft Word or Excel to edit JSON files
   ✗ Don't forget commas between entries
   ✗ Don't remove quotes around text
   ✗ Don't break the JSON structure
   ✗ Don't forget to restart the chatbot after changes

________________________________________________________________________________


TROUBLESHOOTING

Problem: Chatbot shows old information
Solution:
   • Make sure you saved the file (Ctrl+S)
   • Restart the chatbot completely
   • Clear browser cache (Ctrl+Shift+R)

Problem: Chatbot stops working after update
Solution:
   • You likely broke the JSON format
   • Restore the backup copy
   • Use an online JSON validator: https://jsonlint.com/
   • Paste your JSON and check for errors

Problem: New information not appearing
Solution:
   • Check if you added it in the correct section
   • Verify JSON syntax (commas, quotes, brackets)
   • Make sure the chatbot restarted properly

________________________________________________________________________________


QUICK REFERENCE

File to edit: knowledge_base.json

Sections in the file:
   • company_socials - Social media links
   • products - Product information
   • plans_pricing - Pricing and offers
   • support_articles - Support information
   • faqs - Frequently asked questions
   • how_it_works - Process explanations
   • accessories - Accessories and add-ons

After every change:
   1. Save file (Ctrl+S)
   2. Stop chatbot
   3. Restart: python -m streamlit run streamlit-deploy/app.py
   4. Test the changes

________________________________________________________________________________


NEED HELP?

If you're not comfortable editing JSON files, you can:
   1. Contact Aman (the developer) for assistance
   2. Use an online JSON editor for easier editing
   3. Keep a list of changes and update in batches

________________________________________________________________________________

Last Updated: December 2025
Created by: Aman (Intern, Dostbin Solutions)

