Hello!

This is a python tool to stop you wanting to off yourself as much as I did using the 
god awful facebook API.

This tool simply takes a few parameters in the 'parameters.txt' file and will post on
the facebook page you desire! 
Alternatively, use the command set to make posts from a seperate script, or from the
console!

===== REQUIREMENTS =====
- Python3.7 or higher
- Python requests library
- Python re library

===== HOW TO - Facebook App & Page Setup =====

1) Go to https://developers.facebook.com and create an account/sign in
2) In the top-right dropdown go to 'My Apps > Add New App'
3) Give it a display name and complete the reCAPTCHA
4) On the left-hand menus, go to 'Settings > Advanced'
5) Scroll down until you see 'App Page'
6) Click on the 'Create New Page' button
7) Select the 'Business or brand' option in the new window
8) Give your page a name and a category ('Just for fun' if you can't think of anything else)
9) Press 'Continue' and either skip or add a profile and cover picture
10) Go to https://developers.facebook.com/tools/explorer and log in
11) Select your App from the top right dropdown menu
12) Select "Get User Access Token" from dropdown (right of access token field)
13) In the pop-up box, make sure 'manage_pages', 'pages_show_list' and 'publish_pages' are ticked
14) Click 'Get Access Token'
15) In the pop-up window, select the page you created for the bot
16) Leave all of the permissions active (there should be 3 - the ones in step 13) and press 'Done'
14) Copy the user access token (the big string that appeared in the 'Access Token' box)
15) Go to https://developers.facebook.com/tools/debug/accesstoken/
16) Paste the copied token in the input field and press "Debug"
17) Press "Extend Access Token" (bottom on the page) and click the debug button the appears next to the new token
18) Copy the new access token from the new window
19) Go back to the Graph API Explorer
20) Paste copied token into the "Access Token" field
21) Make sure 'GET' is selected from the command dropdown (far left of input field)
22) Go to your facebook page and copy the page ID from the URL (the big number after the page name - https://www.facebook.com/Test_page-610753842700559)
23) Input: '{PAGE_ID}?fields=access_token' into the input field, where {PAGE_ID} is the id of the facebook page
24) Find the permanent page access token in the response (node "access_token")
25) Go back to the Access Token Debugger and paste the permanent token and press "Debug". "Expires" should be "Never"
26) Go back to https://developers.facebook.com and select your app in 'My Apps'
27) On the right hand side, go to 'Settings > Basic'
28) Under 'Privacy Policy URL', input a URL to a text document containing your Privacy Policy (Google Drive Docs works for this)
29) In the top right of the app settings should be a toggle that says 'OFF' next to 'Status: In Development'. Click on the toggle to publish your app.
30) You're all setup!

You now have everything you need to post to your facebook page!

===== 'parameters.txt' SETUP =====

- The text file should look as follows, with {} areas being replaced with the required
  field
------------------------
parameters.txt
------------------------
"access_token"='{Your permanent page access token}'
"page_id"='{Your page ID number}'
"message"='{The message you wish to post}'

===== COMMANDS =====

Whether running in the python shell or through the console, these commands will allow you
to post content with ease.

Post.fromFile()
- Makes a post utilising the values input into parameters.txt

Post.custom(access_token, page_id, message)
- Fully custom way to post things to your page. Takes the three parameters described.

Post.withMessage(message)
- Uses the access_token and page_id from parameters.txt, whilst using a message input through a custom parameter

Utility.createFile()
- Creates a 'parameters.txt' file in the current directory of fbpb.py
