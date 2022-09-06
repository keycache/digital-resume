from datetime import datetime
from functools import lru_cache
from typing import Any, Dict, Iterator

import streamlit as st
import streamlit_modal as st_modal
from PIL import Image

import core.modal as modal
from definitions import (
    BG_COLOR,
    DESCRIPTION,
    EDUCATION,
    EMAIL,
    GPA,
    INSTITUTE_NAME,
    INSTITUTE_STAY,
    NAME,
    NOW,
    PAGE_ICON,
    PAGE_TITLE,
    PERSONAL_PROJECTS,
    PROFESSIONAL_COMPANY,
    PROFESSIONAL_EXPERIENCE,
    PROFESSIONAL_HARD_SKILLS,
    PROFESSIONAL_PROJECTS,
    PROFESSIONAL_STAY,
    PROFESSIONAL_SUMMARY,
    PROFESSIONAL_TITLE,
    PROJECT_DEMO,
    PROJECT_DESCRIPTION,
    PROJECT_DETAILS,
    PROJECT_NAME,
    PROJECT_TECNOLOGIES,
    PROJECT_URL,
    SOCIAL_MEDIA,
    css_file_path,
    profile_pic_path,
    resume_file_path,
)


@lru_cache
def read_file(file_path, mode: str = "r"):
    with open(file=file_path, mode=mode) as f:
        return f.read()


def load_resources():
    css = read_file(css_file_path)
    profile_pic = Image.open(profile_pic_path)
    resume = read_file(resume_file_path, mode="rb")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    return profile_pic, resume


def render_hero_section(profile_pic, resume):
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=resume,
            file_name="Akash-Patki-Resume.pdf",
            mime="application/octet-stream",
        )
        pressed = st.button("📫 Contact Me")
        if pressed:
            st_modal.open()


def render_social_presence():
    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


def render_professional_experience():
    def get_prof_title(job) -> str:
        return job[PROFESSIONAL_TITLE]

    def get_prof_company(job) -> str:
        return job[PROFESSIONAL_COMPANY]

    def get_prof_dates(job) -> Iterator[str]:
        st_date, end_date = job[PROFESSIONAL_STAY]
        DATE_FORMAT = "%Y %b"
        return st_date.strftime(
            DATE_FORMAT
        ), end_date if end_date == NOW else end_date.strftime(DATE_FORMAT)

    def get_prof_projects(job):
        return job[PROFESSIONAL_PROJECTS]

    def get_prof_proj_details(prof_project):
        return (prof_project[PROJECT_NAME], prof_project[PROJECT_DETAILS])

    def render_professional_project(prof_project):
        prof_proj_name, prof_proj_details = get_prof_proj_details(prof_project)
        st.markdown(
            f"""
        - ► **{prof_proj_name}**: {prof_proj_details}
        """
        )

    def render_professional_projects(job):
        prof_projects = get_prof_projects(job)
        for prof_project in prof_projects:
            render_professional_project(prof_project=prof_project)

    def render_job(job: Dict[str, Any]):
        title = get_prof_title(job)
        company = get_prof_company(job)
        st_date, end_date = get_prof_dates(job)
        return st.markdown(
            f"""
        ### {title} - {company}
        *{st_date} - {end_date}*
        """
        )

    st.write("#")
    st.header("Professional Experience")
    for job in PROFESSIONAL_EXPERIENCE:
        render_job(job=job)
        render_professional_projects(job=job)


def render_personal_projects():
    def get_personal_projects():
        return PERSONAL_PROJECTS

    def get_personal_project_details(
        personal_project: Dict[str, str]
    ) -> Iterator[str]:
        return (
            personal_project.get(PROJECT_NAME),
            personal_project.get(PROJECT_DESCRIPTION),
            personal_project.get(PROJECT_URL),
            personal_project.get(PROJECT_DEMO),
            personal_project.get(PROJECT_TECNOLOGIES),
        )

    def render_personal_project(personal_project):
        (
            name,
            description,
            github_url,
            demo_url,
            technologies,
        ) = get_personal_project_details(personal_project)
        demo_url = (
            f"[:globe_with_meridians: Demo]({demo_url})" if demo_url else ""
        )
        github_url = (
            f"[:information_source: Github]({github_url})"
            if github_url
            else ""
        )
        tags = " ".join([f"`{tech}`" for tech in technologies])
        st.markdown(
            f"""
        - :star: **{name}**: {description}. \n
            - {github_url} \n
            - {demo_url} \n
            - {tags}
        """
        )

    st.write("#")
    st.header("Personal Projects")
    personal_projects = get_personal_projects()
    for personal_project in personal_projects:
        render_personal_project(personal_project)


def render_summary():
    st.write("#")
    st.header("Experience & Qualifications")
    st.write("\n".join(PROFESSIONAL_SUMMARY))
    # st.markdown('''
    # [![Repo](https://cdn-icons-png.flaticon.com/16/1384/1384060.png)](https://github.com/AvratanuBiswas/PubLit)

    # ''', unsafe_allow_html=True)


def render_skills():
    st.write("#")
    st.header("Hard Skills")
    st.write("\n".join(PROFESSIONAL_HARD_SKILLS))


def render_education():
    def get_education():
        return EDUCATION

    def get_name(entry: Dict[str, str]) -> str:
        return entry[INSTITUTE_NAME]

    def get_stay(entry: Dict[str, Any]) -> Iterator[str]:
        start, end = entry[INSTITUTE_STAY]
        return (
            start.strftime("%Y %B"),
            (end.strftime("%Y %B") if isinstance(end, datetime) else end),
        )

    def get_gpa(entry: Dict[str, str]) -> str:
        return entry[GPA]

    def render_education_entry(entry):
        name, stay, gpa = get_name(entry), get_stay(entry), get_gpa(entry)
        start, end = stay
        st.markdown(
            f"<h3 style='text-align: center;'><b>{name}</b></h3>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<p style='text-align: center;'><i>{start} to {end}</i></p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<h4 style='text-align: center;'>GPA: <b>{gpa}</b></h4>",
            unsafe_allow_html=True,
        )
        st.markdown("#")

    st.write("#")
    st.header("Education")
    for entry in get_education():
        render_education_entry(entry=entry)


def render_contact_form():
    if st_modal.is_open():
        # with st_modal.container():
        with modal.container(
            background_color=BG_COLOR, padding=20, title="Contact Me"
        ):
            st.subheader("Fill up the details below to get in touch")
            name = st.text_input("Name", max_chars=50, placeholder="John Doe")
            email = st.text_input(
                "Email", max_chars=50, placeholder="me@example.com"
            )
            message = st.text_area(
                "Message", max_chars=250, placeholder="Sampe Message"
            )
            st.markdown("---")

            feedback = st.empty()

            columns = st.columns(6)
            submit = columns[0].button("Submit")
            close = columns[1].button("Close")
            if submit:
                if name and email and message:
                    print(
                        "Submitting the request now"
                        f" {name}->{email}->{message}"
                    )
                    st_modal.close()
                else:
                    feedback.error(
                        f"Name, Email and Message are all mandatory"
                    )
            if close:
                st_modal.close()


def run():
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
    profile_pic, resume = load_resources()
    render_hero_section(profile_pic, resume)
    render_social_presence()
    render_summary()
    render_skills()
    render_professional_experience()
    render_personal_projects()
    render_education()
    render_contact_form()


if __name__ == "__main__":
    run()
