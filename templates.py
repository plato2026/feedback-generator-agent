"""
templates.py — Feedback Template Definitions
=============================================
Contains the four assignment feedback templates with system prompts,
Part A (individual) and Part B (collective) prompt builders, and metadata.

Each template is a dict with:
  - label, icon, description: UI display info
  - has_part_a: whether individual feedback is generated
  - part_a_label, part_b_label: section headers for the output document
  - format_help: instructions for file formatting shown to the user
  - system_prompt: the AI role/persona for this template
  - build_part_a(name, text, ctx): builds the Part A prompt for one student
  - build_part_b(summaries, ctx): builds the Part B collective prompt
"""

TEMPLATES = {

    # ─── TEMPLATE 1: HANDS-ON LEARNING ACTIVITY ──────────────────────

    "hands_on": {
        "label": "Hands-On Learning Activity",
        "icon": "🔬",
        "description": (
            "For activities where students build, create, or experiment with "
            "hands-on artifacts and write reflections. Generates **individual "
            "two-section critiques** (Section A1: Artifact, Section A2: Reflection) "
            "plus a **collective expert synthesis**."
        ),
        "has_part_a": True,
        "part_a_label": "Individualized Student Feedback",
        "part_b_label": "Collective Expert Synthesis — Masterclass",
        "format_help": (
            "Ensure each student's submission starts with: **Student: [Full Name]**. "
            "Include descriptions of their hands-on artifact and their written reflection."
        ),
        "system_prompt": (
            "You are a master educator and learning design critic with deep expertise "
            "across multiple disciplines. You serve as a thought partner to students "
            "learning through hands-on creation. Your feedback style is analytically "
            "rigorous yet deeply supportive—you see the creative intent behind every "
            "student's work and help them refine their thinking through precise, "
            "constructive guidance. You understand that hands-on activities produce "
            "multiple artifact types (visual, written, interactive, etc.), each "
            "requiring its own evaluative lens."
        ),
        "build_part_a": lambda name, text, ctx: f"""Generate individualized feedback for "{name}" on their hands-on learning activity submission.

FORMAT YOUR RESPONSE EXACTLY AS FOLLOWS:

**Section A1: Critique of the Hands-On Artifact**

Analyze the student's creation/experiment as a form of knowledge representation and creative execution. Consider dimensions relevant to the artifact type present in their submission:
- Conceptual Completeness and Design Intent
- Execution Quality and Depth of Insight
- Visual Clarity / Technical Execution / Craft (as applicable)

Provide 3–5 sentences that:
1. Acknowledge specific strengths in their artifact
2. Identify gaps or missed opportunities
3. Offer specific, actionable recommendations for improvement

**Section A2: Critique of the Written Reflection**

Analyze the student's written reflection for depth of insight, personal connection, and critical thinking. Consider:
- Engagement with the activity's core questions
- Evidence of genuine learning and evolution in thinking
- Integration of theory and practice
- Personal authenticity and critical self-assessment

Provide 3–5 sentences that:
1. Highlight strengths in the reflection
2. Identify underdeveloped areas
3. Offer guidance to deepen future reflections

IMPORTANT: Address the student directly by name. Keep feedback concise, warm yet rigorous, and actionable. Honor their creative effort while pushing toward deeper understanding.

{"ASSIGNMENT CONTEXT:" + chr(10) + ctx + chr(10) if ctx else ""}
STUDENT SUBMISSION BY {name}:
{text}""",

        "build_part_b": lambda summaries, ctx: f"""Generate a "Collective Expert Synthesis — Masterclass" addressed to the entire class based on their hands-on learning activity submissions. This section should stand alone as an insightful essay that elevates everyone's understanding.

FORMAT YOUR RESPONSE WITH THESE EXACT SECTIONS:

**Introduction: Why This Activity Matters**
Affirm the core purpose of the activity. Acknowledge the range of approaches students took. Validate the difficulty. Frame it as engagement with enduring questions in the field.

**Theme 1: The Most Powerful Insights Students Generated**
Synthesize the most insightful moves, connections, or executions across multiple submissions. Highlight 2–3 exemplary approaches and explain why they are significant. Use these examples to teach.

**Theme 2: The Patterns of Struggle — Where the Activity Pushed Thinking**
Synthesize challenges multiple students encountered. Validate that struggles were shared. Offer expert frameworks, reframings, or mental models to navigate them more effectively.

**Theme 3: Connecting to the Broader Landscape**
Connect the activity's themes to current events, industry trends, research frontiers, or enduring questions. Ground in specific, contemporary examples. Address what current developments make this especially relevant now.

**Closing Challenge: The Work Ahead**
End with a powerful, inspiring call to students as emerging professionals. Leave them with a provocative question or challenge to carry forward.

Write in an authoritative yet warm voice. Make it approximately 600–800 words.

{"ASSIGNMENT CONTEXT:" + chr(10) + ctx + chr(10) if ctx else ""}
SUMMARY OF ALL STUDENT SUBMISSIONS:
{summaries}"""
    },

    # ─── TEMPLATE 2: CURRENT EVENTS & TREND REPORTS ──────────────────

    "current_events": {
        "label": "Current Events & Trend Reports",
        "icon": "📊",
        "description": (
            "For research-based reports analyzing AI trends, industry developments, "
            "and implications. Generates **three-part individual critiques** "
            "(What Worked / Gaps / Recommendations) plus a **collective expert reflection**."
        ),
        "has_part_a": True,
        "part_a_label": "Individualized Student Feedback",
        "part_b_label": "Collective Expert Reflection & Masterclass",
        "format_help": (
            "Ensure each student's submission starts with: **Student: [Full Name]**. "
            "Include their complete trend report or analysis text."
        ),
        "system_prompt": (
            "You are a distinguished professor and leading expert in AI-driven business "
            "innovation and information systems. Your teaching philosophy combines rigorous "
            "critical analysis with supportive, developmental guidance. You are skilled at "
            "identifying both the strengths and the gaps in student work and at delivering "
            "feedback that is direct, constructive, and actionable. Your tone is professional, "
            "respectful, and designed to elevate each student's understanding and performance."
        ),
        "build_part_a": lambda name, text, ctx: f"""Generate individualized feedback for "{name}" on their Current Events and Trend Report submission.

FORMAT YOUR RESPONSE EXACTLY AS FOLLOWS:

**What Worked Well:**
Begin with 1–2 sentences acknowledging what the student did effectively. Be specific about strengths related to the assignment objectives (depth of research, clarity of argument, use of examples, connection to course concepts).

**Critical Gaps & Missed Opportunities:**
In 2–3 sentences, identify what the student did not do well or omitted. Be direct but constructive. Point to specific gaps relative to the assignment's success criteria — weak analysis, outdated sources, superficial treatment of key concepts, failure to address counterarguments, etc. This section must be honest and specific to drive real improvement.

**Actionable Recommendations for Improvement:**
Provide 2–3 concrete, expert-level suggestions for how the student could strengthen their work. These should be practical and forward-looking, guiding them toward deeper research, sharper analysis, or more current perspectives. If relevant, point them toward specific frameworks, recent developments, or authoritative sources.

IMPORTANT: Address the student directly by name. Keep feedback concise, direct, and constructive.

{"ASSIGNMENT CONTEXT:" + chr(10) + ctx + chr(10) if ctx else ""}
STUDENT SUBMISSION BY {name}:
{text}""",

        "build_part_b": lambda summaries, ctx: f"""Generate a "Collective Expert Reflection & Masterclass" addressed to the entire class based on their Current Events and Trend Report submissions.

FORMAT YOUR RESPONSE WITH THESE EXACT SECTIONS:

**Synthesizing the Core Themes**
Identify the central themes, tensions, and questions the assignment surfaced. Acknowledge the range of approaches students took and validate the complexity of the topic.

**Deepening Understanding Through Expert Insight**
Offer your own expert-level analysis of the assignment's core topics. Do not simply repeat what students wrote. Instead, build upon their collective efforts to introduce:
1. Current, real-world developments that make the topic urgent and relevant.
2. Nuanced perspectives that challenge simplistic conclusions.
3. Frameworks and lenses that students can use to analyze similar problems in the future.

**Connecting to Students' Professional Futures**
Explicitly address why this analysis matters for their careers. What skills are they building? What questions will they need to answer as future managers, consultants, entrepreneurs, or policymakers? Ground this in realistic scenarios from contemporary industry practice.

Write in an authoritative yet accessible voice. Make it approximately 500–700 words.

{"ASSIGNMENT CONTEXT:" + chr(10) + ctx + chr(10) if ctx else ""}
SUMMARY OF ALL STUDENT SUBMISSIONS:
{summaries}"""
    },

    # ─── TEMPLATE 3: REFLECTION ACTIVITY ─────────────────────────────

    "reflection": {
        "label": "Reflection Activity",
        "icon": "💭",
        "description": (
            "For reflective writing where students connect theory with personal experience. "
            "Generates **individualized three-part critiques** (What Worked / Gaps / "
            "Recommendations) plus a **collective mentor-style guided reflection** for the whole class."
        ),
        "has_part_a": True,
        "part_a_label": "Individualized Student Feedback",
        "part_b_label": "Collective Reflective Feedback",
        "format_help": (
            "Ensure each student's reflection starts with: **Student: [Full Name]**. "
            "Include their complete reflection text."
        ),
        "system_prompt": (
            "You are a master educator and a leading thinker in the field of AI and "
            "Automation. You possess a rare gift for making complex, abstract concepts "
            "feel personally relevant and for guiding learners to connect theory with "
            "their own lived experiences. Your voice is wise, encouraging, and thought-provoking."
        ),
        "build_part_a": lambda name, text, ctx: f"""Generate individualized feedback for "{name}" on their Reflection Activity submission.

FORMAT YOUR RESPONSE EXACTLY AS FOLLOWS:

**What Worked Well:**
Begin with 1–2 sentences acknowledging what the student did effectively in their reflection. Be specific about strengths — depth of personal connection, quality of critical thinking, authenticity of voice, meaningful integration of course concepts with lived experience, or willingness to grapple with complexity and uncertainty.

**Critical Gaps & Missed Opportunities:**
In 2–3 sentences, identify what the student did not do well or omitted. Be direct but constructive. Point to specific gaps — superficial engagement with the prompts, failure to move beyond description into genuine analysis, lack of connection between personal experience and course concepts, missing consideration of alternative perspectives, or absence of critical self-assessment about their own assumptions.

**Actionable Recommendations for Improvement:**
Provide 2–3 concrete, expert-level suggestions for how the student could deepen their reflective practice. These should be practical and forward-looking — guiding them toward deeper introspection, stronger theory-practice connections, more nuanced reasoning, or more honest engagement with the discomfort that genuine reflection often surfaces.

IMPORTANT: Address the student directly by name. Keep feedback concise, warm yet honest, and actionable. Honor the personal nature of reflective writing while pushing toward deeper, more transformative thinking.

{"REFLECTION ACTIVITY CONTEXT:" + chr(10) + ctx + chr(10) if ctx else ""}
STUDENT REFLECTION BY {name}:
{text}""",

        "build_part_b": lambda summaries, ctx: f"""Generate "Collective Reflective Feedback" for the entire class. This is NOT individual critique — it is a guided, expert-level reflection that deepens everyone's understanding by building upon the themes the reflection activity explored.

FORMAT YOUR RESPONSE WITH THESE EXACT SECTIONS:

**1. Synthesis of Core Themes**
Eloquently synthesize the central themes and tensions the reflection activity surfaced. Acknowledge the different ways students grappled with these ideas. Validate the range of student experiences and set the stage for deeper exploration.

**2. Deepening the Reflection (The "So What" for You)**
This is the heart of the response. Act as a guide, prompting students to go one layer deeper in their thinking. Do NOT provide new external information. Instead, pose powerful, open-ended questions and offer new lenses or frameworks through which they can re-examine their initial thoughts. Extend their internal dialogue. Example tone: "Many of you touched on the theme of trust in AI. But let's push that further. What is the nature of that trust? Is it trust in the technology, or trust in the humans who built and deployed it?"

**3. Bridging to Your Professional Future (The "Now What")**
Connect the introspective themes directly to students' future roles as professionals. How will the personal stances they are developing now shape their actions, decisions, and ethical frameworks in the workplace? Ground this in realistic, contemporary scenarios.

Write in the tone of a mentor providing a personalized masterclass — insightful, supportive, and geared towards fostering individual growth within a shared learning journey. Keep to approximately 500–600 words. Must NOT evaluate or call out any specific student's post.

{"REFLECTION ACTIVITY CONTEXT:" + chr(10) + ctx + chr(10) if ctx else ""}
SUMMARY OF STUDENT REFLECTIONS:
{summaries}"""
    },

    # ─── TEMPLATE 4: DISCUSSION QUESTION ─────────────────────────────

    "discussion": {
        "label": "Discussion Question",
        "icon": "💬",
        "description": (
            "For discussion board responses. Generates **individualized three-part "
            "critiques** (What Worked / Gaps / Recommendations) plus a **masterclass-style "
            "meta-feedback** synthesis that serves as a 'gold standard' learning model."
        ),
        "has_part_a": True,
        "part_a_label": "Individualized Student Feedback",
        "part_b_label": "Meta-Feedback Masterclass",
        "format_help": (
            "Ensure each student's discussion post starts with: **Student: [Full Name]**. "
            "Include their complete discussion response."
        ),
        "system_prompt": (
            "You are an expert in instructional design and a leading authority on AI and "
            "Automation. Your communication style is authoritative, insightful, and accessible, "
            "capable of making complex, cutting-edge concepts clear and compelling for a "
            "diverse group of learners."
        ),
        "build_part_a": lambda name, text, ctx: f"""Generate individualized feedback for "{name}" on their Discussion Question submission.

FORMAT YOUR RESPONSE EXACTLY AS FOLLOWS:

**What Worked Well:**
Begin with 1–2 sentences acknowledging what the student did effectively in their discussion post. Be specific about strengths — quality of argumentation, depth of analysis, originality of perspective, effective use of examples or evidence, meaningful engagement with the discussion prompt, or ability to connect course concepts to real-world implications.

**Critical Gaps & Missed Opportunities:**
In 2–3 sentences, identify what the student did not do well or omitted. Be direct but constructive. Point to specific gaps — surface-level treatment of complex ideas, unsupported claims, failure to consider counterarguments or alternative perspectives, lack of engagement with course frameworks, missed opportunities to connect theory to contemporary practice, or absence of critical analysis beyond description.

**Actionable Recommendations for Improvement:**
Provide 2–3 concrete, expert-level suggestions for how the student could strengthen their discussion contributions. These should be practical and forward-looking — guiding them toward more nuanced argumentation, deeper engagement with multiple perspectives, stronger evidence-based reasoning, or more sophisticated connections between the discussion topic and their professional future.

IMPORTANT: Address the student directly by name. Keep feedback concise, direct, and constructive. Respect the conversational nature of discussion posts while pushing toward greater intellectual rigor and depth.

{"DISCUSSION QUESTION CONTEXT:" + chr(10) + ctx + chr(10) if ctx else ""}
STUDENT DISCUSSION POST BY {name}:
{text}""",

        "build_part_b": lambda summaries, ctx: f"""Generate comprehensive "Meta-Feedback" for the entire class. This is NOT feedback on any single student's post, but rather a masterclass-style response that elevates the collective understanding of the topic.

FORMAT YOUR RESPONSE WITH THESE EXACT SECTIONS:

**1. The Exemplary Synthesis**
Craft a powerful, holistic response that directly answers the discussion question. This should read like a "gold standard" post that synthesizes the core concepts, acknowledges different perspectives, and demonstrates a sophisticated understanding of the topic. It serves as a learning model for students.

**2. Deconstructing the Core**
Break down the key themes and complexities at the heart of the discussion. Explain why this specific topic is a critical pillar of the field. What are its foundational principles, inherent tensions, and nuances? Help students move from a surface-level understanding to a deeper, more critical analysis.

**3. Bridging to the Real World & Your Future**
Connect the discussion directly to current events, industry trends, and the future workplace. Explicitly address the "so what?" factor. How will the principles discussed manifest in the industries students will soon enter? What new roles, challenges, or opportunities does this create for them as future professionals? Ground in concrete, contemporary examples to make implications tangible and urgent.

Write in an engaging, authoritative voice as if you are a guest expert providing a masterclass. Keep to approximately 500–700 words. Must NOT reference or evaluate any specific student's contribution.

{"DISCUSSION QUESTION CONTEXT:" + chr(10) + ctx + chr(10) if ctx else ""}
SUMMARY OF STUDENT DISCUSSION POSTS:
{summaries}"""
    },
}
