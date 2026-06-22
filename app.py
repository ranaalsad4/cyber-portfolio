import streamlit as st

st.set_page_config(
    page_title="Alaa Al Saad | Cybersecurity Portfolio",
    page_icon="🛡️",
    layout="wide"
)

# ---------- DESIGN ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #050b16, #0b1f33, #101820);
    color: white;
}

h1, h2, h3 {
    color: #00e5ff;
}

.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid rgba(0, 229, 255, 0.35);
    box-shadow: 0 0 20px rgba(0, 229, 255, 0.12);
    margin-bottom: 20px;
}

.section-title {
    color: #00e5ff;
    font-size: 32px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)




st.markdown("""
<style>

/* Radio button labels */
div[role="radiogroup"] label {
    color: white !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* Project selector text */
label[data-baseweb="radio"] {
    color: white !important;
}

/* General text */
p, li {
    color: #EAEAEA !important;
}

/* Headings */
h1, h2, h3, h4 {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
div.stDownloadButton > button {
    background: linear-gradient(135deg, #00e5ff, #7b2cff) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    padding: 12px 20px !important;
}

div.stDownloadButton > button:hover {
    color: white !important;
    border: 1px solid #00e5ff !important;
    box-shadow: 0 0 15px rgba(0,229,255,0.45) !important;
}
</style>
""", unsafe_allow_html=True)




























# ---------- TOP NAVIGATION ----------
st.markdown("""
<style>
.nav-container {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(0,229,255,0.25);
    border-radius: 18px;
    padding: 14px;
    margin-bottom: 25px;
    text-align: center;
}
.hero {
    background: linear-gradient(135deg, rgba(0,229,255,0.16), rgba(123,44,255,0.14));
    border: 1px solid rgba(0,229,255,0.35);
    border-radius: 26px;
    padding: 38px;
    margin-bottom: 25px;
    box-shadow: 0 0 25px rgba(0,229,255,0.14);
}
.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: white;
}
.hero-subtitle {
    font-size: 22px;
    color: #00e5ff;
    font-weight: 600;
}
.project-card {
    background: rgba(255,255,255,0.075);
    border: 1px solid rgba(0,229,255,0.28);
    border-radius: 22px;
    padding: 24px;
    height: 100%;
    box-shadow: 0 0 18px rgba(0,229,255,0.10);
}
.project-icon {
    font-size: 46px;
    margin-bottom: 8px;
}
.project-title {
    color: #00e5ff;
    font-size: 22px;
    font-weight: 800;
}
.project-desc {
    color: #eaeaea;
    font-size: 15px;
}
.metric {
    background: rgba(0,229,255,0.08);
    border: 1px solid rgba(0,229,255,0.25);
    border-radius: 18px;
    padding: 18px;
    text-align: center;
}
.metric-num {
    font-size: 34px;
    font-weight: 800;
    color: #00e5ff;
}
.metric-label {
    color: #eaeaea;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

page = st.radio(
    "",
    [
        "Home",
        "About Me",
        "Cyber Forensics",
        "IT Auditing",
        "Vulnerability Analysis",
        "MIS Project",
        "Skills",
        "Certifications",
        "Contact"
    ],
    horizontal=True,
    label_visibility="collapsed"
)











# ---------- HOME ----------
if page == "Home":

    import os

    resume_file = "Alaa Al Saad_Cyber Forensics & Security_Resume.pdf"
    banner_path = "Projects/Cyber Forensics/images/cyber_banner.jpg"

    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.markdown("""
<div class="hero">
    <div class="hero-title">Alaa Al Saad</div>
    <div class="hero-subtitle">
    Cyber Forensics • Penetration Testing • IT Auditing • Vulnerability Analysis
    </div>
    <br>
    <p>
    A cybersecurity portfolio showcasing practical work in digital forensics,
    penetration testing, vulnerability analysis, IT auditing, risk assessment,
    and security governance.
    </p>
    <p>
    This platform brings together my technical projects, investigation reports,
    security tools, certifications, and professional background in one place.
    </p>
</div>
""", unsafe_allow_html=True)

    with col2:
        if os.path.exists(banner_path):
            st.image(banner_path, use_container_width=True)
        else:
            st.info("Cyber banner image not found.")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="metric"><div class="metric-num">10+</div><div class="metric-label">Cybersecurity Projects</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric"><div class="metric-num">4+</div><div class="metric-label">Certifications</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric"><div class="metric-num">3.9</div><div class="metric-label">Master GPA</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric"><div class="metric-num">90%</div><div class="metric-label">Security Improvement</div></div>', unsafe_allow_html=True)

    st.markdown("## Explore the Portfolio")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
<div class="project-card">
    <div class="project-icon">🕵️</div>
    <div class="project-title">Cyber Forensics</div>
    <p class="project-desc">
    Digital evidence analysis, forensic image verification, hash validation,
    fraud investigation, and mobile evidence review.
    </p>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="project-card">
    <div class="project-icon">📋</div>
    <div class="project-title">IT Auditing</div>
    <p class="project-desc">
    IT control review, general computer controls, risk assessment,
    governance analysis, disaster recovery, and business continuity.
    </p>
</div>
""", unsafe_allow_html=True)

    with col3:
        st.markdown("""
<div class="project-card">
    <div class="project-icon">🔍</div>
    <div class="project-title">Vulnerability Analysis</div>
    <p class="project-desc">
    Penetration testing, OSINT, active reconnaissance, password cracking,
    phishing simulation, and vulnerability remediation.
    </p>
</div>
""", unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
<div class="project-card">
    <div class="project-icon">💻</div>
    <div class="project-title">MIS Security Project</div>
    <p class="project-desc">
    Academic security project covering Nmap scanning, John the Ripper,
    SQL injection testing, and ethical hacking practices.
    </p>
</div>
""", unsafe_allow_html=True)

    with col5:
        st.markdown("""
<div class="project-card">
    <div class="project-icon">🛠️</div>
    <div class="project-title">Technical Skills</div>
    <p class="project-desc">
    Tools and skills across forensics, penetration testing,
    risk management, security frameworks, and technical reporting.
    </p>
</div>
""", unsafe_allow_html=True)

    with col6:
        st.markdown("""
<div class="project-card">
    <div class="project-icon">🏆</div>
    <div class="project-title">Certifications</div>
    <p class="project-desc">
    Security+, eJPT, eCIR, CyberDefense, incident response training,
    professional memberships, and continuous learning.
    </p>
</div>
""", unsafe_allow_html=True)

    st.markdown("## Resume")

    if os.path.exists(resume_file):
        with open(resume_file, "rb") as file:
            st.download_button(
                label="⬇️ Download Resume",
                data=file,
                file_name=resume_file,
                mime="application/pdf"
            )
    else:
        st.info("Place your resume PDF in the same folder as app.py.")


















# ---------- ABOUT ME ----------
if page == "About Me":

    import os

    st.title("👋 About Me")
    st.subheader("Cyber Forensics & Security Professional")

    resume_file = "Alaa Al Saad_Cyber Forensics & Security_Resume.pdf"

    st.markdown("""
<style>
.hero-card {
    background: linear-gradient(135deg, rgba(0,229,255,0.16), rgba(123,44,255,0.12));
    border: 1px solid rgba(0,229,255,0.35);
    border-radius: 24px;
    padding: 32px;
    box-shadow: 0 0 25px rgba(0,229,255,0.18);
    margin-bottom: 25px;
}
.metric-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(0,229,255,0.25);
    border-radius: 18px;
    padding: 22px;
    text-align: center;
}
.metric-number {
    color: #00e5ff;
    font-size: 36px;
    font-weight: 800;
}
.metric-label {
    color: #eaeaea;
    font-size: 14px;
}
.about-box {
    background: rgba(255,255,255,0.07);
    border-left: 4px solid #00e5ff;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 18px;
}
.tag {
    display: inline-block;
    background: linear-gradient(135deg,#00e5ff,#7b2cff);
    color: white;
    padding: 8px 14px;
    margin: 5px;
    border-radius: 20px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="hero-card">
<h1>Alaa Al Saad</h1>
<h3>Cyber Forensics & Security | Penetration Testing | IT Auditing | Risk Assessment</h3>

<p>
Cybersecurity professional specializing in cyber forensics, digital investigations, penetration testing, vulnerability management, IT auditing, and security risk assessment. Holds a Master of Cyber Forensics and Security from the Illinois Institute of Technology and combines advanced technical expertise with a strong understanding of security governance, compliance, and organizational risk.
</p>

<p>
Demonstrated ability to identify critical vulnerabilities, investigate security incidents, assess cyber risk, and transform complex technical findings into actionable security strategies. Experienced in conducting forensic examinations, security assessments, penetration tests, and audit engagements aligned with industry frameworks including ISO 27001 and the NIST Cybersecurity Framework.
</p>

</p>
Committed to strengthening organizational resilience through proactive risk management, evidence-based security analysis, and practical recommendations that enhance the confidentiality, integrity, and availability of critical information assets. 
</p>

</div>
""", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="metric-card"><div class="metric-number">3.9</div><div class="metric-label">Master GPA</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><div class="metric-number">10+</div><div class="metric-label">Cyber Projects</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><div class="metric-number">4+</div><div class="metric-label">Certifications</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><div class="metric-number">90%</div><div class="metric-label">Security Improvement</div></div>', unsafe_allow_html=True)

    st.markdown("## 🔍 Professional Focus")

    st.markdown("""
<div class="about-box">
I specialize in practical cybersecurity work that connects technical investigation with business risk.
My portfolio includes forensic image verification, fraud investigation, owl trafficking digital evidence analysis,
penetration testing, password cracking, phishing simulation, OSINT reconnaissance, IT audit analysis,
and formal risk assessment.
</div>
""", unsafe_allow_html=True)

    st.markdown("## 🛡️ Core Strengths")

    st.markdown("""
<span class="tag">Digital Forensics</span>
<span class="tag">Penetration Testing</span>
<span class="tag">Vulnerability Assessment</span>
<span class="tag">IT Auditing</span>
<span class="tag">Risk Assessment</span>
<span class="tag">Incident Response</span>
<span class="tag">NIST CSF</span>
<span class="tag">ISO 27001</span>
<span class="tag">Security Reporting</span>
""", unsafe_allow_html=True)

    st.markdown("## 🎓 Education & Credentials")

    st.markdown("""
<div class="about-box">
<b>Master of Cyber Forensics and Security</b><br>
Illinois Institute of Technology, Chicago, USA | GPA: 3.9/4.0
<br><br>
<b>Bachelor of Science in Computer Science</b><br>
Imam Abdulrahman Bin Faisal University, Saudi Arabia | GPA: 4.3/5.0
<br><br>
<b>Certifications:</b> CompTIA Security+, eJPT, eCIR, TestOut CyberDefense
</div>
""", unsafe_allow_html=True)

    st.markdown("## 📄 Resume")

    if os.path.exists(resume_file):
        with open(resume_file, "rb") as file:
            st.download_button(
                label="⬇️ Download Resume",
                data=file,
                file_name=resume_file,
                mime="application/pdf"
            )
    else:
        st.warning("Resume file not found. Place your resume PDF in the same folder as app.py.")

    st.markdown("## 📬 Contact")

    st.markdown("""
<div class="about-box">
📍 Saudi Arabia<br>
📞 +966 530661057<br>
📧 <a href="mailto:aalsaad.alaa@gmail.com">aalsaad.alaa@gmail.com</a><br>
💼 <a href="https://linkedin.com/in/alaa-alsad" target="_blank">linkedin.com/in/alaa-alsad</a>
</div>
""", unsafe_allow_html=True)



















  # ---------- CYBER FORENSICS ----------
elif page == "Cyber Forensics":

    import os

    st.title("🕵️ Cyber Forensics Projects")
    st.subheader("Digital Evidence • Investigation • Integrity Verification")

    base_path = "Projects/Cyber Forensics"
    image_path = "Projects/Cyber Forensics/images"

    selected_project = st.radio(
        "Select a project",
        [
            "Forensic Image Verification",
            "Owl Trafficking Investigation",
            "Financial Fraud Investigation"
        ],
        horizontal=True
    )

    def download_report(file_name, label):
        report_path = os.path.join(base_path, file_name)

        try:
            with open(report_path, "rb") as file:
                st.download_button(
                    label=label,
                    data=file,
                    file_name=file_name,
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.warning(f"Report not found: {report_path}")

    def show_gallery(images):
        st.markdown("### 📸 Evidence Screenshots")

        for i in range(0, len(images), 2):
            col1, col2 = st.columns(2)

            with col1:
                img_file, caption = images[i]
                full_path = img_file
                if os.path.exists(full_path):
                    st.image(full_path, caption=caption, use_container_width=True)
                else:
                    st.warning(f"Image not found: {img_file}")

            if i + 1 < len(images):
                with col2:
                    img_file, caption = images[i + 1]
                    full_path = os.path.join(image_path, img_file)
                    if os.path.exists(full_path):
                        st.image(full_path, caption=caption, use_container_width=True)
                    else:
                        st.warning(f"Image not found: {img_file}")

    if selected_project == "Forensic Image Verification":

        st.markdown("## 01 | Forensic Image Verification Using MD5 and SHA-1")

        st.markdown("""
### 🔍 Investigation Overview

Digital evidence must remain unchanged throughout an investigation. In this project, I created a forensic image of a disk image and verified that the acquired copy was an exact bit-by-bit duplicate of the original evidence.

To ensure evidence integrity, I generated MD5 and SHA-1 hash values for both the original image and the forensic copy. The matching hash values confirmed that no modifications occurred during acquisition or analysis.

### 🛠 Tools & Techniques

- Command Prompt & CertUtil
- WinHex
- FTK Imager
- MD5 Hash Verification
- SHA-1 Hash Verification
- Forensic Imaging

### ⚡ Investigation Process

1. Acquired a forensic copy of the original disk image.
2. Generated MD5 and SHA-1 hashes for the source evidence.
3. Created a forensic image using WinHex.
4. Verified image integrity using WinHex hash verification.
5. Performed independent verification using FTK Imager.
6. Compared all hash values to confirm evidence authenticity.

### 🎯 Outcome

The forensic image was successfully validated as an exact duplicate of the original evidence. The matching hash values demonstrated evidence integrity and forensic soundness, ensuring the image could be used for further analysis without altering the original source.
""")

        forensic_images = [
            ("Image_01.png", "Figure 1: MD5 hash calculation using Command Prompt"),
            ("Image_02.png", "Figure 2: SHA-1 hash calculation using Command Prompt"),
            ("Image_03.png", "Figure 3: hashes.txt file showing MD5 and SHA-1 values"),
            ("Image_04.png", "Figure 4: WinHex forensic copy / cloning log"),
            ("Image_05.png", "Figure 5: MD5 verification using WinHex"),
            ("Image_06.png", "Figure 6: SHA-1 verification using WinHex"),
            ("Image_07.png", "Figure 7: MD5 and SHA-1 verification using FTK Imager"),
            ("Image_08.png", "Figure 8: Final project folder contents")
        ]

        show_gallery(forensic_images)

        st.markdown("### 📄 Full Report")
        download_report(
            "Forensic_Image_Verification_MD5_SHA1.pdf",
            "Download Forensic Image Verification Report"
        )

    elif selected_project == "Owl Trafficking Investigation":

        st.markdown("## 02 | Endangered Owl Trafficking Investigation")

        st.markdown("""
### 🦉 Case Overview

This investigation focused on a simulated wildlife trafficking case involving the illegal sale and transportation of endangered owls.

The objective was to examine digital evidence recovered from a suspect device and identify communication records, delivery details, and individuals involved in the trafficking operation.

### 🛠 Tools & Techniques

- Autopsy
- FQLite
- SQLite Database Analysis
- Digital Evidence Tagging
- Mobile Device Forensics

### ⚡ Investigation Process

1. Examined forensic images using Autopsy.
2. Analyzed SMS records stored in the mmssms.db database.
3. Identified messages discussing owl delivery arrangements.
4. Recovered delivery date and time information.
5. Investigated contact databases to identify associated individuals.
6. Tagged, extracted, and documented relevant evidence.

### 🔎 Key Findings

- Recovered communications discussing owl delivery.
- Identified the scheduled delivery timeframe.
- Located information related to the second suspect.
- Recovered account and contact information associated with the investigation.
- Generated a complete forensic report documenting evidence and findings.

### 🎯 Outcome

The investigation successfully reconstructed communication activities, identified key individuals, and established a digital evidence trail linking participants to the suspected trafficking operation.
""")

        owl_images = [
            ("owl_01.png", "Figure 1: Autopsy case details"),
            ("owl_02.png", "Figure 2: Relevant images identified in Autopsy"),
            ("owl_03.png", "Figure 3: Tag creation for owl-related evidence"),
            ("owl_04.png", "Figure 4: SMS records in mmssms.db"),
            ("owl_05.png", "Figure 5: Contact information from database records"),
            ("owl_06.png", "Figure 6: Extracted evidence files"),
            ("owl_07.png", "Figure 7: HTML report generation"),
            ("owl_08.png", "Figure 8: Final report/evidence view")
        ]

        show_gallery(owl_images)

        st.markdown("### 📄 Full Report")
        download_report(
            "Digital_Forensics_Owl_Trafficking_Investigation.pdf",
            "Download Owl Trafficking Investigation Report"
        )

    elif selected_project == "Financial Fraud Investigation":

        st.markdown("## 03 | Financial Fraud Forensic Investigation")

        st.markdown("""
### 💰 Case Overview

This project involved a forensic investigation into a suspected financial fraud scheme. The objective was to recover hidden account information concealed within a forensic image of a USB storage device.

The investigation followed a series of clues left by the suspect, including partition references, sector addresses, and encoded color values.

### 🛠 Tools & Techniques

- WinHex
- Autopsy
- File Signature Analysis
- RGB Color Mapping
- Digital Evidence Recovery
- Hidden Data Analysis

### ⚡ Investigation Process

1. Examined the forensic USB image using WinHex.
2. Located hidden partition references from investigative clues.
3. Extracted RGB color values from partition sectors.
4. Converted color values into meaningful file identifiers.
5. Used Autopsy to locate hidden files matching recovered clues.
6. Repaired damaged file signatures to recover inaccessible evidence.
7. Distinguished valid evidence from intentionally misleading artifacts.

### 🔎 Key Findings

- Identified hidden partitions containing investigative clues.
- Decoded RGB values that led to concealed files.
- Recovered a hidden PDF containing eight account numbers.
- Repaired corrupted file headers to restore access.
- Documented a false lead involving a hidden IP address image.

### 🎯 Outcome

The investigation successfully recovered critical financial evidence hidden within the storage device and demonstrated advanced forensic recovery techniques used to uncover intentionally concealed information.
""")

        fraud_images = [
            ("fraud_01.png", "Figure 1: Forensic raw copy opened in WinHex"),
            ("fraud_02.png", "Figure 2: Forensic raw copy examined in Autopsy"),
            ("fraud_03.png", "Figure 3: Suspect note with investigation clues"),
            ("fraud_04.png", "Figure 4: RGB color code found on Partition 14"),
            ("fraud_05.png", "Figure 5: Crimson color identified using web tool"),
            ("fraud_06.png", "Figure 6: Crimson file located in Autopsy"),
            ("fraud_07.png", "Figure 7: Recovered account numbers from Crimson file"),
            ("fraud_08.png", "Figure 8: RGB color code found on Partition 12"),
            ("fraud_09.png", "Figure 9: Goldenrod color clue identified"),
            ("fraud_10.png", "Figure 10: Goldenrod file found in Autopsy"),
        ]

        show_gallery(fraud_images)

        st.markdown("### 📄 Full Report")
        download_report(
            "Financial_Fraud_Forensic_Investigation_Case_Study.pdf",
            "Download Financial Fraud Investigation Report"
        )










# ---------- IT AUDITING ----------
elif page == "IT Auditing":

    import os

    st.title("📋 Information Technology Auditing Projects")
    st.subheader("Governance • Risk Assessment • Controls • Business Continuity")

    base_path = "Projects/Information Technology Auditing"
    image_path = "Projects/Information Technology Auditing/images"

    selected_audit_project = st.radio(
        "Select an IT Auditing project",
        [
            "Anthem General Computer Controls Audit",
            "Arthur Andersen Ethics & COBIT Case Study",
            "Banner Finance Risk Assessment",
            "Disaster Recovery & Business Continuity Audit"
        ],
        horizontal=True
    )

    def download_audit_report(file_name, label):
        report_path = os.path.join(base_path, file_name)
        try:
            with open(report_path, "rb") as file:
                st.download_button(
                    label=label,
                    data=file,
                    file_name=file_name
                )
        except FileNotFoundError:
            st.warning(f"Report not found: {report_path}")

    def show_audit_gallery(images):

        for i in range(0, len(images), 2):
            col1, col2 = st.columns(2)

            with col1:
                img_file, caption = images[i]
                full_path = img_file
                if os.path.exists(full_path):
                    st.image(full_path, caption=caption, use_container_width=True)

            if i + 1 < len(images):
                with col2:
                    img_file, caption = images[i + 1]
                    full_path = os.path.join(image_path, img_file)
                    if os.path.exists(full_path):
                        st.image(full_path, caption=caption, use_container_width=True)

    if selected_audit_project == "Anthem General Computer Controls Audit":

        st.markdown("## 01 | General Computer Controls Audit at Anthem")

        st.markdown("""
### 🔍 Project Overview

This project evaluated Anthem’s information security environment through a General Computer Controls audit. The audit focused on whether key IT controls supported confidentiality, integrity, availability, risk management, secure operations, and protection of sensitive healthcare information.

The project reviewed major information security findings, including data breach exposure, phishing attacks, access termination weaknesses, physical security gaps, private data protection issues, system configuration risks, and unauthorized access concerns.

### 🛠 Frameworks & Control Areas

- General Computer Controls
- NIST Cybersecurity Framework
- CIS Controls
- COSO Enterprise Risk Management
- SOC 2 Security and Availability Criteria
- PCI DSS concepts
- HIPAA-related privacy and security concerns

### ⚡ Audit Work Performed

1. Reviewed Anthem’s information security risk exposure.
2. Identified seven key information security findings.
3. Mapped each finding to relevant standards and control expectations.
4. Analyzed root causes behind each control weakness.
5. Evaluated business impact, including data breach, financial loss, regulatory exposure, and reputational damage.
6. Developed practical recommendations to strengthen security controls.

### 🔎 Key Findings

- Data breach exposure due to weak protection of sensitive healthcare information.
- Phishing risk caused by limited security awareness and email protection controls.
- Delays in removing terminated user access.
- Physical security weaknesses around access points and monitoring.
- Weak access controls protecting private data.
- Configuration management risks caused by inconsistent change approval and documentation.
- Network security concerns related to unauthorized access and data misuse.

### 🎯 Outcome

This audit demonstrated my ability to evaluate IT control environments, identify security weaknesses, connect findings to recognized frameworks, assess business impact, and recommend realistic remediation actions for a healthcare organization.
""")






    elif selected_audit_project == "Arthur Andersen Ethics & COBIT Case Study":

        st.markdown("## 02 | Arthur Andersen Ethics & COBIT Governance Case Study")

        st.markdown("""
### 🔍 Project Overview

This project analyzed the Arthur Andersen case through the lens of professional ethics, audit independence, integrity, due professional care, and governance accountability. It examined how ethical violations and conflicts of interest contributed to major audit failures and the collapse of trust in the firm.

The second part of the project proposed how COBIT governance objectives should evolve to address next-generation technologies such as artificial intelligence, digital platforms, cybersecurity risk, data privacy, and technology ethics.

### 🛠 Standards & Governance Areas

- AICPA Code of Professional Conduct
- ISACA Code of Professional Ethics
- COBIT Governance Objectives
- Audit independence and objectivity
- Conflict-of-interest analysis
- Emerging technology governance
- AI ethics and compliance monitoring

### ⚡ Analysis Performed

1. Reviewed Andersen’s conduct across major client cases.
2. Identified violations related to independence, integrity, conflict of interest, and due care.
3. Assessed how consulting pressure weakened audit objectivity.
4. Evaluated Andersen’s relationship with Enron, Waste Management, and DeLorean.
5. Proposed updates to COBIT objectives for AI, cybersecurity, privacy, and digital governance.
6. Connected historical audit failures to modern technology risk challenges.

### 🔎 Key Findings

- Andersen’s consulting and audit conflicts weakened professional independence.
- Integrity and due care failures contributed to serious audit breakdowns.
- Close client relationships increased ethical and legal exposure.
- COBIT objectives should include stronger controls for AI ethics, digital compliance, cybersecurity resilience, and continuous monitoring.

### 🎯 Outcome

This project demonstrated my ability to analyze audit ethics, interpret professional standards, evaluate governance failures, and connect traditional audit principles to emerging technology risks.
""")











    elif selected_audit_project == "Banner Finance Risk Assessment":

        st.markdown("## 03 | Banner Finance Risk Assessment")

        st.markdown("""
### 🔍 Project Overview

This project performed a structured risk assessment for a university Banner Finance application. The assessment focused on identifying threats, vulnerabilities, predisposing conditions, likelihood, impact, and overall risk levels affecting the confidentiality, integrity, and availability of the system.

The work followed a risk-based audit approach and organized risks across organizational, departmental, and information system levels.

### 🛠 Risk Assessment Areas

- NIST-style risk assessment methodology
- Threat source identification
- Threat event analysis
- Vulnerability identification
- Predisposing condition analysis
- Likelihood and impact determination
- Risk prioritization
- Audit universe planning

### ⚡ Assessment Performed

1. Defined the purpose and scope of the Banner Finance risk assessment.
2. Identified adversarial and non-adversarial threat sources.
3. Evaluated vulnerabilities such as weak password configuration, poor access review, delayed account termination, and local backup storage.
4. Assessed likelihood and impact across multiple risk scenarios.
5. Classified risks by severity level.
6. Developed mitigation recommendations for university leadership.

### 🔎 Risk Summary

- Total risks identified: 8
- Very High risks: 2
- High risks: 2
- Moderate risks: 3
- Low risks: 1

### 🎯 Key Risks

- Weak password configuration increasing unauthorized access risk.
- Irregular user activity monitoring.
- Delayed removal of terminated user accounts.
- Local-only backup storage with no offsite recovery strategy.
- Employee error involving sensitive data.
- Poor application design and change control.
- Natural disaster exposure due to Florida location.
- Power outage risk affecting backup availability.

### 🎯 Outcome

This project demonstrated my ability to conduct a formal IT risk assessment, classify risks by severity, evaluate threat likelihood and business impact, and communicate practical recommendations to executive leadership.
""")












    elif selected_audit_project == "Disaster Recovery & Business Continuity Audit":

        st.markdown("## 04 | Disaster Recovery & Business Continuity Audit")

        st.markdown("""
### 🔍 Project Overview

This project assessed disaster recovery and business continuity practices for Florida University of Technology after the Hurricane Sandy disaster scenario. The project examined how IT audit teams evaluate institutional readiness, continuity planning, disaster response, communication procedures, and recovery practices.

The focus was on understanding how universities can maintain operations, protect critical systems, and reduce disruption during major disasters.

### 🛠 Audit Focus Areas

- Disaster Recovery Planning
- Business Continuity Planning
- IT Audit Recommendations
- NIST SP 800-34 concepts
- ISO 22301 concepts
- Offsite backup and system resilience
- Emergency communication
- Operational continuity

### ⚡ Audit Analysis Performed

1. Reviewed the university’s disaster recovery and continuity planning practices.
2. Examined the scale of Hurricane Sandy’s operational impact.
3. Identified lessons learned from the disaster scenario.
4. Evaluated communication practices for students, staff, and faculty.
5. Reviewed continuity actions such as shelter planning, online learning continuity, and offsite backup.
6. Developed recommendations for IT audit and leadership.

### 🔎 Key Lessons

- Disaster communication should reach all students, faculty, and staff through multiple channels.
- Universities need backup power and resilient infrastructure.
- Flood drainage and transportation planning are important for campus recovery.
- Offsite backup is essential to protect critical systems.
- Periodic testing and training improve disaster readiness.

### 🎯 Outcome

This project demonstrated my understanding of business continuity, disaster recovery, IT audit planning, and operational resilience. It also showed how audit recommendations can help organizations prepare for disruptive events and protect critical assets.
""")

        disaster_images = [
            ("audit_01.png", "Instructor feedback and presentation overview"),
            ("audit_02.png", "Presentation outline"),
            ("audit_03.png", "Florida University of Technology overview"),
            ("audit_04.png", "Hurricane Sandy disaster impact"),
            ("audit_05.png", "Lessons learned from disaster response"),
            ("audit_06.png", "Continuity and infrastructure lessons"),
            ("audit_07.png", "Disaster recovery and business continuity practices"),
            ("audit_08.png", "Conclusion and audit recommendation")
        ]

        show_audit_gallery(disaster_images)






















# ---------- VULNERABILITY ANALYSIS ----------
elif page == "Vulnerability Analysis":

    import os

    st.title("🔍 Vulnerability Analysis & Control")
    st.subheader("Penetration Testing • Reconnaissance • Password Security • Phishing Assessment")

    base_path = "Projects/Vulnerability Analysis and Control"
    image_path = "Projects/Vulnerability Analysis and Control/Image_VA"

    selected_project = st.radio(
        "Select a project",
        [
            "Acme Coffee Penetration Test",
            "OSINT & Active Reconnaissance Assessment",
            "Password Cracking & Hash Analysis",
            "Phishing Attack Simulation"
        ],
        horizontal=True
    )

    def download_report(file_name, label):
        report_path = os.path.join(base_path, file_name)

        try:
            with open(report_path, "rb") as file:
                st.download_button(
                    label=label,
                    data=file,
                    file_name=file_name
                )
        except FileNotFoundError:
            st.info(f"Place report here: {report_path}")

    # ==========================================================
    # PROJECT 1
    # ==========================================================

    if selected_project == "Acme Coffee Penetration Test":

        st.markdown("""
# ☕ Acme Coffee Company Penetration Test

### Project Overview

This project involved a full penetration test against the Acme Coffee Company environment to identify exploitable weaknesses in network services, authentication controls, password security, and privilege management.

The assessment followed a clear attack path: reconnaissance, service enumeration, vulnerability research, user discovery, credential attacks, remote access validation, password hash analysis, and privilege escalation.

### Tools Used

- Nmap
- CVE Database
- Enum4Linux
- Hydra
- Medusa
- SSH
- John the Ripper
- Linux Privilege Escalation Techniques

### Assessment Story

The engagement began with scanning the target system to understand its exposed services. Nmap identified multiple open ports, which created a starting point for deeper enumeration and vulnerability analysis.

After identifying service versions, I reviewed public vulnerability information to understand possible exploitation paths. I then used Enum4Linux to collect system and user account information. Once usernames were identified, controlled credential attacks were performed using Hydra and Medusa.

The assessment successfully validated remote access through SSH and demonstrated that weak credentials could allow unauthorized access. After gaining access, password hashes were collected and analyzed using John the Ripper. The final stage demonstrated privilege escalation to root-level access, showing the seriousness of the security exposure.

### Key Findings

- Seven open ports were exposed.
- Service versions could be identified by attackers.
- User account enumeration was possible.
- Weak credentials were discovered.
- SSH access was successfully validated.
- Password hashes were recoverable.
- Root-level access was obtained.

### Recommendations

- Close unnecessary ports and restrict exposed services.
- Harden SSH and FTP configurations.
- Enforce strong password policies.
- Enable account lockout and brute-force protection.
- Disable direct root access.
- Apply regular patching and service updates.
- Deploy intrusion detection and prevention controls.
- Conduct routine penetration testing and vulnerability reviews.

### Skills Demonstrated

- Penetration Testing
- Vulnerability Assessment
- Network Enumeration
- Credential Attacks
- Password Cracking
- Linux Security
- Privilege Escalation
- Security Reporting

### Project Outcome

This project demonstrated how an attacker could move from basic reconnaissance to full system compromise by chaining service exposure, weak credentials, and privilege escalation weaknesses.
""")

        st.markdown("### 📸 Evidence Screenshots")

        acme_images = [
            ("acme_1.png", "Figure 1: Nmap scan showing open ports"),
            ("acme_2.png", "Figure 2: Nmap service and version detection"),
            ("acme_3.png", "Figure 3: FTP vulnerability score review"),
            ("acme_4.png", "Figure 4: SSH vulnerability score review"),
            ("acme_5.png", "Figure 5: Enum4Linux user enumeration"),
            ("acme_6.png", "Figure 6: Hydra credential attack result"),
            ("acme_7.png", "Figure 7: Medusa credential attack result"),
            ("acme_8.png", "Figure 8: Successful SSH login"),
            ("acme_9.png", "Figure 9: John the Ripper password cracking results"),
            ("acme_10.png", "Figure 10: Root privilege escalation")
        ]

        for i in range(0, len(acme_images), 2):
            col1, col2 = st.columns(2)

            with col1:
                img_file, caption = acme_images[i]
                img_path = os.path.join(image_path, img_file)
                if os.path.exists(img_path):
                    st.image(img_path, caption=caption, use_container_width=True)
                else:
                    st.warning(f"Image not found: {img_path}")

            if i + 1 < len(acme_images):
                with col2:
                    img_file, caption = acme_images[i + 1]
                    img_path = os.path.join(image_path, img_file)
                    if os.path.exists(img_path):
                        st.image(img_path, caption=caption, use_container_width=True)
                    else:
                        st.warning(f"Image not found: {img_path}")

        download_report(
            "Acme_Coffee_Penetration_Test_Report.docx",
            "📄 Download Penetration Test Report"
        )
















    # ==========================================================
    # PROJECT 2
    # ==========================================================

    elif selected_project == "OSINT & Active Reconnaissance Assessment":

        st.markdown("""
# 🌐 Active Reconnaissance and OSINT Assessment

### Project Overview

This project assessed the public attack surface of **certifiedhacker.com** using passive and active reconnaissance techniques.

The goal was to understand what information an attacker could collect before launching an attack, including domain records, hosting details, technologies, exposed services, open ports, directories, and possible vulnerabilities.

### Tools Used

- Whois
- Nslookup
- Dig
- Host
- Netcraft
- Wappalyzer
- Shodan
- Nmap
- Ping
- DirBuster
- CVE / NIST vulnerability references

### Assessment Story

The assessment began with passive reconnaissance to collect publicly available information without directly interacting aggressively with the target. This included domain registration data, DNS records, hosting information, technology stack details, and publicly indexed exposure.

After that, active reconnaissance was performed using tools such as Nmap, Ping, and DirBuster to identify open services, reachable infrastructure, directories, and potential attack surface areas.

The final stage focused on vulnerability review, where exposed technologies such as OpenSSH and MySQL were compared against public vulnerability information to understand potential exploitation risk.

### Key Findings

- Public domain and registration information was discoverable.
- DNS and hosting details were exposed.
- Technology stack information was visible through public tools.
- Open services and ports were identified.
- Directory discovery revealed additional accessible paths.
- OpenSSH and MySQL vulnerability indicators were reviewed.
- The target had multiple attack surface entry points.

### Recommendations

- Reduce public information exposure where possible.
- Harden DNS and hosting configurations.
- Disable unnecessary services.
- Patch outdated technologies.
- Restrict exposed directories.
- Conduct regular vulnerability scanning.
- Monitor public exposure through OSINT tools.

### Skills Demonstrated

- Passive Reconnaissance
- Active Reconnaissance
- OSINT Collection
- DNS Analysis
- Attack Surface Mapping
- Vulnerability Research
- Security Reporting

### Project Outcome

This project demonstrated how attackers can combine public intelligence with active scanning to build a detailed profile of a target and identify possible exploitation paths.
""")

        st.markdown("### 📸 Evidence Screenshots")

        osint_images = [
            ("osint_1.png", "Figure 1: Whois reconnaissance result"),
            ("osint_2.png", "Figure 2: Nslookup result"),
            ("osint_3.png", "Figure 3: Dig command result"),
            ("osint_4.png", "Figure 4: Host command result"),
            ("osint_5.png", "Figure 5: Netcraft website intelligence"),
            ("osint_6.png", "Figure 6: Wappalyzer technology stack result"),
            ("osint_7.png", "Figure 7: Shodan exposure result"),
            ("osint_8.png", "Figure 8: Nmap active scan result"),
            ("osint_9.png", "Figure 9: Ping command result"),
            ("osint_10.png", "Figure 10: Additional ping / network response result"),
            ("osint_11.png", "Figure 11: DirBuster directory discovery result"),
            ("osint_12.png", "Figure 12: OpenSSH vulnerability score review"),
            ("osint_13.png", "Figure 13: MySQL vulnerability score review")
        ]

        for i in range(0, len(osint_images), 2):
            col1, col2 = st.columns(2)

            with col1:
                img_file, caption = osint_images[i]
                img_path = os.path.join(image_path, img_file)
                if os.path.exists(img_path):
                    st.image(img_path, caption=caption, use_container_width=True)
                else:
                    st.warning(f"Image not found: {img_path}")

            if i + 1 < len(osint_images):
                with col2:
                    img_file, caption = osint_images[i + 1]
                    img_path = os.path.join(image_path, img_file)
                    if os.path.exists(img_path):
                        st.image(img_path, caption=caption, use_container_width=True)
                    else:
                        st.warning(f"Image not found: {img_path}")

        download_report(
            "Active_Reconnaissance_and_OSINT_Assessment.docx",
            "📄 Download OSINT Assessment"
        )







    # ==========================================================
    # PROJECT 3
    # ==========================================================

    elif selected_project == "Password Cracking & Hash Analysis":

        st.markdown("""
# 🔐 Password Cracking & Hash Analysis

### Project Overview

This project focused on password security assessment through hash identification and controlled password cracking techniques.

The objective was to demonstrate how weak passwords can be recovered from hashes and why poor password practices create serious security risks.

### Tools Used

- Hashcat
- Hash Identifier
- John the Ripper
- Hashes.com
- RockYou wordlist
- NTLM hash analysis

### Assessment Story

The project began by identifying the hash type to understand which cracking method should be used. After confirming the likely hash algorithm, I used dictionary-based cracking techniques with Hashcat and John the Ripper.

The results showed that several passwords could be recovered successfully, including weak, reused, and predictable passwords. The exercise also identified an account with a blank password, which represents a critical security weakness.

### Passwords Recovered

- vagrant
- pr0t0c0l
- mandalorian1
- blank password identified

### Security Risks Identified

- Weak password selection
- Password reuse
- Predictable credentials
- Blank password configuration
- Lack of password complexity controls
- Exposure to offline cracking attacks

### Recommendations

- Enforce strong password policies.
- Require multi-factor authentication.
- Block blank passwords.
- Prevent password reuse.
- Monitor leaked credential exposure.
- Conduct periodic password audits.
- Use secure password storage and salting mechanisms.

### Skills Demonstrated

- Password Security Analysis
- Hash Identification
- Hashcat
- John the Ripper
- Dictionary Attacks
- Credential Security Assessment
- Security Reporting

### Project Outcome

This project demonstrated how attackers can recover weak passwords from compromised hashes and why organizations must implement strong authentication and password management controls.
""")

        st.markdown("### 📸 Evidence Screenshots")

        hash_images = [
            ("hash_1.png", "Figure 1: Hash identifier analysis"),
            ("hash_2.png", "Figure 2: Hash type recognition and command preparation"),
            ("Hash_3.png", "Figure 3: Hashcat cracking command execution"),
            ("Hash_4.png", "Figure 4: Hashcat recovered password results"),
            ("Hash_5.png", "Figure 5: Hashes.com blank password result"),
            ("Hash_6.png", "Figure 6: Hashes.com recovered password result"),
            ("Hash_7.png", "Figure 7: Hashes.com vagrant password result")
        ]

        for i in range(0, len(hash_images), 2):
            col1, col2 = st.columns(2)

            with col1:
                img_file, caption = hash_images[i]
                img_path = os.path.join(image_path, img_file)
                if os.path.exists(img_path):
                    st.image(img_path, caption=caption, use_container_width=True)
                else:
                    st.warning(f"Image not found: {img_path}")

            if i + 1 < len(hash_images):
                with col2:
                    img_file, caption = hash_images[i + 1]
                    img_path = os.path.join(image_path, img_file)
                    if os.path.exists(img_path):
                        st.image(img_path, caption=caption, use_container_width=True)
                    else:
                        st.warning(f"Image not found: {img_path}")

        download_report(
            "Password_Cracking_Hash_Analysis.docx",
            "📄 Download Hash Analysis Report"
        )































    # ==========================================================
    # PROJECT 4
    # ==========================================================

    elif selected_project == "Phishing Attack Simulation":

        st.markdown("""
# 🎣 Phishing Attack Simulation and Analysis

### Project Overview

This project recreated a phishing-based credential theft attack after a company experienced a breach caused by compromised credentials.

The objective was to demonstrate how attackers capture authentication information through social engineering and network poisoning techniques.

### Attack Scenario

The assessment recreated a phishing campaign targeting employees through a malicious file-sharing request.

### Tools Used

- Kali Linux
- Responder
- LLMNR Poisoning
- NBT-NS Poisoning
- DNS Poisoning

### Attack Methodology

1. Prepared attacker environment.
2. Configured Responder.
3. Enabled LLMNR and NBT-NS poisoning.
4. Simulated victim interaction.
5. Captured authentication hashes.
6. Validated successful credential theft.

### Key Findings

- Users could be tricked into submitting credentials.
- Network poisoning attacks were successful.
- Authentication hashes were captured.
- User awareness represented a significant security gap.

### Recommendations

- Security awareness training
- Disable LLMNR and NBT-NS
- Strengthen email filtering
- Deploy phishing-resistant MFA
- Improve incident reporting processes

### Skills Demonstrated

- Phishing Assessment
- Social Engineering Analysis
- Responder
- Credential Capture
- Network Poisoning
- Security Awareness Evaluation

### Project Outcome

Successfully recreated the credential theft attack and demonstrated how employee awareness and network hardening controls can significantly reduce phishing risk.
""")

        st.markdown("### 📸 Evidence Screenshots")

        phish_images = [
            ("phish_1.png", "Figure 1: Kali Linux IP address and Responder configuration"),
            ("phish_2.png", "Figure 2: Responder running with LLMNR, NBT-NS, and DNS poisoning enabled"),
            ("phish_3.png", "Figure 3: Victim workstation initiating connection to attacker system"),
            ("phish_4.png", "Figure 4: Credential prompt presented to the victim"),
            ("phish_5.png", "Figure 5: Captured authentication hashes demonstrating successful attack")
        ]

        for i in range(0, len(phish_images), 2):
            col1, col2 = st.columns(2)

            with col1:
                img_file, caption = phish_images[i]
                img_path = os.path.join(image_path, img_file)

                if os.path.exists(img_path):
                    st.image(
                        img_path,
                        caption=caption,
                        use_container_width=True
                    )
                else:
                    st.warning(f"Image not found: {img_path}")

            if i + 1 < len(phish_images):
                with col2:
                    img_file, caption = phish_images[i + 1]
                    img_path = os.path.join(image_path, img_file)

                    if os.path.exists(img_path):
                        st.image(
                            img_path,
                            caption=caption,
                            use_container_width=True
                        )
                    else:
                        st.warning(f"Image not found: {img_path}")





        download_report(
            "Phishing_Attack_Simulation_and_Analysis.docx",
            "📄 Download Phishing Assessment"
        )





















# ---------- MIS PROJECT ----------
elif page == "MIS Project":

    import os

    st.title("💻 MIS-470 Information Systems Security Project")
    st.subheader("Network Security • Password Cracking • SQL Injection • Ethical Security Practice")

    base_path = "Projects/This project was designed and developed by me"
    image_path = "Projects/This project was designed and developed by me/images"

    st.markdown("""
## Project Overview

This MIS-470 Information Systems Security project was designed to help students apply practical cybersecurity techniques in a controlled academic environment. The project focused on penetration testing fundamentals, including network scanning, password cracking, and SQL injection analysis.

The purpose of the project was not only to identify vulnerabilities, but also to explain how attackers may exploit them and what countermeasures can be implemented to protect computer systems.

### Main Security Exercises

#### 1. Nmap Security Scanning

The first exercise focused on using Nmap to scan a target IP address and identify exposed services, operating system details, and possible vulnerabilities.

**Key activities included:**

- Performing OS detection
- Identifying open ports and services
- Reviewing vulnerabilities from scan results
- Explaining how malicious actors could exploit exposed services
- Recommending countermeasures to reduce attack risk

#### 2. John the Ripper Password Cracking

The second exercise focused on password security and hash cracking using John the Ripper.

**Key activities included:**

- Identifying hash types
- Running John the Ripper through Windows Command Prompt
- Cracking password hashes using a wordlist
- Creating a username, hash, and password table
- Explaining why weak or cracked passwords represent serious security vulnerabilities
- Recommending stronger password and authentication controls

#### 3. SQL Injection Testing

The third exercise focused on SQL injection testing using sqlmap against a vulnerable test website.

**Key activities included:**

- Running sqlmap from Command Prompt
- Identifying internal database names
- Identifying database version information
- Extracting table names
- Identifying PHP version information
- Explaining SQL injection risks
- Recommending secure coding and database protection practices

### Ethical Security Disclaimer

This project emphasized that penetration testing knowledge must be used only in authorized environments. Testing systems, websites, devices, networks, or users without consent is illegal and unethical.

The project included a signed ethical pledge confirming that all knowledge gained in the course must be used responsibly and in compliance with university policy and the law.

### Skills Demonstrated

- Network security scanning
- Vulnerability identification
- Penetration testing methodology
- Password hash analysis
- Password cracking concepts
- SQL injection testing
- Security countermeasure development
- Ethical hacking awareness
- Technical reporting
- Team collaboration

### Project Outcome

This project demonstrated my ability to understand practical attack techniques, analyze system weaknesses, and recommend appropriate defensive controls. It also reinforced the importance of ethics, authorization, and responsible cybersecurity practice.
""")



    mis_images = [
        ("mis_01.png", "Nmap scan results with OS detection"),
        ("mis_02.png", "Detected services and vulnerabilities"),
        ("mis_03.png", "John the Ripper command execution"),
        ("mis_04.png", "Cracked password results"),
        ("mis_05.png", "SQLMap command execution"),
        ("mis_06.png", "Database and table discovery results")
    ]

    for i in range(0, len(mis_images), 2):
        col1, col2 = st.columns(2)

        with col1:
            img_file, caption = mis_images[i]
            full_path = os.path.join(image_path, img_file)
            if os.path.exists(full_path):
                st.image(full_path, caption=caption, use_container_width=True)

        if i + 1 < len(mis_images):
            with col2:
                img_file, caption = mis_images[i + 1]
                full_path = os.path.join(image_path, img_file)
                if os.path.exists(full_path):
                    st.image(full_path, caption=caption, use_container_width=True)

    st.markdown("### 📄 Full Project Specification")

    report_path = os.path.join(base_path, "Custom_Software_Development_Project_Specification.docx")

    try:
        with open(report_path, "rb") as file:
            st.download_button(
                label="Download MIS-470 Project Specification",
                data=file,
                file_name="Custom_Software_Development_Project_Specification.docx"
            )
    except FileNotFoundError:
        st.info("Place the MIS project file inside: Projects/This project was designed and developed by me/")









# ---------- SKILLS ----------
elif page == "Skills":

    st.title("🛠️ Cybersecurity Skills")
    st.subheader("Technical Security • Digital Forensics • Risk & Governance")

    st.markdown("""
<style>
.skill-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(0,229,255,0.35);
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 18px;
    box-shadow: 0 0 18px rgba(0,229,255,0.12);
}

.skill-title {
    color: #00e5ff;
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 10px;
}

.skill-tag {
    display: inline-block;
    background: linear-gradient(135deg, #00e5ff, #7b2cff);
    color: white;
    padding: 7px 13px;
    margin: 5px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 600;
}

.metric-box {
    text-align: center;
    background: rgba(0,229,255,0.09);
    border: 1px solid rgba(0,229,255,0.3);
    border-radius: 16px;
    padding: 18px;
}
.metric-number {
    color: #00e5ff;
    font-size: 34px;
    font-weight: 800;
}
.metric-label {
    color: #eaeaea;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

    st.markdown("""
    <div class="skill-card">
        <div class="skill-title">Professional Skill Snapshot</div>
        <p>
        My skills combine hands-on cybersecurity practice, digital forensic investigation,
        penetration testing, vulnerability analysis, IT auditing, risk assessment, and security governance.
        These capabilities were developed through graduate-level cyber forensics work, applied security projects,
        teaching experience, and practical use of industry tools.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-number">5+</div>
            <div class="metric-label">Security Domains</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-number">15+</div>
            <div class="metric-label">Security Tools</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-number">10+</div>
            <div class="metric-label">Cyber Projects</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-number">90%</div>
            <div class="metric-label">Security Improvement Impact</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="skill-card">
            <div class="skill-title">🕵️ Digital Forensics & Investigation</div>
            <span class="skill-tag">Digital Evidence Analysis</span>
            <span class="skill-tag">Forensic Imaging</span>
            <span class="skill-tag">Hash Verification</span>
            <span class="skill-tag">Evidence Integrity</span>
            <span class="skill-tag">Autopsy</span>
            <span class="skill-tag">WinHex</span>
            <span class="skill-tag">FTK Imager</span>
            <span class="skill-tag">FQLite</span>
            <span class="skill-tag">Investigation Reporting</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="skill-card">
            <div class="skill-title">🔍 Penetration Testing & Vulnerability Analysis</div>
            <span class="skill-tag">Penetration Testing</span>
            <span class="skill-tag">Vulnerability Assessment</span>
            <span class="skill-tag">Nmap</span>
            <span class="skill-tag">Enum4Linux</span>
            <span class="skill-tag">Hydra</span>
            <span class="skill-tag">Medusa</span>
            <span class="skill-tag">SQL Injection</span>
            <span class="skill-tag">SQLMap</span>
            <span class="skill-tag">Burp Suite</span>
            <span class="skill-tag">Acunetix</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="skill-card">
            <div class="skill-title">🔐 Password & Credential Security</div>
            <span class="skill-tag">Hash Analysis</span>
            <span class="skill-tag">Password Cracking</span>
            <span class="skill-tag">John the Ripper</span>
            <span class="skill-tag">Hashcat</span>
            <span class="skill-tag">NTLM Hashes</span>
            <span class="skill-tag">Credential Risk</span>
            <span class="skill-tag">Password Policy</span>
            <span class="skill-tag">MFA Awareness</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="skill-card">
            <div class="skill-title">📋 IT Auditing, Risk & Governance</div>
            <span class="skill-tag">IT Auditing</span>
            <span class="skill-tag">Risk Assessment</span>
            <span class="skill-tag">General Computer Controls</span>
            <span class="skill-tag">Access Review</span>
            <span class="skill-tag">Control Gap Analysis</span>
            <span class="skill-tag">Remediation Planning</span>
            <span class="skill-tag">Security Governance</span>
            <span class="skill-tag">Business Continuity</span>
            <span class="skill-tag">Disaster Recovery</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="skill-card">
            <div class="skill-title">🧭 Frameworks & Standards</div>
            <span class="skill-tag">ISO 27001</span>
            <span class="skill-tag">NIST CSF</span>
            <span class="skill-tag">COBIT</span>
            <span class="skill-tag">SOC 2 Concepts</span>
            <span class="skill-tag">PCI DSS Concepts</span>
            <span class="skill-tag">COSO ERM</span>
            <span class="skill-tag">HIPAA Awareness</span>
            <span class="skill-tag">Security Compliance</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="skill-card">
            <div class="skill-title">🌐 OSINT, Reconnaissance & Network Security</div>
            <span class="skill-tag">OSINT</span>
            <span class="skill-tag">Active Reconnaissance</span>
            <span class="skill-tag">Passive Reconnaissance</span>
            <span class="skill-tag">Whois</span>
            <span class="skill-tag">Shodan</span>
            <span class="skill-tag">Wappalyzer</span>
            <span class="skill-tag">Netcraft</span>
            <span class="skill-tag">DNS Analysis</span>
            <span class="skill-tag">Network Security</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="skill-card">
        <div class="skill-title">🧠 What These Skills Allow Me To Do</div>
        <p>
        I can investigate digital evidence, validate forensic images, identify vulnerabilities,
        perform reconnaissance, analyze password security, evaluate IT controls, assess risk,
        and translate technical findings into clear recommendations for management.
        </p>
        <p>
        My strongest value is the ability to connect technical security work with business risk,
        compliance expectations, and practical remediation.
        </p>
    </div>
    """, unsafe_allow_html=True)











# ---------- CERTIFICATIONS ----------
elif page == "Certifications":

    st.title("🏆 Certifications & Professional Development")
    st.subheader("Continuous Learning • Industry Credentials • Cybersecurity Excellence")

    st.markdown("""
<style>

.cert-card{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(0,229,255,0.35);
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 20px;
    box-shadow: 0 0 18px rgba(0,229,255,0.12);
}

.cert-title{
    color:#00e5ff;
    font-size:24px;
    font-weight:700;
    margin-bottom:10px;
}

.cert-badge{
    display:inline-block;
    padding:10px 15px;
    margin:6px;
    border-radius:25px;
    background:linear-gradient(135deg,#00e5ff,#6d28d9);
    color:white;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="cert-card">
<div class="cert-title">🎯 Professional Certifications</div>

<span class="cert-badge">Certified Incident Responder (eCIR) - 2026</span>
<span class="cert-badge">Junior Penetration Tester (eJPT) - 2026</span>
<span class="cert-badge">CompTIA Security+ - 2024</span>
<span class="cert-badge">CyberDefense Certification (TestOut) - 2024</span>
<span class="cert-badge">Cybersecurity Incident Response Analysis (STC) - 2023</span>
<span class="cert-badge">Introduction to Cyber Security - 2019</span>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="cert-card">
<div class="cert-title">🎓 Academic Achievements</div>

<ul>
<li>Master of Cyber Forensics and Security – Illinois Institute of Technology</li>
<li>GPA: 3.9 / 4.0</li>
<li>Bachelor of Science in Computer Science</li>
<li>Saudi Ministry of Education Scholarship Recipient</li>
</ul>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="cert-card">
<div class="cert-title">👥 Professional Memberships</div>

<ul>
<li>Women in Cybersecurity (WiCyS)</li>
<li>OWASP – Open Web Application Security Project</li>
<li>Cyber Security Club – King Saud University</li>
</ul>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="cert-card">
<div class="cert-title">📚 Areas of Continuous Development</div>

<ul>
<li>Digital Forensics</li>
<li>Incident Response</li>
<li>Penetration Testing</li>
<li>Threat Detection & Analysis</li>
<li>IT Auditing</li>
<li>Risk Assessment</li>
<li>Security Governance</li>
<li>Cloud Security</li>
<li>Security Operations</li>
</ul>

</div>
""", unsafe_allow_html=True)







# ---------- CONTACT ----------
elif page == "Contact":

    st.title("📬 Contact")
    st.subheader("Let's Connect")

    st.markdown("""
<style>

.contact-card{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(0,229,255,0.35);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 0 20px rgba(0,229,255,0.12);
}

.contact-title{
    color:#00e5ff;
    font-size:30px;
    font-weight:700;
    margin-bottom:20px;
}

.contact-item{
    font-size:20px;
    margin-bottom:18px;
}

</style>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="contact-card">

<div class="contact-title">
Alaa Al Saad
</div>

<div class="contact-item">
📍 Saudi Arabia
</div>

<div class="contact-item">
📞 +966 530661057
</div>

<div class="contact-item">
📧 <a href="mailto:aalsaad.alaa@gmail.com" target="_blank">aalsaad.alaa@gmail.com</a>
</div>

<div class="contact-item">
💼 <a href="https://linkedin.com/in/alaa-alsad" target="_blank">linkedin.com/in/alaa-alsad</a>
</div>

<br>


<p>
Feel free to reach out for professional opportunities, collaborations, or cybersecurity discussions.
</p>

</div>
""", unsafe_allow_html=True)
