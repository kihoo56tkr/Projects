# Python Email Automation Script
This script automates the process of sending an email reminder about updating a link for data as of the previous quarter. It does this by performing the following actions:
1. Determine Date Information:
- The script calculates the first day of the current month, the last day of the previous month, and the deadline for data submission.

2. Interact with Outlook:
- It retrieves the most recent email from the Outlook inbox to check if the email reminder for the quarter has been sent already.

3. Read Data from Excel:
- It loads email addresses from a specific Excel file (.xlsx) and prepares the recipients list.

4. Send Email:
- If the reminder email has not been sent already, it composes a custom HTML email and sends it via Outlook.

Note: Some of the details are intentionally omitted or generalized for privacy and security reasons.
