from contextlib import contextmanager

import streamlit as st
import streamlit.components.v1 as components


@contextmanager
def container(title=None, padding=100, **kwargs):
    background_color = kwargs.get("background_color", "#f0f0f0")
    st.markdown(
        f"""
        <style>
        div[data-modal-container='true'] {{
            position: fixed;
            z-index: 1001;
        }}

        div[data-modal-container='true'] h1 a {{
            display: none
        }}

        div[data-modal-container='true']::before {{
                position: fixed;
                content: ' ';
                left: 0;
                right: 0;
                top: 0;
                bottom: 0;
                z-index: 1000;
                background-color: rgba(0, 0, 0, 0.5);
        }}

        div[data-modal-container='true'] > div:first-child > div:first-child {{
            width: unset !important;
            background-color: {background_color};
            margin: auto;
            padding: {padding}px;
            margin-top: {padding}px;
            margin-left: -{padding}px;
            margin-bottom: -{2*padding}px;
            z-index: 1001;
            border-radius: 5px;
        }}
        div[data-modal-container='true'] > div > div:nth-child(2)  {{
            z-index: 1003;
            position: absolute;
        }}
        div[data-modal-container='true'] > div > div:nth-child(2) > div {{
            text-align: right;
        }}
        div[data-modal-container='true'] > div > div:nth-child(2) > div > button {{
            right: 0;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    with st.container():
        _container = st.container()
        if title:
            _container.markdown(f"<h1>{title}</h1>", unsafe_allow_html=True)

        # close_ = st.button("X")
        # if close_:
        #     close()
    components.html(
        """
        <script>
        // MODAL
        const iframes = parent.document.body.getElementsByTagName('iframe');
        let container
        for(const iframe of iframes)
        {
          if (iframe.srcdoc.indexOf("MODAL") !== -1) {
            container = iframe.parentNode.previousSibling;
            container.setAttribute('data-modal-container', 'true');
          }
        }
        </script>
        """,
        height=0,
        width=0,
    )

    with _container:
        yield _container
