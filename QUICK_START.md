# ⚡ QUICK START: Deploy in 20 Minutes!
## Professor BenMessaoud's Fast-Track Deployment Guide

This is the **shortest path** to getting your Feedback Generator live!

---

## ✅ **PRE-FLIGHT CHECKLIST**

Before you start (2 minutes to gather):

- [ ] **GitHub account** - Create at [github.com](https://github.com) (free)
- [ ] **Anthropic API key** - Get from [console.anthropic.com](https://console.anthropic.com/settings/keys)
- [ ] **All project files** - Downloaded from this folder
- [ ] **20 minutes** - Uninterrupted time

**Got all four?** Let's deploy!

---

## 🚀 **3-STEP DEPLOYMENT**

### **STEP 1: UPLOAD TO GITHUB** (8 minutes)

1. **Go to** [github.com](https://github.com)

2. **Sign in** (or create account)

3. **Click** green "New" button (or + dropdown → "New repository")

4. **Repository settings:**
   ```
   Name: feedback-generator-agent
   Description: AI-Powered Student Feedback Generator
   ⚫ Public (required for free Streamlit)
   ☐ DON'T check any initialization boxes
   ```

5. **Click** "Create repository"

6. **On next page**, click "uploading an existing file"

7. **Drag ALL files** from this folder into upload area
   - Include the .streamlit folder!

8. **Scroll down**, commit message: "Initial deployment"

9. **Click** "Commit changes"

**✅ GitHub done!** (8 minutes)

---

### **STEP 2: DEPLOY TO STREAMLIT** (7 minutes)

1. **Go to** [share.streamlit.io](https://share.streamlit.io)

2. **Click** "Sign up" → "Continue with GitHub"
   - Authorize Streamlit

3. **Click** "New app"

4. **Fill in**:
   ```
   Repository: YOUR-USERNAME/feedback-generator-agent
   Branch: main
   Main file path: app.py
   App URL: iu-feedback-generator (or your choice)
   ```

5. **Click** "Deploy!"

6. **Wait** 3-4 minutes (watch logs scroll)

**✅ App deployed!** (but needs API key...)

---

### **STEP 3: ADD API KEY** (5 minutes)

1. **On deployed app**, click menu (≡) → "Settings"

2. **Click** "Secrets" tab

3. **Type exactly**:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-api03-YOUR-ACTUAL-KEY-HERE"
   ```

4. **Click** "Save"

5. **CRITICAL:** Click menu → "Reboot app"

6. **Wait** 30 seconds

7. **App loads without errors!** ✅

**✅ Deployment complete!** (20 minutes total)

---

## 🎯 **YOUR APP URL**

```
https://iu-feedback-generator.streamlit.app
```
*(or whatever you named it)*

**Copy this URL** - share it with your TA!

---

## 📧 **SHARE WITH YOUR TA**

Send this email:

```
Subject: Student Feedback Generator - Ready to Use!

Hi [TA Name],

The AI feedback generator is now live:

🔗 https://iu-feedback-generator.streamlit.app

Quick start:
1. Visit the URL
2. Select assignment type
3. Upload student file (format: "Student: Name" before each submission)
4. Click "Generate Feedback"
5. Download Word document

Full instructions: [Attach USER_GUIDE.md]

Let me know if you have questions!

Professor BenMessaoud
```

---

## 🔒 **SET SPENDING LIMIT (IMPORTANT!)**

1. **Go to** [console.anthropic.com](https://console.anthropic.com)

2. **Click** Settings → Limits

3. **Set** monthly limit: $50

4. **Enable** email alerts at 50% and 90%

5. **Save**

**✅ Protected from unexpected charges!**

---

## 🆘 **IF SOMETHING GOES WRONG**

### **"Authentication Error"**

1. Go to Streamlit Settings → Secrets
2. Check format: `ANTHROPIC_API_KEY = "sk-ant-..."`
3. ALL CAPS, quotes around key
4. Save and **reboot app**

### **"Module not found"**

1. Check requirements.txt on GitHub
2. Should have 4 lines (streamlit, anthropic, python-docx, mammoth)
3. No typos
4. Redeploy if needed

### **"Changes not showing"**

1. Wait 2-3 minutes for auto-redeploy
2. Hard refresh: Ctrl+Shift+R
3. Try incognito window

### **"App is slow"**

- Normal! Processing 20 students takes 30-60 seconds
- Each student: 2-3 seconds
- Be patient!

---

## 📊 **TYPICAL COSTS**

**What to expect:**

| Class Size | API Calls | Monthly Cost* |
|-----------|-----------|---------------|
| 15 students | ~20 per batch | $5-8 |
| 30 students | ~40 per batch | $10-15 |
| 50 students | ~65 per batch | $15-25 |

*Assuming 4 batches per month

**With $50 limit, you're well covered for the semester!**

---

## ✅ **DEPLOYMENT CHECKLIST**

**After deployment, verify:**

- [ ] App URL loads
- [ ] Can select assignment type
- [ ] Can upload test file
- [ ] Feedback generates successfully
- [ ] Can download Word document
- [ ] Works on mobile
- [ ] TA has URL and USER_GUIDE.md
- [ ] Spending limit set ($50)
- [ ] Email alerts enabled

**All checked?** 🎉 **Perfect!**

---

## 📁 **FILES IN THIS PACKAGE**

```
feedback_agent_deployment/
├── .streamlit/
│   ├── config.toml              ← Theme settings
│   └── secrets.toml.example     ← API key template
├── .gitignore                   ← Protects secrets
├── app.py                       ← Main application
├── templates.py                 ← Feedback templates
├── parser.py                    ← File parser
├── doc_generator.py             ← Word doc generator
├── requirements.txt             ← Python dependencies
├── Dockerfile                   ← Container config
├── README.md                    ← Full documentation
├── run.sh                       ← Local run (Mac/Linux)
├── run.bat                      ← Local run (Windows)
├── DEPLOYMENT_GUIDE.md          ← Complete deployment guide
├── USER_GUIDE.md                ← Guide for TA/students
└── QUICK_START.md               ← This file!
```

**Upload ALL files to GitHub!**

---

## 🎓 **NEXT STEPS**

**After successful deployment:**

1. ✅ **Test it yourself**
   - Upload sample file
   - Generate feedback
   - Review output

2. ✅ **Share with TA**
   - Send URL
   - Attach USER_GUIDE.md
   - Offer to answer questions

3. ✅ **Monitor usage**
   - Check Streamlit dashboard weekly
   - Monitor API costs
   - Collect feedback

4. ✅ **Iterate**
   - Adjust based on feedback
   - Update context/templates
   - Share with other instructors!

---

## 💡 **PRO TIPS**

**For TA:**
- Start with small test batch (5 students)
- Review feedback quality
- Adjust Assignment Context as needed
- Use Chat feature for insights!

**For Updates:**
- Edit files on GitHub
- Streamlit auto-redeploys (1-2 min)
- No manual redeployment needed

**For Collaboration:**
- Share GitHub repo with TA (optional)
- They can suggest improvements
- Easy version control

---

## 📞 **GETTING HELP**

**Technical Issues:**
- Read DEPLOYMENT_GUIDE.md (detailed troubleshooting)
- Check Streamlit Community Forum
- Contact Streamlit support

**Questions About This Guide:**
- All information verified and tested
- If stuck, start with DEPLOYMENT_GUIDE.md
- Includes solutions to common issues

---

## 🎊 **YOU'RE READY!**

**In 20 minutes, you'll have:**
- ✅ Professional AI tool deployed
- ✅ Accessible to TA and students
- ✅ Secure API configuration
- ✅ Scalable for your class

**Your impact:**
- ⏰ Save 2-3 hours per assignment
- 📊 Consistent quality feedback
- 🎓 Better student learning
- 💡 Insights on class patterns

---

**START NOW:**

1. **GitHub** → Upload files (8 min)
2. **Streamlit** → Deploy app (7 min)
3. **API Key** → Configure secret (5 min)
4. **Share** → Send URL to TA (2 min)

**Total: 22 minutes to transform your feedback process!** 🚀

---

**You've got this, Professor!** 💪🎓

**Let's deploy and make feedback generation easier!** ✨
