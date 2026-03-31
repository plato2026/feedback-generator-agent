"""
app.py — Student Feedback Generator Agent
==========================================
A Streamlit application that guides educators through a workflow
to generate AI-powered, template-driven feedback for student submissions,
with a built-in Chat feature for follow-up questions and clarifications.

Built for Professor Fawzi BenMessaoud
Luddy School of Informatics, Computing, and Engineering
Indiana University Indianapolis

Usage:
    streamlit run app.py
"""

import streamlit as st
import anthropic
from datetime import datetime

from templates import TEMPLATES
from parser import (
    parse_students, extract_text_from_docx, StudentSubmission,
    process_file_by_type, extract_files_from_zip, process_multiple_files,
    create_submission_from_file
)
from doc_generator import generate_feedback_docx


# ─── PAGE CONFIG ──────────────────────────────────────────────────────

st.set_page_config(
    page_title="Feedback Generator Agent",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CUSTOM CSS ───────────────────────────────────────────────────────

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400&family=Source+Sans+3:wght@400;600;700&display=swap');

    .main .block-container { max-width: 920px; padding-top: 2rem; }
    h1, h2, h3 { font-family: 'Crimson Pro', Georgia, serif !important; }
    h1 { color: #1a1a2e !important; }
    h2 { color: #2E5C8A !important; }

    .agent-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #2d3561 100%);
        padding: 16px 24px; border-radius: 10px; margin-bottom: 24px;
        display: flex; align-items: center; gap: 14px;
    }
    .agent-header .logo {
        width: 42px; height: 42px; border-radius: 10px;
        background: linear-gradient(135deg, #c06030, #e8a87c);
        display: flex; align-items: center; justify-content: center;
        font-size: 20px; font-weight: 800; color: white;
    }
    .agent-header .title { color: #f0ebe3; font-size: 18px; font-weight: 700; font-family: 'Crimson Pro', serif; }
    .agent-header .subtitle { color: #8b8b9e; font-size: 11px; letter-spacing: 2px; text-transform: uppercase; }

    .badge { display: inline-block; padding: 3px 9px; border-radius: 4px; font-size: 10px; font-weight: 600; margin-right: 4px; }
    .badge-green { background: rgba(42,125,95,0.1); color: #2a7d5f; border: 1px solid rgba(42,125,95,0.25); }
    .badge-purple { background: rgba(107,76,154,0.1); color: #6b4c9a; border: 1px solid rgba(107,76,154,0.25); }

    .success-banner {
        background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px;
        padding: 24px; text-align: center; margin-bottom: 20px;
    }

    .streamlit-expanderHeader { font-family: 'Crimson Pro', serif !important; font-weight: 600 !important; }

    div[data-testid="stSidebar"] { background: #1a1a2e; }
    div[data-testid="stSidebar"] * { color: #e0ddd8 !important; }
    div[data-testid="stSidebar"] .stMarkdown h1,
    div[data-testid="stSidebar"] .stMarkdown h2,
    div[data-testid="stSidebar"] .stMarkdown h3 { color: #f0ebe3 !important; }

    /* Chat styling */
    .chat-context-box {
        background: rgba(46,92,138,0.06); border: 1px solid rgba(46,92,138,0.15);
        border-radius: 8px; padding: 12px 16px; margin-bottom: 16px;
        font-size: 13px; color: #555;
    }
    .chat-context-box strong { color: #2E5C8A; }
    .chat-hint {
        background: #fdfcfa; border: 1px solid #e8e4de; border-radius: 8px;
        padding: 12px 16px; margin-bottom: 12px; font-size: 12px; color: #888;
    }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ─── SESSION STATE INITIALIZATION ─────────────────────────────────────

DEFAULTS = {
    "step": 0,
    "category": None,
    "students": [],
    "parse_error": None,
    "pattern_used": None,
    "assignment_ctx": "",
    "part_a_results": [],
    "part_b_result": "",
    "generation_error": None,
    "doc_bytes": None,
    "chat_messages": [],        # Chat history for the Chat tab
    "active_tab": "generator",  # Track which tab is active
}

for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v


def reset_state():
    """Reset feedback generator state (preserves chat history)."""
    saved_chat = st.session_state.chat_messages
    saved_tab = st.session_state.active_tab
    for k, v in DEFAULTS.items():
        st.session_state[k] = v
    st.session_state.chat_messages = saved_chat
    st.session_state.active_tab = saved_tab


def go_to_step(n):
    st.session_state.step = n


# ─── SIDEBAR: API KEY & NAVIGATION ───────────────────────────────────

with st.sidebar:
    st.markdown("### 🔑 Configuration")

    default_key = ""
    try:
        default_key = st.secrets.get("ANTHROPIC_API_KEY", "")
    except Exception:
        pass

    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        value=default_key,
        help="Your key is used only for API calls and is never stored.",
        placeholder="sk-ant-api03-..."
    )

    if default_key and api_key == default_key:
        st.caption("✅ Key loaded from app secrets")

    st.divider()

    # Step indicator for Feedback Generator
    step_names = ["Select Category", "Upload Files", "Review", "Generate", "Results"]
    st.markdown("### 📍 Feedback Workflow")
    for i, name in enumerate(step_names):
        if i < st.session_state.step:
            st.markdown(f"✅ ~~{name}~~")
        elif i == st.session_state.step:
            st.markdown(f"🔵 **{name}** ← current")
        else:
            st.markdown(f"⬜ {name}")

    st.divider()

    if st.session_state.step > 0:
        if st.button("🔄 Start Over", use_container_width=True):
            reset_state()
            st.rerun()

    # Chat status
    if st.session_state.chat_messages:
        st.markdown(f"### 💬 Chat")
        st.caption(f"{len(st.session_state.chat_messages)} messages in conversation")
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.chat_messages = []
            st.rerun()

    st.markdown("---")
    st.markdown(
        "<div style='font-size:10px;color:#666;text-align:center;'>"
        "Student Feedback Generator Agent<br>"
        "Built for Prof. BenMessaoud<br>"
        "Luddy School · IU Indianapolis"
        "</div>",
        unsafe_allow_html=True,
    )


# ─── HEADER ──────────────────────────────────────────────────────────

st.markdown("""
<div class="agent-header">
    <div class="logo">F</div>
    <div>
        <div class="title">Student Feedback Generator Agent</div>
        <div class="subtitle">AI-Powered Assessment Tool</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ─── HELPER: Call Anthropic API ───────────────────────────────────────

def call_anthropic(system_prompt: str, user_prompt: str, key: str) -> str:
    """Call the Anthropic API and return the text response."""
    client = anthropic.Anthropic(api_key=key)
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return "\n".join(block.text for block in message.content if block.type == "text")


def call_anthropic_chat(system_prompt: str, messages: list, key: str) -> str:
    """Call the Anthropic API with full conversation history for chat."""
    client = anthropic.Anthropic(api_key=key)
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        system=system_prompt,
        messages=messages,
    )
    return "\n".join(block.text for block in message.content if block.type == "text")


# ─── BUILD CHAT CONTEXT ──────────────────────────────────────────────

def build_chat_system_prompt() -> str:
    """Build a context-aware system prompt for the chat based on current session state."""
    base = (
        "You are an expert educational AI assistant embedded in the Student Feedback "
        "Generator Agent — a tool built for Professor Fawzi BenMessaoud at the Luddy School "
        "of Informatics, Computing, and Engineering at Indiana University Indianapolis. "
        "You help the professor and teaching assistants with questions about student feedback, "
        "assignment design, grading strategies, interpreting student submissions, refining "
        "feedback language, understanding learning patterns, and any other educational matters.\n\n"
        "You are knowledgeable about educational pedagogy, assessment design, constructive "
        "feedback best practices, AI in education, and the specific course 'Human-AI "
        "Collaborative Systems.' You are warm, collegial, and intellectually rigorous.\n\n"
    )

    # Add context from the current feedback session
    context_parts = []

    cat = st.session_state.category
    if cat and cat in TEMPLATES:
        T = TEMPLATES[cat]
        context_parts.append(
            f"CURRENT SESSION: The user is working on feedback for a '{T['label']}' assignment."
        )

    if st.session_state.assignment_ctx:
        ctx_excerpt = st.session_state.assignment_ctx[:1500]
        context_parts.append(
            f"ASSIGNMENT CONTEXT/RUBRIC:\n{ctx_excerpt}"
        )

    students = st.session_state.students
    if students:
        names = [s.name for s in students]
        context_parts.append(
            f"STUDENTS IN THIS BATCH ({len(students)}): {', '.join(names)}"
        )
        # Include brief excerpts of student submissions
        excerpts = []
        for s in students[:20]:  # Cap at 20 to avoid token overflow
            excerpt = s.text[:400] + ("…" if len(s.text) > 400 else "")
            excerpts.append(f"[{s.name}]: {excerpt}")
        context_parts.append(
            "STUDENT SUBMISSION EXCERPTS:\n" + "\n---\n".join(excerpts)
        )

    if st.session_state.part_a_results:
        fb_summary = []
        for r in st.session_state.part_a_results:
            fb_summary.append(f"[{r['name']}]: {r['feedback'][:300]}…")
        context_parts.append(
            "GENERATED INDIVIDUAL FEEDBACK (EXCERPTS):\n" + "\n---\n".join(fb_summary)
        )

    if st.session_state.part_b_result:
        context_parts.append(
            f"GENERATED COLLECTIVE SYNTHESIS (EXCERPT):\n{st.session_state.part_b_result[:800]}…"
        )

    if context_parts:
        base += (
            "You have access to the following context from the current feedback session. "
            "Use this information to give specific, grounded answers when relevant. "
            "You can reference specific students by name, quote or discuss their submissions, "
            "explain feedback decisions, suggest refinements, or answer questions about "
            "patterns you observe.\n\n"
            + "\n\n".join(context_parts)
        )
    else:
        base += (
            "No feedback session is currently active. You can still help with general "
            "questions about assignment design, feedback strategies, grading, pedagogy, "
            "or anything else related to teaching."
        )

    return base


# ═══════════════════════════════════════════════════════════════════════
# MAIN TABS
# ═══════════════════════════════════════════════════════════════════════

tab_generator, tab_chat = st.tabs(["📝 Feedback Generator", "💬 Chat with Agent"])


# ═══════════════════════════════════════════════════════════════════════
# TAB 1: FEEDBACK GENERATOR (Original 5-step workflow)
# ═══════════════════════════════════════════════════════════════════════

with tab_generator:

    # ═══ STEP 0: CATEGORY SELECTION ═══════════════════════════════════

    if st.session_state.step == 0:
        st.markdown("## What are you grading today?")
        st.markdown(
            "Select the assignment type to load the matching feedback template, "
            "tone, and output structure."
        )

        cols = st.columns(2)
        template_keys = list(TEMPLATES.keys())

        for i, key in enumerate(template_keys):
            t = TEMPLATES[key]
            col = cols[i % 2]
            with col:
                with st.container(border=True):
                    st.markdown(f"### {t['icon']} {t['label']}")
                    st.markdown(t["description"])
                    badge_html = '<span class="badge badge-green">Part A: Individual</span>'
                    badge_html += '<span class="badge badge-purple">Part B: Collective</span>'
                    st.markdown(badge_html, unsafe_allow_html=True)
                    if st.button(f"Select → {t['label']}", key=f"cat_{key}", use_container_width=True):
                        st.session_state.category = key
                        go_to_step(1)
                        st.rerun()


    # ═══ STEP 1: FILE UPLOAD ═════════════════════════════════════════

    elif st.session_state.step == 1:
        cat_key = st.session_state.category
        T = TEMPLATES[cat_key]

        st.markdown(f"## {T['icon']} {T['label']}")
        st.markdown(
            "Upload student submissions and optionally provide the assignment "
            "prompt for context-aware feedback."
        )

        # Assignment context
        with st.expander("📋 Assignment Context (Optional — Strongly Recommended)", expanded=True):
            st.markdown(
                "Paste the assignment prompt, rubric, or success criteria below. "
                "This allows the AI to evaluate student work against **your specific "
                "learning objectives** rather than generic standards."
            )
            ctx = st.text_area(
                "Assignment Instructions / Rubric",
                value=st.session_state.assignment_ctx,
                height=150,
                placeholder="Paste your assignment instructions, learning objectives, rubric, or success criteria here...",
                label_visibility="collapsed",
            )
            st.session_state.assignment_ctx = ctx

        # File format instructions
        st.markdown("### 📤 Upload Student Submissions")

        st.info(
            f"📋 **Supported File Formats**\n\n"
            f"✅ **Single file with all submissions:** .docx, .txt, .md, .pdf\n"
            f"✅ **Individual student files:** .docx, .pdf, .pptx, .xlsx, .png, .jpg\n"
            f"✅ **ZIP folder:** Upload entire Canvas export folder!\n\n"
            f"**Format for combined files:**\n"
            f"```\n"
            f"Student: Jane Doe\n"
            f"[Jane's complete submission text here...]\n\n"
            f"Student: John Smith\n"
            f"[John's complete submission text here...]\n"
            f"```\n\n"
            f"**For ZIP files:** Each file should be named with student name or contain 'Student: [Name]' header."
        )

        # Upload mode selection
        upload_mode = st.radio(
            "Upload Mode",
            ["📄 Single File (all submissions)", "📁 Multiple Files", "🗜️ ZIP Folder (Canvas Export)"],
            horizontal=True
        )

        uploaded_files = []
        
        # ═══ SINGLE FILE MODE ═══
        if upload_mode == "📄 Single File (all submissions)":
            uploaded_file = st.file_uploader(
                "Choose a file",
                type=["docx", "txt", "md", "doc", "pdf"],
                help="Upload a single file containing all student submissions separated by 'Student: [Name]' headers.",
            )
            if uploaded_file:
                uploaded_files = [(uploaded_file.name, uploaded_file.getvalue())]
        
        # ═══ MULTIPLE FILES MODE ═══
        elif upload_mode == "📁 Multiple Files":
            uploaded_file_list = st.file_uploader(
                "Choose files",
                type=["docx", "txt", "md", "doc", "pdf", "pptx", "xlsx", "png", "jpg", "jpeg"],
                accept_multiple_files=True,
                help="Upload multiple files - one per student or containing multiple students each."
            )
            if uploaded_file_list:
                uploaded_files = [(f.name, f.getvalue()) for f in uploaded_file_list]
        
        # ═══ ZIP MODE ═══
        elif upload_mode == "🗜️ ZIP Folder (Canvas Export)":
            uploaded_zip = st.file_uploader(
                "Choose ZIP file",
                type=["zip"],
                help="Upload a ZIP folder containing all student submissions (e.g., Canvas export)."
            )
            if uploaded_zip:
                try:
                    zip_bytes = uploaded_zip.getvalue()
                    extracted = extract_files_from_zip(zip_bytes)
                    uploaded_files = [(fname, fbytes) for fname, fbytes, _ in extracted]
                    st.success(f"✅ Extracted {len(uploaded_files)} files from ZIP")
                except Exception as e:
                    st.error(f"⚠️ Error extracting ZIP: {e}")

        # ═══ PROCESS UPLOADED FILES ═══
        if uploaded_files:
            try:
                with st.spinner(f"Processing {len(uploaded_files)} file(s)..."):
                    
                    # Process files
                    if len(uploaded_files) == 1:
                        # Single file - traditional parsing
                        filename, file_bytes = uploaded_files[0]
                        raw_text, file_type = process_file_by_type(file_bytes, filename)
                        
                        if raw_text.startswith("⚠️"):
                            st.error(raw_text)
                            st.session_state.students = []
                        else:
                            students, error, pattern = parse_students(raw_text, filename)
                            
                            if error:
                                st.error(f"⚠️ {error}")
                                st.session_state.students = []
                                st.session_state.parse_error = error
                            else:
                                st.session_state.students = students
                                st.session_state.parse_error = None
                                st.session_state.pattern_used = pattern
                                
                                st.success(
                                    f"✅ **Found {len(students)} student{'s' if len(students) != 1 else ''}** "
                                    f"(detected via `{pattern}` pattern)"
                                )
                                st.markdown(
                                    "**Students found:** " + " · ".join(s.name for s in students)
                                )
                    
                    else:
                        # Multiple files - try two approaches
                        st.info(f"📊 Processing {len(uploaded_files)} files...")
                        
                        # Approach 1: Try to find students in combined text
                        combined_text, file_stats = process_multiple_files(uploaded_files)
                        students, error, pattern = parse_students(combined_text, "multiple_files")
                        
                        # Approach 2: If no students found, treat each file as one student
                        if error or len(students) == 0:
                            st.warning("⚠️ Could not find 'Student: [Name]' headers. Treating each file as one student submission...")
                            students = []
                            for filename, file_bytes in uploaded_files:
                                text, file_type = process_file_by_type(file_bytes, filename)
                                if not text.startswith("⚠️") and len(text.strip()) > 10:
                                    submission = create_submission_from_file(filename, text, file_type)
                                    students.append(submission)
                        
                        # Show results
                        if students:
                            st.session_state.students = students
                            st.session_state.parse_error = None
                            st.session_state.pattern_used = pattern or "filename"
                            
                            # Show file stats
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("📁 Files Processed", file_stats['total'])
                            with col2:
                                st.metric("👥 Students Found", len(students))
                            with col3:
                                errors = file_stats.get('errors', 0)
                                st.metric("⚠️ Errors", errors)
                            
                            # Show file types
                            file_types_str = " · ".join([
                                f"{ftype.upper()}: {count}" 
                                for ftype, count in file_stats.items() 
                                if ftype not in ['total', 'errors', 'unknown'] and count > 0
                            ])
                            if file_types_str:
                                st.success(f"✅ **File types processed:** {file_types_str}")
                            
                            st.markdown(
                                "**Students found:** " + " · ".join(s.name for s in students)
                            )
                        else:
                            st.error("⚠️ No valid student submissions found in uploaded files.")
                            st.session_state.students = []
                
            except Exception as e:
                st.error(f"⚠️ Error processing files: {e}")
                st.session_state.students = []

        # Navigation
        st.divider()
        c1, c2 = st.columns([1, 1])
        with c1:
            if st.button("← Back to Category Selection"):
                go_to_step(0)
                st.session_state.category = None
                st.rerun()
        with c2:
            if st.button(
                "Review & Confirm →",
                disabled=len(st.session_state.students) == 0,
                type="primary",
                use_container_width=True,
            ):
                go_to_step(2)
                st.rerun()


    # ═══ STEP 2: REVIEW & CONFIRM ════════════════════════════════════

    elif st.session_state.step == 2:
        cat_key = st.session_state.category
        T = TEMPLATES[cat_key]
        students = st.session_state.students

        st.markdown("## Review & Confirm")
        st.markdown(
            "Verify the parsed submissions below. "
            "Toggle students on/off to include/exclude from feedback generation."
        )

        if st.session_state.assignment_ctx:
            with st.expander("✅ Assignment Context Provided", expanded=False):
                st.markdown(st.session_state.assignment_ctx[:500] + ("..." if len(st.session_state.assignment_ctx) > 500 else ""))

        st.markdown(f"### {T['icon']} {len(students)} Students")

        selected_names = []
        for i, s in enumerate(students):
            col1, col2, col3 = st.columns([0.5, 4, 1.5])
            with col1:
                checked = st.checkbox("", value=True, key=f"stu_{i}", label_visibility="collapsed")
            with col2:
                st.markdown(f"**{s.name}**")
                st.caption(f"{s.word_count} words · {s.char_count:,} characters")
            with col3:
                with st.expander("Preview", expanded=False):
                    st.text(s.text[:1500] + ("\n\n[…truncated]" if len(s.text) > 1500 else ""))
            if checked:
                selected_names.append(s.name)

        selected = [s for s in students if s.name in selected_names]

        st.divider()
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Students Selected", f"{len(selected)} of {len(students)}")
        with c2:
            api_calls = len(selected) + 1
            st.metric("Estimated API Calls", api_calls)

        st.info("📄 **Output:** Part A (Individual) + Part B (Collective)")

        if not api_key:
            st.warning("⚠️ Please enter your Anthropic API key in the sidebar before generating feedback.")

        st.divider()
        c1, _, c3 = st.columns([1, 2, 1])
        with c1:
            if st.button("← Back"):
                go_to_step(1)
                st.rerun()
        with c3:
            if st.button(
                "🚀 Generate Feedback",
                disabled=len(selected) == 0 or not api_key,
                type="primary",
                use_container_width=True,
            ):
                st.session_state.selected_students = selected
                go_to_step(3)
                st.rerun()


    # ═══ STEP 3: GENERATE FEEDBACK ═══════════════════════════════════

    elif st.session_state.step == 3:
        cat_key = st.session_state.category
        T = TEMPLATES[cat_key]
        selected = getattr(st.session_state, "selected_students", st.session_state.students)
        ctx = st.session_state.assignment_ctx

        st.markdown(f"## {T['icon']} Generating Feedback")

        total_steps = len(selected) + 1
        progress_bar = st.progress(0)
        status_text = st.empty()

        part_a_results = []
        part_b_text = ""

        try:
            # Part A: Individual feedback
            st.markdown("### Part A: Individual Feedback")
            for i, student in enumerate(selected):
                status_text.markdown(f"🔄 Analyzing **{student.name}**'s submission... ({i+1}/{len(selected)})")
                progress_bar.progress((i + 1) / total_steps)

                prompt = T["build_part_a"](student.name, student.text, ctx)
                feedback = call_anthropic(T["system_prompt"], prompt, api_key)
                part_a_results.append({"name": student.name, "feedback": feedback})

                with st.expander(f"✅ {student.name}", expanded=False):
                    st.markdown(feedback)

            # Part B: Collective synthesis
            status_text.markdown("🔄 Crafting **collective synthesis**...")
            progress_bar.progress(1.0)

            summaries = "\n\n---\n\n".join(
                f"[{s.name}]:\n{s.text[:900]}{'…' if len(s.text) > 900 else ''}"
                for s in selected
            )
            prompt_b = T["build_part_b"](summaries, ctx)
            part_b_text = call_anthropic(T["system_prompt"], prompt_b, api_key)

            st.markdown(f"### {T['part_b_label']}")
            with st.expander("✅ Collective Synthesis", expanded=False):
                st.markdown(part_b_text)

            # Generate document
            status_text.markdown("📄 Assembling Word document...")
            doc_bytes = generate_feedback_docx(
                category_label=T["label"],
                part_a_label=T.get("part_a_label"),
                part_b_label=T["part_b_label"],
                has_part_a=T["has_part_a"],
                part_a_results=part_a_results,
                part_b_text=part_b_text,
            )

            st.session_state.part_a_results = part_a_results
            st.session_state.part_b_result = part_b_text
            st.session_state.doc_bytes = doc_bytes
            st.session_state.generation_error = None

            status_text.markdown("✅ **Feedback generation complete!**")
            go_to_step(4)
            st.rerun()

        except anthropic.AuthenticationError:
            st.error("🔑 **Authentication Error**: Invalid API key. Please check the sidebar.")
            if st.button("← Back to Review"):
                go_to_step(2)
                st.rerun()

        except anthropic.RateLimitError:
            st.error("⏳ **Rate Limit**: Too many requests. Please wait and try again.")
            if st.button("🔄 Retry"):
                st.rerun()
            if st.button("← Back to Review"):
                go_to_step(2)
                st.rerun()

        except Exception as e:
            st.error(f"⚠️ **Error**: {e}")
            if st.button("← Back to Review"):
                go_to_step(2)
                st.rerun()


    # ═══ STEP 4: RESULTS & DOWNLOAD ══════════════════════════════════

    elif st.session_state.step == 4:
        cat_key = st.session_state.category
        T = TEMPLATES[cat_key]

        st.markdown("""
        <div class="success-banner">
            <div style="font-size:48px;margin-bottom:4px;">✅</div>
            <h2 style="color:#15803d !important;margin:0 0 4px;">Feedback Ready</h2>
        </div>
        """, unsafe_allow_html=True)

        count_msg = f"{len(st.session_state.part_a_results)} individual reports + collective synthesis generated"
        st.markdown(f"<p style='text-align:center;color:#666;'>{count_msg}</p>", unsafe_allow_html=True)

        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"Feedback_{cat_key}_{date_str}.docx"

        _, center_col, _ = st.columns([1, 2, 1])
        with center_col:
            st.download_button(
                label="📥 Download .docx File",
                data=st.session_state.doc_bytes,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                type="primary",
                use_container_width=True,
            )

        # Tip about chat
        st.info(
            "💬 **Tip:** Switch to the **Chat with Agent** tab to ask follow-up questions "
            "about the generated feedback, individual student submissions, patterns you "
            "noticed, or get help refining specific feedback sections."
        )

        st.divider()

        if st.session_state.part_a_results:
            st.markdown("### Part A — Individual Feedback")
            for r in st.session_state.part_a_results:
                with st.expander(f"📋 {r['name']}"):
                    st.markdown(r["feedback"])

        if st.session_state.part_b_result:
            label = f"Part B — {T['part_b_label']}"
            st.markdown(f"### {label}")
            with st.expander("📖 View Full Synthesis", expanded=True):
                st.markdown(st.session_state.part_b_result)

        st.divider()
        c1, c2, c3 = st.columns([1, 1, 1])
        with c1:
            st.download_button(
                label="📥 Download Again",
                data=st.session_state.doc_bytes,
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True,
            )
        with c3:
            if st.button("🔄 Start New Session", use_container_width=True):
                reset_state()
                st.rerun()


# ═══════════════════════════════════════════════════════════════════════
# TAB 2: CHAT WITH AGENT
# ═══════════════════════════════════════════════════════════════════════

with tab_chat:

    st.markdown("## 💬 Chat with the Feedback Agent")

    # ─── Context Awareness Indicator ──────────────────────────────

    has_context = bool(
        st.session_state.category
        or st.session_state.students
        or st.session_state.part_a_results
    )

    if has_context:
        context_parts = []
        if st.session_state.category and st.session_state.category in TEMPLATES:
            T = TEMPLATES[st.session_state.category]
            context_parts.append(f"**Assignment type:** {T['icon']} {T['label']}")
        if st.session_state.students:
            names = [s.name for s in st.session_state.students[:10]]
            context_parts.append(f"**Students loaded:** {', '.join(names)}" + (f" (+{len(st.session_state.students)-10} more)" if len(st.session_state.students) > 10 else ""))
        if st.session_state.part_a_results:
            context_parts.append(f"**Feedback generated:** {len(st.session_state.part_a_results)} individual reports + collective synthesis")
        if st.session_state.assignment_ctx:
            context_parts.append("**Assignment context/rubric:** Loaded ✅")

        st.markdown(
            '<div class="chat-context-box">'
            '🧠 <strong>Context-Aware Mode</strong> — The agent has access to your current session:<br>'
            + "<br>".join(context_parts)
            + '</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="chat-context-box">'
            '💡 <strong>General Mode</strong> — No feedback session is active. '
            'The agent can help with assignment design, grading strategies, pedagogy, '
            'and general questions. Load student submissions in the Feedback Generator '
            'tab to enable context-aware conversations about specific students.'
            '</div>',
            unsafe_allow_html=True,
        )

    # ─── Suggested Questions ──────────────────────────────────────

    if not st.session_state.chat_messages:
        st.markdown("#### Get started with a question:")

        if has_context and st.session_state.part_a_results:
            suggestions = [
                "What common patterns do you see across all student submissions?",
                "Which students showed the strongest critical thinking and why?",
                "Can you suggest how I might adjust the feedback for students who struggled?",
                "What themes should I emphasize in next week's lecture based on these submissions?",
                "Help me draft an announcement to the class summarizing key takeaways.",
                "Are there any students whose submissions suggest they might need extra support?",
            ]
        elif has_context and st.session_state.students:
            suggestions = [
                "Give me a quick overview of the submission quality before I generate feedback.",
                "What should I look for in these submissions based on the assignment rubric?",
                "Are there any red flags I should be aware of in the uploaded submissions?",
            ]
        else:
            suggestions = [
                "How can I design a rubric that encourages deeper student reflection?",
                "What are best practices for giving constructive criticism to students?",
                "Help me write an assignment prompt for a discussion on AI ethics.",
                "What's the difference between formative and summative feedback?",
            ]

        cols = st.columns(2)
        for i, suggestion in enumerate(suggestions):
            col = cols[i % 2]
            with col:
                if st.button(f"💡 {suggestion}", key=f"suggest_{i}", use_container_width=True):
                    st.session_state.chat_messages.append({"role": "user", "content": suggestion})
                    st.rerun()

    # ─── Chat Message Display ─────────────────────────────────────

    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"], avatar="👤" if msg["role"] == "user" else "🤖"):
            st.markdown(msg["content"])

    # ─── Chat Input ───────────────────────────────────────────────

    if prompt := st.chat_input(
        "Ask about student feedback, assignment design, grading, or anything educational...",
        disabled=not api_key,
    ):
        # Add user message
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Thinking..."):
                try:
                    system_prompt = build_chat_system_prompt()

                    # Build message history for API (last 20 messages to manage token window)
                    api_messages = [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.chat_messages[-20:]
                    ]

                    response = call_anthropic_chat(system_prompt, api_messages, api_key)

                    st.markdown(response)
                    st.session_state.chat_messages.append({"role": "assistant", "content": response})

                except anthropic.AuthenticationError:
                    st.error("🔑 Invalid API key. Please check the sidebar.")
                except anthropic.RateLimitError:
                    st.error("⏳ Rate limited. Please wait a moment and try again.")
                except Exception as e:
                    st.error(f"⚠️ Error: {e}")

    if not api_key:
        st.warning("⚠️ Enter your Anthropic API key in the sidebar to start chatting.")
