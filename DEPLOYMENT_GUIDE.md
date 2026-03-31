# 🚀 DEPLOYMENT GUIDE: Student Feedback Generator Agent
## GitHub + Streamlit Cloud Deployment for Professor BenMessaoud

This guide will help you deploy your Feedback Generator Agent so your TA and students can use it from anywhere!

---

## 📋 **WHAT YOU'LL ACCOMPLISH**

By the end of this guide, you'll have:
- ✅ Your app hosted on GitHub
- ✅ Your app deployed on Streamlit Cloud (FREE!)
- ✅ A public URL your TA and students can access
- ✅ Secure API key configuration
- ✅ Professional deployment ready for classroom use

**Total Time: 30-40 minutes**

---

## 🎯 **PREREQUISITES**

Before starting, make sure you have:

- [ ] **GitHub Account** - Free at [github.com](https://github.com)
- [ ] **Anthropic API Key** - Get from [console.anthropic.com](https://console.anthropic.com/settings/keys)
- [ ] **All Project Files** - The files I'll provide
- [ ] **30-40 minutes** of uninterrupted time
- [ ] **Basic familiarity** with file management

**Don't worry if you're new to GitHub/Streamlit - I'll explain everything!**

---

## 📦 **PART 1: PREPARE YOUR FILES** (5 minutes)

### **Step 1.1: Organize Your Project**

Create a new folder on your computer called `feedback-agent-deploy`:

```
feedback-agent-deploy/
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml.example
├── .gitignore
├── app.py
├── templates.py
├── parser.py
├── doc_generator.py
├── requirements.txt
├── Dockerfile
├── run.sh
├── run.bat
└── README.md
```

### **Step 1.2: Download All Files**

Make sure you have all the files I'm providing:

**Core Application Files:**
- ✅ `app.py` - Main application
- ✅ `templates.py` - Feedback templates
- ✅ `parser.py` - Student submission parser
- ✅ `doc_generator.py` - Word document generator

**Configuration Files:**
- ✅ `requirements.txt` - Python dependencies
- ✅ `.gitignore` - Protects secrets
- ✅ `.streamlit/config.toml` - App theming
- ✅ `.streamlit/secrets.toml.example` - API key template

**Documentation:**
- ✅ `README.md` - Full documentation
- ✅ `Dockerfile` - Container configuration (optional)

**Helper Scripts:**
- ✅ `run.sh` - Quick start (Mac/Linux)
- ✅ `run.bat` - Quick start (Windows)

### **Step 1.3: Verify File Structure**

Double-check that:
- All files are in the `feedback-agent-deploy` folder
- The `.streamlit` subfolder exists with both files
- No file is password-protected or corrupted

**✅ Files ready? Let's move to GitHub!**

---

## 🐙 **PART 2: UPLOAD TO GITHUB** (10-15 minutes)

### **Step 2.1: Create GitHub Account (if needed)**

1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Enter your email (use your university email)
4. Create a strong password
5. Choose a username (e.g., `profbenmessaoud` or `iu-feedback-tools`)
6. Verify your email
7. **Done!** ✅

**Already have GitHub account?** Skip to Step 2.2!

---

### **Step 2.2: Create New Repository**

1. **Log into GitHub**

2. **Click the green "New" button** (top right, or the "+" dropdown)

3. **Fill in repository details:**

   ```
   Repository name: feedback-generator-agent
   Description: AI-Powered Student Feedback Generator for IU
   
   ⚪ Public (recommended - allows free Streamlit deployment)
   ⚫ Private (requires paid Streamlit plan)
   
   Initialize repository:
   ☐ Add a README file (DON'T check - we have one!)
   ☐ Add .gitignore (DON'T check - we have one!)
   ☐ Choose a license (optional)
   ```

4. **Click "Create repository"** (green button)

**✅ Repository created!**

---

### **Step 2.3: Upload Files to GitHub**

You'll see a page with upload instructions. Here's the easiest way:

#### **Method A: Upload via Web Interface (Easiest!)**

1. **On your new repository page**, click "uploading an existing file"

2. **Drag ALL your files** from `feedback-agent-deploy` folder into the upload area
   - You can drag the entire folder contents at once!
   - Make sure to include the `.streamlit` folder

3. **Important**: To upload the `.streamlit` folder:
   - If it doesn't upload automatically, click "Add file" → "Create new file"
   - Type: `.streamlit/config.toml`
   - Paste the contents of `config.toml`
   - Commit
   - Repeat for `.streamlit/secrets.toml.example`

4. **Scroll down** to "Commit changes"

5. **Commit message**: Type:
   ```
   Initial deployment: Student Feedback Generator Agent
   ```

6. **Click "Commit changes"** (green button)

**⏰ Wait**: 10-20 seconds for upload to complete

---

#### **Method B: Upload via GitHub Desktop (Alternative)**

If you prefer a desktop app:

1. Download [GitHub Desktop](https://desktop.github.com)
2. Install and sign in
3. Click "Add" → "Add existing repository"
4. Select your `feedback-agent-deploy` folder
5. Click "Publish repository"
6. Done!

---

### **Step 2.4: Verify Upload**

On your GitHub repository page, you should see:

```
feedback-generator-agent/
├── 📁 .streamlit/
│   ├── config.toml
│   └── secrets.toml.example
├── .gitignore
├── app.py
├── templates.py
├── parser.py
├── doc_generator.py
├── requirements.txt
├── Dockerfile
├── README.md
├── run.sh
└── run.bat
```

**All files visible?** ✅ **Perfect!**

**Missing files?** Upload them individually using "Add file" → "Upload files"

---

## ☁️ **PART 3: DEPLOY TO STREAMLIT CLOUD** (10-15 minutes)

### **Step 3.1: Create Streamlit Account**

1. Go to [share.streamlit.io](https://share.streamlit.io)

2. **Click "Sign up" or "Get started"**

3. **Sign up with GitHub** (EASIEST!)
   - Click "Continue with GitHub"
   - Authorize Streamlit to access your GitHub
   - ✅ Done!

**Why GitHub sign-up?**
- One less password to remember
- Automatic connection to your repositories
- Easier deployment workflow

---

### **Step 3.2: Deploy Your App**

1. **On Streamlit Cloud dashboard**, click "New app" (or "Deploy an app")

2. **Fill in deployment form:**

   ```
   ┌─────────────────────────────────────────┐
   │ Repository:                             │
   │ [YOUR-USERNAME/feedback-generator-agent]│
   │                                         │
   │ Branch:                                 │
   │ [main]                                  │
   │                                         │
   │ Main file path:                         │
   │ app.py                                  │
   │                                         │
   │ App URL (optional):                     │
   │ [iu-feedback-generator]                 │
   └─────────────────────────────────────────┘
   ```

   **Important fields:**
   - **Repository**: Select `YOUR-USERNAME/feedback-generator-agent`
   - **Branch**: Use `main` (or `master` if that's what GitHub created)
   - **Main file path**: Type exactly `app.py`
   - **App URL**: Choose something memorable like:
     - `iu-feedback-generator`
     - `feedback-agent-iu`
     - `student-feedback-tool`

3. **Click "Deploy!"** (big button)

**⏰ Wait**: 2-5 minutes while Streamlit:
- Clones your repository
- Installs dependencies
- Starts your app

**You'll see logs scrolling:**
```
⏳ Cloning repository...
⏳ Installing Python packages...
⏳ Starting Streamlit...
⏳ Running your app...
```

---

### **Step 3.3: Initial Deployment (Will Show Error)**

When deployment finishes, you'll see your app... but it will show:

```
❌ Error: API Key Required

Please provide an Anthropic API key in the sidebar
or configure it in Streamlit secrets.
```

**This is NORMAL!** We haven't added the API key yet.

**Next step: Add your API key securely!**

---

### **Step 3.4: Configure API Key (CRITICAL!)**

**This is the most important step for security!**

1. **On your deployed app page**, look for the **menu button** (≡ or three dots, top right)

2. **Click**: Menu → "Settings"

3. **In Settings panel**, click the **"Secrets"** tab

4. **You'll see a text editor**. Type EXACTLY this:

   ```toml
   ANTHROPIC_API_KEY = "sk-ant-api03-YOUR-ACTUAL-KEY-HERE"
   ```

   **⚠️ CRITICAL FORMATTING:**
   - ALL CAPS: `ANTHROPIC_API_KEY`
   - Space before and after `=`
   - Double quotes around your key
   - Your actual API key between the quotes

   **Example (with fake key):**
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-api03-abc123xyz789examplekey"
   ```

5. **Click "Save"** button

6. **IMPORTANT**: Click "Reboot app" (in the menu)
   - This is REQUIRED for the key to load!
   - Without rebooting, the app won't work!

**⏰ Wait**: 30 seconds for app to restart

---

### **Step 3.5: Verify It Works!**

After the app reboots:

1. **You should see**: The app loads without errors!

2. **Test it**:
   - Click "Select Assignment Category"
   - Choose any template
   - Verify it shows options

3. **If you see the interface working**: ✅ **SUCCESS!**

**Still seeing errors?** See Troubleshooting section below.

---

### **Step 3.6: Get Your Public URL**

**Your app is now live!** The URL is:

```
https://your-chosen-name.streamlit.app
```

**Example:**
```
https://iu-feedback-generator.streamlit.app
```

**Copy this URL** - you'll share it with your TA and students!

---

## 🎓 **PART 4: SHARE WITH TA AND STUDENTS** (5 minutes)

### **Step 4.1: Test from Different Device**

Before sharing widely:

1. **Open your phone** or another computer
2. **Go to your app URL**
3. **Verify**:
   - App loads
   - Can select templates
   - Interface is responsive
   - No error messages

**Works on different devices?** ✅ **Ready to share!**

---

### **Step 4.2: Prepare User Guide**

Create a simple document for your TA/students:

```
📝 Student Feedback Generator - Quick Start

URL: https://iu-feedback-generator.streamlit.app

WHAT IT DOES:
This tool generates AI-powered feedback for student assignments.

WHO CAN USE IT:
- Teaching Assistants
- Course instructors
- Anyone with the URL (no login required!)

HOW TO USE:
1. Go to the URL above
2. Select your assignment type
3. Upload your student submissions file
4. Click "Generate Feedback"
5. Download the Word document

SUPPORTED FILE FORMATS:
- .docx (Word documents)
- .txt (Plain text files)

FILE PREPARATION:
Each student's submission should start with:
Student: [Student Name]

Example:
Student: Jane Doe
[Jane's submission here...]

Student: John Smith
[John's submission here...]

QUESTIONS?
Contact Professor BenMessaoud
```

---

### **Step 4.3: Share the Link**

**Email Template for TA:**

```
Subject: Student Feedback Generator Tool - Now Available!

Dear [TA Name],

I'm excited to share a new AI-powered tool to help with student
feedback generation:

🔗 https://iu-feedback-generator.streamlit.app

This tool can:
✅ Generate individualized feedback for each student
✅ Create collective synthesis and expert reflections
✅ Export formatted Word documents
✅ Support multiple assignment types

Please review the attached user guide and let me know if you
have any questions.

The tool is ready for immediate use!

Best regards,
Professor BenMessaoud
```

---

### **Step 4.4: Announce to Students (Optional)**

If students will use it directly:

```
Subject: New Feedback Tool Available

Dear Students,

We now have an AI-powered feedback tool available:

🔗 https://iu-feedback-generator.streamlit.app

This tool helps generate constructive feedback on assignments.
Your TA will use this tool, and you may access it as well for
peer feedback exercises.

Instructions are available at the link.

Best regards,
Professor BenMessaoud
```

---

## 🔒 **SECURITY & BEST PRACTICES**

### **API Key Security:**

✅ **DO:**
- Store key in Streamlit Cloud secrets (done! ✅)
- Use spending limits on Anthropic account
- Monitor usage regularly
- Keep key confidential

❌ **DON'T:**
- Put key in code files
- Commit key to GitHub
- Share key with others
- Email or text the key

### **Spending Limits:**

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Navigate to Settings → Limits
3. Set monthly budget: **$50** (recommended for class use)
4. Enable email alerts at 50% and 90%

### **Usage Monitoring:**

**Check weekly:**
- How many API calls made
- Current spending
- Any unusual activity

**Typical costs:**
- 20 students: ~$0.35 per batch
- 100 students per month: ~$7-10
- Well within reasonable budget!

---

## 📊 **MANAGING THE DEPLOYED APP**

### **Updating Your App:**

When you want to make changes:

1. **Edit files on GitHub**:
   - Go to your repository
   - Click the file to edit
   - Click pencil icon ✏️
   - Make changes
   - Commit

2. **Streamlit auto-redeploys!**
   - Takes 1-2 minutes
   - No manual deployment needed
   - Changes go live automatically

### **Monitoring Usage:**

**Streamlit Cloud Dashboard:**
- Shows visitor count
- Shows active sessions
- Shows resource usage
- Available at share.streamlit.io

### **Rebooting the App:**

If something goes wrong:

1. Go to share.streamlit.io
2. Find your app
3. Click menu (≡)
4. Click "Reboot app"
5. Wait 30 seconds

**When to reboot:**
- After changing secrets
- If app seems frozen
- After major GitHub updates
- To clear any errors

### **Viewing Logs:**

To debug issues:

1. Go to deployed app
2. Click menu (≡)
3. Click "Download logs"
4. Check for error messages

---

## 🆘 **TROUBLESHOOTING**

### **Problem: "Authentication Error"**

**Cause**: API key is wrong or not loaded

**Solutions:**
1. Go to Streamlit Settings → Secrets
2. Verify key format:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-your-key"
   ```
3. Check for:
   - ALL CAPS variable name
   - Double quotes around key
   - No extra spaces
   - Complete key copied
4. Save and **reboot app**

---

### **Problem: "App didn't wake up"**

**Cause**: Apps sleep after 7 days of inactivity

**Solution:**
1. Go to share.streamlit.io
2. Find your app
3. Click "Reboot app"
4. Wait 30 seconds
5. Try accessing again

---

### **Problem: "Module not found: streamlit"**

**Cause**: requirements.txt issue

**Solution:**
1. Check requirements.txt on GitHub
2. Verify it contains:
   ```
   streamlit>=1.36.0
   anthropic>=0.34.0
   python-docx>=1.1.0
   mammoth>=1.8.0
   ```
3. No typos, no extra characters
4. Redeploy if needed

---

### **Problem: Changes not showing**

**Solutions:**
1. Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
2. Check GitHub - are changes committed?
3. Check Streamlit dashboard - is it deploying?
4. Wait 2-3 minutes for auto-redeploy
5. Try incognito window

---

### **Problem: File upload fails**

**Cause**: File too large or wrong format

**Solutions:**
1. Check file is .docx or .txt
2. File should be under 50MB (plenty for text!)
3. Make sure file isn't password-protected
4. Try saving as .txt if .docx doesn't work

---

### **Problem: "No students found"**

**Cause**: File format doesn't match expected delimiters

**Solution:**
1. Check each submission starts with:
   ```
   Student: [Name]
   ```
2. No extra spaces before "Student:"
3. Each name on its own line
4. Submissions separated by blank lines
5. See the parser.py documentation for supported formats

---

## 📞 **GETTING HELP**

### **Streamlit Support:**

- Documentation: [docs.streamlit.io](https://docs.streamlit.io)
- Community Forum: [discuss.streamlit.io](https://discuss.streamlit.io)
- GitHub Issues: Report bugs

### **Anthropic Support:**

- Console: [console.anthropic.com](https://console.anthropic.com)
- Documentation: [docs.anthropic.com](https://docs.anthropic.com)
- API Status: Check for outages

### **Technical Issues:**

If you encounter technical issues:

1. Check this troubleshooting guide
2. Review Streamlit logs
3. Check GitHub repository
4. Test locally first (using `run.sh` or `run.bat`)
5. Contact Streamlit support if needed

---

## ✅ **DEPLOYMENT CHECKLIST**

Use this checklist to verify everything is done:

### **Before Deployment:**
- [ ] Have GitHub account
- [ ] Have Anthropic API key
- [ ] All project files downloaded
- [ ] Files organized in folder

### **GitHub Setup:**
- [ ] Repository created
- [ ] All files uploaded
- [ ] .streamlit folder uploaded
- [ ] README.md visible
- [ ] Repository is PUBLIC

### **Streamlit Deployment:**
- [ ] Streamlit account created
- [ ] App deployed from GitHub
- [ ] API key added to secrets
- [ ] App rebooted after adding key
- [ ] App loads without errors

### **Testing:**
- [ ] Can select assignment type
- [ ] Can upload test file
- [ ] Feedback generates successfully
- [ ] Can download Word document
- [ ] Works on mobile device
- [ ] Works in incognito mode

### **Sharing:**
- [ ] Public URL obtained
- [ ] URL tested from different device
- [ ] User guide created
- [ ] TA notified
- [ ] Students notified (if applicable)

### **Security:**
- [ ] API key in secrets (not code)
- [ ] Spending limits set
- [ ] Email alerts enabled
- [ ] Usage monitored

**All checked?** 🎉 **PERFECT DEPLOYMENT!** 🎉

---

## 🎊 **CONGRATULATIONS!**

**Your Feedback Generator Agent is now live and serving your class!**

**What you've accomplished:**
✅ Deployed a professional AI tool
✅ Made it accessible to TA and students
✅ Set up secure API configuration
✅ Created sustainable classroom tool

**Your URL:**
```
https://your-app-name.streamlit.app
```

**Impact:**
- ⏰ Saves hours of feedback time
- 📊 Provides consistent, quality feedback
- 🎓 Enhances student learning
- 💡 Empowers your TA
- 🌟 Uses cutting-edge AI for education

**Thank you for using AI to enhance education!** 🎓

---

## 📚 **APPENDIX: ADDITIONAL RESOURCES**

### **Video Tutorials:**
- [GitHub Basics](https://www.youtube.com/watch?v=0fKg7e37bQE)
- [Streamlit Cloud Deployment](https://www.youtube.com/watch?v=HKoOBiAaHGg)

### **Documentation:**
- [Streamlit Docs](https://docs.streamlit.io)
- [GitHub Docs](https://docs.github.com)
- [Anthropic API Docs](https://docs.anthropic.com)

### **Best Practices:**
- Regular backups of generated feedback
- Weekly usage monitoring
- Monthly cost reviews
- Quarterly security audits

---

**Ready to deploy?** Start with **PART 1** and follow step-by-step!

**Questions?** Refer to the Troubleshooting section!

**You've got this, Professor!** 💪🎓
