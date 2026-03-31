# 📖 USER GUIDE: Student Feedback Generator
## Quick Start for TAs and Students

Welcome! This guide will help you use the Student Feedback Generator tool in just a few minutes.

---

## 🔗 **ACCESS THE TOOL**

**URL:** `https://[your-app-name].streamlit.app`

*(Professor BenMessaoud will provide the exact URL)*

**Requirements:**
- Web browser (Chrome, Firefox, Safari, Edge)
- Internet connection
- Student submission file (.docx or .txt)

**No login required!** Just visit the URL and start using it!

---

## 🎯 **WHAT THIS TOOL DOES**

The Feedback Generator creates AI-powered, constructive feedback for student assignments.

**Features:**
- ✅ **Individualized feedback** for each student
- ✅ **Collective synthesis** across all submissions
- ✅ **Multiple assignment types** supported
- ✅ **Professional Word documents** generated
- ✅ **Fast processing** (30-60 seconds)

---

## 📝 **PREPARING YOUR FILE**

### **Step 1: Collect Submissions**

Gather all student submissions into a single file (.docx or .txt)

### **Step 2: Format the File**

Each student's submission should start with their name:

```
Student: Jane Doe
[Jane's complete submission text here - can be multiple paragraphs]

Student: John Smith
[John's complete submission text here - can be multiple paragraphs]

Student: Maria Garcia
[Maria's complete submission text here...]
```

### **Step 3: Supported Formats**

The tool recognizes these formats:
- `Student: [Name]` ✅ **Recommended**
- `Name: [Name]`
- `Submission by: [Name]`
- `--- [Name] ---`
- `## [Name]`

### **Example File:**

```
Student: Jane Doe
I found the hands-on learning activity very insightful. Working with
the actual system helped me understand the theoretical concepts better.
The artifact I created demonstrates my understanding of...

Student: John Smith
This activity challenged my initial assumptions about the topic. Through
the practical work, I realized that...

Student: Maria Garcia
The most significant learning moment came when I had to troubleshoot the
system. This forced me to...
```

**Tips:**
- Keep each student's submission together
- Don't skip the name header
- Use consistent formatting
- Include complete submissions

---

## 🚀 **USING THE TOOL (5-STEP WORKFLOW)**

### **Step 1: Access the Tool**

1. Open your web browser
2. Go to the URL provided by Professor BenMessaoud
3. The app loads - you're ready!

---

### **Step 2: Select Assignment Type**

1. **Click the dropdown**: "Select Assignment Category"

2. **Choose your assignment type**:
   - 🔬 **Hands-On Learning Activity**
   - 📊 **Current Events & Trend Reports**
   - 💭 **Reflection Activity**
   - 💬 **Discussion Question**

3. **Read the description** that appears

---

### **Step 3: Provide Context (Optional but Recommended)**

1. **Expand**: "📋 Assignment Context" section

2. **Add information** like:
   - Assignment prompt
   - Rubric criteria
   - Learning objectives
   - Special instructions

**Example:**
```
This hands-on activity asked students to:
1. Set up a development environment
2. Create a simple application
3. Reflect on challenges and learning

Evaluation criteria:
- Technical accuracy (40%)
- Depth of reflection (30%)
- Documentation quality (30%)
```

**Why add context?**
- Better, more specific feedback
- Aligned with your rubric
- More relevant insights

---

### **Step 4: Upload Student Submissions**

1. **Click**: "📤 Upload Student Submissions"

2. **Click**: "Browse files" button

3. **Select your file** (.docx or .txt)

4. **Wait** for upload (usually instant)

5. **Review parsed students**:
   ```
   ✅ Successfully parsed 15 students:
   • Jane Doe (245 words)
   • John Smith (312 words)
   • Maria Garcia (198 words)
   ...
   ```

6. **Toggle students** on/off if needed:
   - Check boxes to include/exclude specific students
   - Useful if you want to process a subset

---

### **Step 5: Generate Feedback**

1. **Click**: "🎯 Generate Feedback" button (big green button)

2. **Watch the progress**:
   ```
   ⏳ Generating individualized feedback...
   [Progress bar]
   Processing: Jane Doe (1/15)
   Processing: John Smith (2/15)
   ...
   ```

3. **Wait**: 30-60 seconds (depends on number of students)

4. **See completion**:
   ```
   ✅ Feedback generation complete!
   
   📊 Summary:
   • Students processed: 15
   • Individual feedbacks: 15
   • Collective synthesis: ✅
   • Total time: 42 seconds
   ```

5. **Download the document**:
   - Click "📥 Download Feedback Document"
   - File saves as: `Feedback_YYYYMMDD_HHMMSS.docx`

---

## 📄 **UNDERSTANDING THE OUTPUT**

### **Word Document Structure:**

**Title Page:**
- Assignment type
- Date generated
- Course information

**Part A: Individualized Student Feedback**
- One section per student
- Customized feedback based on submission
- Structured by template type:
  - **Hands-On**: Artifact analysis + Reflection analysis
  - **Current Events**: What worked + Gaps + Recommendations
  - **Reflection**: What worked + Gaps + Recommendations
  - **Discussion**: What worked + Gaps + Recommendations

**Part B: Collective Synthesis**
- Expert analysis across all submissions
- Common patterns and themes
- Collective strengths and growth areas
- Masterclass teaching moments

---

## 💬 **USING THE CHAT FEATURE**

The tool includes a Chat tab for interactive help!

### **When Feedback Session is Active:**

The AI assistant knows about:
- Your assignment type and context
- All student names and submissions
- Generated feedback

**Ask things like:**
- "What patterns do you see across all submissions?"
- "Which students might need extra support?"
- "Suggest talking points for next week's lecture"
- "Help me phrase this feedback more constructively"

### **When No Session Active (General Mode):**

The AI can help with:
- Assignment design
- Rubric creation
- Grading strategies
- Pedagogical questions

**Example Chat Queries:**

```
✅ "What common misconceptions appear in these reflections?"
✅ "Which students demonstrated deep critical thinking?"
✅ "Suggest 3 lecture topics based on student gaps"
✅ "How can I improve this assignment prompt for next semester?"
✅ "Draft an email announcement about common issues"
```

---

## ⚙️ **ADVANCED FEATURES**

### **Processing Subsets of Students:**

1. Upload your full file
2. **Uncheck** students you don't want to process
3. Generate feedback for selected students only

**Use cases:**
- Process only late submissions
- Re-generate feedback for specific students
- Test with small groups first

### **Regenerating Feedback:**

Want different feedback?

1. Click "🔄 Start Over" (top of page)
2. Upload same file
3. Adjust context if desired
4. Generate again

**Each generation is unique** - slight variations in phrasing and emphasis.

### **Exporting for Different Purposes:**

The Word document can be:
- Printed for physical distribution
- Emailed to students
- Converted to PDF
- Edited before distribution
- Stored for records

---

## 📊 **TEMPLATE COMPARISON**

| Template | Individual Feedback Structure | Collective Synthesis |
|----------|------------------------------|---------------------|
| **Hands-On Learning** | Section A1 (Artifact) + A2 (Reflection) | Expert Synthesis Masterclass |
| **Current Events** | What Worked / Gaps / Recommendations | Expert Reflection & Masterclass |
| **Reflection Activity** | What Worked / Gaps / Recommendations | Collective Reflective Feedback |
| **Discussion Question** | What Worked / Gaps / Recommendations | Meta-Feedback Masterclass |

**Choose the template that matches your assignment type for best results!**

---

## 🆘 **TROUBLESHOOTING**

### **"No students found"**

**Problem:** File doesn't have proper delimiters

**Solution:**
1. Check each submission starts with `Student: [Name]`
2. Name is on its own line
3. No extra characters before "Student:"

---

### **"File upload failed"**

**Problem:** File issue

**Solutions:**
- Save as .txt and try again
- Check file isn't password-protected
- Reduce file size if very large
- Try different browser

---

### **"Authentication Error"**

**Problem:** API key issue (administrator needs to fix)

**Solution:**
- Refresh the page and try again
- If persists, contact Professor BenMessaoud
- This is a backend configuration issue

---

### **Feedback seems generic**

**Problem:** Not enough context provided

**Solution:**
- Add more detail in Assignment Context section
- Include rubric criteria
- Specify learning objectives
- Be specific about what you're evaluating

---

### **Document won't download**

**Solutions:**
- Check popup blocker isn't blocking download
- Try different browser
- Right-click download button → "Save link as"
- Check Downloads folder (might be there already!)

---

### **App is slow**

**Causes & Solutions:**

**Normal behavior:**
- Processing 20+ students takes time
- Each student: 2-3 seconds
- Collective synthesis: 5-10 seconds
- **This is expected!**

**Actually slow:**
- Try at different time of day
- Check your internet connection
- Close other browser tabs
- Refresh and try again

---

## 💡 **TIPS & BEST PRACTICES**

### **For Best Results:**

1. **Provide Context**
   - Always fill in Assignment Context
   - Include rubric details
   - Mention learning objectives

2. **Format Files Properly**
   - Use consistent student delimiters
   - Keep submissions together
   - Include complete text

3. **Review Before Distributing**
   - Read generated feedback
   - Check for accuracy
   - Edit if needed
   - Personalize further if desired

4. **Use Chat Feature**
   - Get insights on patterns
   - Identify struggling students
   - Plan follow-up activities

### **Time-Saving Workflow:**

```
Monday: Upload week's submissions → Generate feedback (5 min)
Tuesday: Review document, make edits (15 min)
Wednesday: Distribute to students (5 min)

Total time: 25 minutes vs. 3-4 hours manual feedback!
```

---

## 📧 **GETTING HELP**

### **Technical Issues:**
Contact Professor BenMessaoud with:
- Screenshot of error
- Description of what you were doing
- Your browser and operating system

### **Pedagogical Questions:**
- Use the Chat feature in the app!
- Ask about assignment design
- Get suggestions for rubrics
- Discuss grading strategies

### **Feature Requests:**
- Email Professor BenMessaoud
- Suggest improvements
- Report bugs
- Request new templates

---

## 🎓 **LEARNING OUTCOMES**

Using this tool, you'll:

✅ **Save time** on feedback generation  
✅ **Maintain consistency** across student feedback  
✅ **Identify patterns** in student learning  
✅ **Provide constructive** individualized feedback  
✅ **Generate insights** for teaching improvement  

---

## ✅ **QUICK REFERENCE CHECKLIST**

Before generating feedback:

- [ ] File prepared with student names
- [ ] Assignment type selected
- [ ] Context provided (recommended)
- [ ] File uploaded successfully
- [ ] Students parsed correctly
- [ ] Selected students to process

After generating:

- [ ] Feedback document downloaded
- [ ] Content reviewed
- [ ] Any edits made
- [ ] Document distributed to students
- [ ] Original file saved for records

---

## 🎯 **SUMMARY**

**In 5 minutes, you can:**

1. Visit the URL
2. Select assignment type
3. Upload student file
4. Generate feedback
5. Download Word document

**It's that simple!**

---

## 📞 **CONTACT**

**Professor Fawzi BenMessaoud**  
Luddy School of Informatics, Computing, and Engineering  
Indiana University Indianapolis

**Tool URL:** *[Provided by professor]*

---

**Happy feedback generating!** 🎉

**Let AI help you help your students!** 🚀
