import os
from datetime import datetime

# Constants
BG_COLOR = "#002b36"
TEXT_COLOR = "#ffffff"

PROJECT_NAME = "project-name"
PROJECT_DESCRIPTION = "project-description"
PROJECT_URL = "project-url"
PROJECT_DEMO = "project-demo"
PROJECT_TECNOLOGIES = "project-technologies"
PROJECT_DETAILS = "project-details"

PROFESSIONAL_TITLE = "professional-title"
PROFESSIONAL_COMPANY = "professional-organization"
PROFESSIONAL_STAY = "professional-duration"
PROFESSIONAL_JOB_DESCRIPTION = "professional-job-description"
PROFESSIONAL_PROJECTS = "professional-projects"

INSTITUTE_NAME = "institute-name"
INSTITUTE_STAY = "study-duration"
GPA = "gpa"

NOW = "now"

current_dir = os.path.dirname(os.path.abspath(__file__))
css_file_path = os.path.join(current_dir, "styles", "main.css")
profile_pic_path = os.path.join(current_dir, "assets", "profile-pic.jpg")
resume_file_path = os.path.join(
    current_dir, "assets", "Akash-Patki-Resume.pdf"
)


# --- GENERAL SETTINGS ---
NAME = "Akash Patki"
PAGE_TITLE = f"Digital Resume | {NAME}"
PAGE_ICON = ":wave:"
DESCRIPTION = """
Senior Full Stack Developer, tech enthusiast assisting enterprises by building data-driven applications.
"""

EMAIL = "johndoe@email.com"

SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCEpDzpADDZRiITpHrtuJ5sA",
    "LinkedIn": "https://www.linkedin.com/in/akashpatki/",
    "GitHub": "https://github.com/keycache",
}

PROFESSIONAL_SUMMARY = [
    (
        "- ✔️  10+ years experience developing high frequency data driven"
        " applications."
    ),
    "- ✔️  Strong hands on experience and knowledge in Python and React.",
    (
        "- ✔️  Good understanding of Computer Science principles and their"
        " respective applications."
    ),
    (
        "- ✔️  Excellent team-player and displaying strong sense of initiative"
        " on tasks."
    ),
]

PROFESSIONAL_HARD_SKILLS = [
    (
        "- Programming Languages: Python (flask, django, pandas), Typescript,"
        " C#, Java and more."
    ),
    "- UI: React, Angular.",
    "- Databases: Postgres, MySQL, sandra(Object Oriented Database)",
    "- DevOps: Jenkins, Terraform",
    "- Tools: NodeJS, AWS, Docker",
]

PROFESSIONAL_EXPERIENCE = [
    {
        PROFESSIONAL_TITLE: "Staff Engineer",
        PROFESSIONAL_COMPANY: "SecurityScorecard Inc, Toronto, Canada",
        PROFESSIONAL_STAY: (datetime(2022, 3, 22), NOW),
        PROFESSIONAL_JOB_DESCRIPTION: "",
        PROFESSIONAL_PROJECTS: [
            {
                PROJECT_NAME: (
                    "Execute “Machine Learning” pipeline for 'Questionnaire"
                    " Filling'"
                ),
                PROJECT_DETAILS: (
                    "Lead role in developing the engineering pipeline to"
                    " deliver end to end solution for one of the “Machine"
                    " Learning” projects. Role involved coordinating with Data"
                    " Science and DevOps while architecting the solution. The"
                    " successful project delivery will result in 70-90 % time"
                    " savings while filling questionnaires."
                ),
            },
            {
                PROJECT_NAME: "Introduce locale based translation",
                PROJECT_DETAILS: (
                    "Independently delivered the project to support new"
                    " locales. Project demanded co-ordination between third"
                    " party vendors and Japanese users, across multiple"
                    " time-zones for a successful project completion. The"
                    " application is now set up for a configuration based"
                    " onboarding of new locale based translations, reducing"
                    " the go live time by 70%."
                ),
            },
            {
                PROJECT_NAME: "Project Management",
                PROJECT_DETAILS: (
                    "Coordinate with Product, UX and Sales Engineers for"
                    " requirement gathering and refinement. Interview new"
                    " candidates for roles in the team. Streamline"
                    " interviewing process(at least, just within the team)."
                    " Coordinate with “Customer Success” teams to rapidly"
                    " resolve the issues and maintain our SLOs."
                ),
            },
            {
                PROJECT_NAME: "Technologies used",
                PROJECT_DETAILS: (
                    "React JS v17.0+, ES6/ES7 to build functional components."
                    " Python v3.9+. TypeScript and Node v16+ to manage backend"
                    " applications. Deliver CI/CD using Docker(to containerize"
                    " the applications), Terraform(to manage AWS"
                    " infrastructure)"
                ),
            },
        ],
    },
    {
        PROFESSIONAL_TITLE: "Vice President(Senior Software Engineer)",
        PROFESSIONAL_COMPANY: "Bank of America, New York City, USA",
        PROFESSIONAL_STAY: (datetime(2015, 5, 26), datetime(2021, 3, 12)),
        PROFESSIONAL_JOB_DESCRIPTION: (
            "The role involved designing, developing, deploying and supporting"
            " Full Stack (React 16.8+, Python 3.8 and JAVA 8) applications in"
            " *nix operating environments. One of the primary responsibilities"
            " was exploring  and incorporating solutions into the technology"
            " stack. The project relied on using agile software methodologies"
            " and leveraging TDD software development practices."
        ),
        PROFESSIONAL_PROJECTS: [
            {
                PROJECT_NAME: (
                    "Building Trade Capture solutions in React, Python and"
                    " Java"
                ),
                PROJECT_DETAILS: (
                    "Lead role in decommissioning legacy “Credit Trade"
                    " Capture” system, automating workflows, resulting in"
                    " savings greater than $1 million a year. Design and"
                    " development lead for retiring a legacy reporting system"
                    " to port (20+) credit instruments/products."
                ),
            },
            {
                PROJECT_NAME: (
                    "Designing high frequency (full stack)trading applications"
                ),
                PROJECT_DETAILS: (
                    "Design and deploy multiple python and OpenFin based"
                    " React-JS (16.8+) applications for onboarding “Trade"
                    " Capture” and “Exception Monitoring” products. Extend the"
                    " project to support Configuration based UI - Workflows to"
                    " automate dynamic trade capture. Implement solutions"
                    " (frontend and backend) for “Performance Metrics"
                    " Dashboard” to monitor system health for exceptions, per"
                    " trade performance trends and bottlenecks."
                ),
            },
            {
                PROJECT_NAME: "Building Java Services (Backend)",
                PROJECT_DETAILS: (
                    "Implement services in core JAVA 8 (Multithreading,"
                    " Collections, lambda) to connect and communicate with"
                    " clearing houses (ICE and TriOptima). Build REST services"
                    " for UI applications through Spring (Boot)"
                ),
            },
            {
                PROJECT_NAME: "Requirement Gathering and Analysis",
                PROJECT_DETAILS: (
                    "Interact with Sales, Traders and Middle Office personnel"
                    " to gather functional/non-functional and performance"
                    " requirements to conduct an effective “Impact Analysis”."
                    " Create a BRD (Business Requirement Document) based on"
                    " findings."
                ),
            },
            {
                PROJECT_NAME: (
                    "Automating the Testing Suite for Integration Testing"
                ),
                PROJECT_DETAILS: (
                    "Investigate and evaluate the technologies for project"
                    " needs. Implement a new solution (with puppeteer) to"
                    " improve execution time by 200%."
                ),
            },
            {
                PROJECT_NAME: "Technologies used",
                PROJECT_DETAILS: (
                    "React JS v16.8+, ES6/ES7 to build functional components."
                    " Python v3.7+ and JAVA 8 to deliver backend services for"
                    " the UI."
                ),
            },
        ],
    },
    {
        PROFESSIONAL_TITLE: "SOFTWARE ENGINEER",
        PROFESSIONAL_COMPANY: "J. P. Morgan Chase, New York City, USA",
        PROFESSIONAL_STAY: (datetime(2013, 7, 1), datetime(2015, 5, 22)),
        PROFESSIONAL_JOB_DESCRIPTION: (
            "This role involved an understanding of the proprietary Risk"
            " evaluation framework (Athena) developed by J.P Morgan, along"
            " with the components (Pixie, Hydra, Extract and Stress Framework,"
            " STPServer, Reactive circuits, etc.) that made up this framework."
            " Developed, deployed and provided L3 Support for “Fixed Income"
            " Repo” applications along with the standard duties of a Scrum"
            " Master in an “Agile Environment”. The project involved enhancing"
            " the Dashboard Application to visualize Risk and PnL benchmarks"
            " for “Fixed Income Repo” (LOB), as well as onboarding new"
            " businesses. This required thorough understanding of the existing"
            " code, workflows and the business."
        ),
        PROFESSIONAL_PROJECTS: [
            {
                PROJECT_NAME: "Requirement/Impact Analysis",
                PROJECT_DETAILS: (
                    "Primarily involved direct interaction with business/desk"
                    " to gather requirements, formalizing it into a"
                    " requirement document and an eventual requirement and"
                    " impact analysis."
                ),
            },
            {
                PROJECT_NAME: "Scrum Master",
                PROJECT_DETAILS: (
                    "The primary responsibilities involved maintaining the"
                    " JIRA board, following-up on the task progress through a"
                    " daily scrum call, task prioritization, sprint"
                    " pre-planning, post sprint analysis(velocity calculation,"
                    " sprint retrospective, etc.)"
                ),
            },
            {
                PROJECT_NAME: "Traders/Middle or Front office interaction",
                PROJECT_DETAILS: (
                    "Weekly L3 Support involved regular interaction with users"
                    " to identify, investigate and verify the resolution of"
                    " support issues (as well as maintain a healthy rapport)."
                    " Depending on the issue we would need to involve Athena"
                    " CORE team."
                ),
            },
            {
                PROJECT_NAME: "Miscellaneous",
                PROJECT_DETAILS: (
                    "Regular refactoring to improve code/application"
                    " performance (once, to the tune of 20 times-size wise of"
                    " the output). Code reviewing, managing entitlements"
                    " within and across teams, etc."
                ),
            },
            {
                PROJECT_NAME: "Technologies used",
                PROJECT_DETAILS: (
                    "Intermediate to Advanced level Python is extensively used"
                    " to develop framework/s, modules, scripts and automation"
                    " processes. Basic to intermediate level Linux proficiency"
                    " was required to manage accounts, reports and file"
                    " management for day to day duties."
                ),
            },
        ],
    },
    {
        PROFESSIONAL_TITLE: "JUNIOR SOFTWARE ENGINEER",
        PROFESSIONAL_COMPANY: "Bank of America, New York City, USA",
        PROFESSIONAL_STAY: (datetime(2012, 4, 1), datetime(2013, 7, 1)),
        PROFESSIONAL_JOB_DESCRIPTION: (
            "This role involved a thorough understanding of “Quartz” framework"
            " (built for developing applications to evaluate risk across"
            " different services) and its core components (like DAG, Sandra,"
            " QzTable, Inform Client, etc.). Designed, developed, deployed and"
            " maintained Prime Brokerage and Securities Lending applications."
            " Managed the 'design and implementation' in coordination with"
            " BAs, team leads and production support to ensure timely"
            " completion of the deliverables, within an 'Agile Environment'."
        ),
        PROFESSIONAL_PROJECTS: [
            {
                PROJECT_NAME: "Prime Brokerage",
                PROJECT_DETAILS: (
                    "Developed financial risk evaluation applications that"
                    " generated reports to evaluate exposure of instruments to"
                    " the firm. Developed/Refactored code to meet the new"
                    " requirements; reduced execution time by 20%. Developed a"
                    " “Reconciliation” application to check the veracity of"
                    " the risk evaluation reports and optimized it to reduce"
                    " execution time to a tune of 50%."
                ),
            },
            {
                PROJECT_NAME: "Securities Lending",
                PROJECT_DETAILS: (
                    "Developed client-side (AutoBorrow) applications to manage"
                    " Inventory. Designed/developed the core functionalities"
                    " and the framework to build outgoing and inbound feeds to"
                    " and from third party systems (Equilend, LCOR, AMPS)."
                    " Refactoring of server-side components to improve"
                    " application performance (design, space and time wise),"
                    " prompting my move to the CORE team."
                ),
            },
            {
                PROJECT_NAME: "Technologies used",
                PROJECT_DETAILS: (
                    "Python was used to develop feed framework, reconciliation"
                    " application and unit/integration test cases. SQL for"
                    " stored procedures to reconcile the results. C# for bug"
                    " fixes and upgrading legacy “Security Lending”"
                    " applications."
                ),
            },
        ],
    },
    {
        PROFESSIONAL_TITLE: "RESEARCH ASSISTANT",
        PROFESSIONAL_COMPANY: "Vanderbilt University, Nashville, TN, USA",
        PROFESSIONAL_STAY: (datetime(2009, 8, 1), datetime(2011, 12, 31)),
        PROFESSIONAL_JOB_DESCRIPTION: (
            "The work mainly covered the area of Model Integrated Computing"
            " (MIC). MIC focuses on the formal representation, composition,"
            " analysis, and manipulation of models during the design process."
            " My work involved development of tools that aided this extremely"
            " complex design and implementation process."
        ),
        PROFESSIONAL_PROJECTS: [
            {
                PROJECT_NAME: "GReAT Debugger",
                PROJECT_DETAILS: (
                    "Developed GReAT (Graph Rewrite and Transformation)"
                    " debugger, adding new features and fixing bugs."
                ),
            },
            {
                PROJECT_NAME: "Model Comparator",
                PROJECT_DETAILS: (
                    "Developed “Model Comparator” for quick and efficient way"
                    " of testing changes to the core features of GReAT."
                ),
            },
            {
                PROJECT_NAME: "Testing Automation",
                PROJECT_DETAILS: (
                    "Automated the testing of new builds across different"
                    " applications and operating systems."
                ),
            },
            {
                PROJECT_NAME: "Technologies used",
                PROJECT_DETAILS: (
                    "Worked with C++, C++/CLI, C# and JAVA across MIC"
                    " projects. Python to automate build and test processes."
                    " (Python) Cheetah for designing templates to automate"
                    " code generation."
                ),
            },
        ],
    },
    {
        PROFESSIONAL_TITLE: "SOFTWARE DEVELOPER",
        PROFESSIONAL_COMPANY: "IBM India, Pune",
        PROFESSIONAL_STAY: (datetime(2009, 8, 1), datetime(2011, 12, 31)),
        PROFESSIONAL_JOB_DESCRIPTION: (
            "The work mainly covered the area of Model Integrated Computing"
            " (MIC). MIC focuses on the formal representation, composition,"
            " analysis, and manipulation of models during the design process."
            " My work involved development of tools that aided this extremely"
            " complex design and implementation process."
        ),
        PROFESSIONAL_PROJECTS: [
            {
                PROJECT_NAME: "GReAT Debugger",
                PROJECT_DETAILS: (
                    "Developed GReAT (Graph Rewrite and Transformation)"
                    " debugger, adding new features and fixing bugs."
                ),
            },
            {
                PROJECT_NAME: "Model Comparator",
                PROJECT_DETAILS: (
                    "Developed “Model Comparator” for quick and efficient way"
                    " of testing changes to the core features of GReAT."
                ),
            },
            {
                PROJECT_NAME: "Testing Automation",
                PROJECT_DETAILS: (
                    "Automated the testing of new builds across different"
                    " applications and operating systems."
                ),
            },
            {
                PROJECT_NAME: "Technologies used",
                PROJECT_DETAILS: (
                    "Worked with C++, C++/CLI, C# and JAVA across MIC"
                    " projects. Python to automate build and test processes."
                    " (Python) Cheetah for designing templates to automate"
                    " code generation."
                ),
            },
        ],
    },
]
PERSONAL_PROJECTS = [
    {
        PROJECT_NAME: "RSS Feeder",
        PROJECT_DESCRIPTION: "Proof of Concept RSS Feeder",
        PROJECT_URL: "https://github.com/keycache/st-rss-reader",
        PROJECT_DEMO: (
            "https://keycache-st-rss-reader-runner-083b2u.streamlitapp.com/"
        ),
        PROJECT_TECNOLOGIES: (
            "python",
            "rss",
            "opml",
            "streamlit",
            "streamlit-cloud",
        ),
    },
    {
        PROJECT_NAME: "Auto Image Paint",
        PROJECT_DESCRIPTION: "Random Image Generator - ASMR",
        PROJECT_URL: "https://github.com/keycache/auto-draw",
        PROJECT_DEMO: "https://www.youtube.com/watch?v=c1M7Hr9Jc_I&t=1s",
        PROJECT_TECNOLOGIES: (
            "python",
            "opencv",
        ),
    },
    {
        PROJECT_NAME: "Digital Resume",
        PROJECT_DESCRIPTION: "My personal resume, digitized",
        PROJECT_URL: "https://github.com/keycache/digital-resume",
        PROJECT_TECNOLOGIES: ("python", "streamlit", "docker"),
    },
    {
        PROJECT_NAME: "Movie Maker",
        PROJECT_DESCRIPTION: "Ready to use lightweight 'Video Maker'",
        PROJECT_URL: "",
        PROJECT_TECNOLOGIES: (
            "python",
            "moviepy",
        ),
    },
]

EDUCATION = [
    {
        INSTITUTE_NAME: "Vanderbilt University, Nashville, TN - USA",
        INSTITUTE_STAY: (datetime(2009, 8, 1), datetime(2011, 12, 1)),
        GPA: 3.87,
    },
    {
        INSTITUTE_NAME: (
            "National Institute of Technology, Rourkela, Orissa - India"
        ),
        INSTITUTE_STAY: (datetime(2003, 8, 10), datetime(2007, 5, 10)),
        GPA: 7.54,
    },
]
