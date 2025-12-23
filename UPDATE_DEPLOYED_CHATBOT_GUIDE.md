

                    HOW TO UPDATE THE DEPLOYED CHATBOT
              Step-by-Step Guide for Making Changes After Deployment


This guide is for updating the chatbot that is already live on Streamlit Cloud.

Time Required: 5-10 minutes per update

________________________________________________________________________________


IMPORTANT: How Updates Work

When the chatbot is deployed on Streamlit Cloud:

   1. The code is stored on GitHub
   2. Streamlit Cloud automatically pulls code from GitHub
   3. When you update files on GitHub, Streamlit automatically rebuilds the chatbot
   4. Changes go live within 2-5 minutes

You ONLY need to update knowledge_base.json on GitHub - Streamlit handles the rest!

________________________________________________________________________________


UPDATE USING GITHUB WEBSITE (NO CODING REQUIRED)


STEP 1: Log in to GitHub

1. Go to: https://github.com
2. Sign in with your credentials
3. Open the "dostbin-chatbot" repository


STEP 2: Edit the Knowledge Base File

1. Click on "knowledge_base.json"
2. Click the pencil icon (✏️) "Edit this file"
3. Make your changes (use Ctrl+F to search)
4. Don't delete commas, quotes, or brackets


STEP 3: Save Your Changes

1. Scroll to bottom
2. Type commit message: "Updated Premium price to ₹32,999"
3. Click "Commit changes"


STEP 4: Wait for Auto-Deployment (2-5 minutes)

Streamlit Cloud automatically detects the change and rebuilds the chatbot.


STEP 5: Test Your Changes

1. Go to your chatbot URL
2. Ask: "What is the price of Premium Dostbin?"
3. Verify the new information appears

________________________________________________________________________________


COMMON UPDATE SCENARIOS


SCENARIO A: Changing Product Pricing

1. Log in to GitHub
2. Open dostbin-chatbot repository
3. Click on knowledge_base.json
4. Click edit (pencil icon)
5. Search for the old price (Ctrl+F)
6. Replace with new price
7. Scroll down and commit with message: "Updated pricing"
8. Wait 2-5 minutes for Streamlit to rebuild
9. Test the chatbot


SCENARIO B: Adding a New Product

1. Log in to GitHub
2. Open knowledge_base.json for editing
3. Find the "products" section
4. Copy an existing product entry
5. Paste it after the last product (don't forget comma after previous entry)
6. Update the details (name, price, features, etc.)
7. Commit with message: "Added new product: [Product Name]"
8. Wait for rebuild
9. Test by asking about the new product


SCENARIO C: Adding Offers/Discounts

1. Log in to GitHub
2. Open knowledge_base.json for editing
3. Find the "plans_pricing" section
4. Add new offer entry with title, description, discount, validity
5. Commit with message: "Added Diwali offer"
6. Wait for rebuild
7. Test by asking: "Do you have any offers?"


SCENARIO D: Updating Contact Information

1. Log in to GitHub
2. Open knowledge_base.json for editing
3. Search for old email/phone (Ctrl+F)
4. Replace with new contact details
5. Commit with message: "Updated contact information"
6. Wait for rebuild
7. Test by asking: "How do I contact support?"

________________________________________________________________________________


TROUBLESHOOTING


Problem: I can't find the edit button (pencil icon)
Solution:
   • Make sure you're logged in to GitHub
   • Make sure you're viewing YOUR repository (not someone else's)
   • Make sure you clicked on the file name to open it


Problem: Changes not appearing in chatbot after 10 minutes
Solution:
   • Go to https://share.streamlit.io
   • Log in with GitHub
   • Find your app in the dashboard
   • Click the three dots (...) menu
   • Click "Reboot app"
   • Wait 2 minutes and check again


Problem: Chatbot shows error after my update
Solution:
   • You likely broke the JSON format (missing comma, quote, or bracket)
   • Go back to GitHub
   • Click on knowledge_base.json
   • Click "History" button
   • Click on the previous version (before your change)
   • Click "..." menu → "View file"
   • Copy the old content
   • Edit the current file and paste the old content back
   • Commit with message: "Reverted to previous version"
   • Make your changes more carefully this time


Problem: I don't remember my GitHub password
Solution:
   • Go to https://github.com
   • Click "Sign in"
   • Click "Forgot password?"
   • Enter your email
   • Follow the reset instructions


Problem: Streamlit app is not rebuilding automatically
Solution:
   • Go to https://share.streamlit.io
   • Log in with GitHub
   • Find your app
   • Click "Reboot app" manually
   • This forces a rebuild

________________________________________________________________________________


IMPORTANT TIPS

DO's:
   ✓ Always test changes in the chatbot after updating
   ✓ Write clear commit messages so you know what you changed
   ✓ Make one change at a time (easier to troubleshoot if something breaks)
   ✓ Keep your GitHub password safe and secure

DON'Ts:
   ✗ Don't edit multiple files at once if you're not sure what you're doing
   ✗ Don't delete commas, quotes, or brackets in JSON files
   ✗ Don't share your GitHub password with unauthorized people
   ✗ Don't panic if something breaks - you can always revert to previous version

________________________________________________________________________________


QUICK REFERENCE CHECKLIST

For every update:

   [ ] Step 1: Log in to GitHub (https://github.com)
   [ ] Step 2: Open dostbin-chatbot repository
   [ ] Step 3: Click on knowledge_base.json
   [ ] Step 4: Click edit button (pencil icon)
   [ ] Step 5: Make your changes
   [ ] Step 6: Scroll down and commit changes
   [ ] Step 7: Wait 2-5 minutes
   [ ] Step 8: Test the chatbot at your Streamlit URL
   [ ] Step 9: Verify changes are working

________________________________________________________________________________


VIEWING CHANGE HISTORY

To see all previous changes:

1. Go to your GitHub repository
2. Click on knowledge_base.json
3. Click "History" button (top right)
4. You'll see all changes with dates and descriptions
5. Click on any version to see what was changed
6. You can restore any previous version if needed

________________________________________________________________________________


NEED HELP?

If you're stuck or something goes wrong:

   1. Check the Troubleshooting section above
   2. Contact Aman (the developer) for assistance
   3. Don't make random changes - you might break the chatbot
   4. You can always revert to a previous working version

________________________________________________________________________________

Last Updated: December 2025
Created by: Aman (Intern, Dostbin Solutions)

