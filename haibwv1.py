import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(page_title="How an Internet Browser Works", layout="wide")

    # Title and Introduction
    st.title("How an Internet Browser Works")
    st.markdown("""
    An **internet browser** is a crucial tool that allows users to access and interact with content on the **World Wide Web**. 
    It retrieves, interprets, and displays web pages from servers using the **HTTP** or **HTTPS** protocols.
    Below is a detailed explanation of how it works step by step.
    """)

    # Step 1: User Input (URL Entry)
    with st.expander("1. User Input (URL Entry)"):
        st.markdown("""
        - The process begins when a user enters a URL (e.g., `https://www.example.com`) into the browser's address bar or clicks a hyperlink.
        - The URL specifies:
          - **Protocol**: How the browser communicates with the server (HTTP/HTTPS).
          - **Domain Name**: The website’s address.
          - **Path**: The specific location of a resource/page on the server.
        """)

    # Step 2: DNS Lookup
    with st.expander("2. Domain Name System (DNS) Lookup"):
        st.markdown("""
        - The browser doesn’t understand domain names like `example.com` directly.
        - It sends a request to a **DNS server** to convert the domain name into an **IP address** (e.g., `93.184.216.34`), which is the actual address of the web server hosting the site.
        """)

    # Step 3: Establishing a Connection
    with st.expander("3. Establishing a Connection"):
        st.markdown("""
        - Using the IP address, the browser establishes a connection with the web server.
        - If the URL uses **HTTPS** (secure), the browser negotiates a secure connection using **SSL/TLS encryption**.
        """)

    # Step 4: Sending an HTTP/HTTPS Request
    with st.expander("4. Sending an HTTP/HTTPS Request"):
        st.markdown("""
        - The browser sends an **HTTP request** to the server for the desired resource.
        - Example of an HTTP request:
          ```
          GET /index.html HTTP/1.1
          Host: www.example.com
          ```
        """)

    # Step 5: Web Server Response
    with st.expander("5. Web Server Response"):
        st.markdown("""
        - The web server processes the browser's request and responds with:
          - A **status code** (e.g., `200 OK` for success, `404 Not Found` for missing pages).
          - The **content** of the page (HTML, CSS, JavaScript, images, etc.).
        """)

    # Step 6: Rendering the Web Page
    with st.expander("6. Rendering the Web Page"):
        st.markdown("""
        - The browser receives the content (often starting with an HTML file) and processes it to display the page. This involves:
          - **Parsing HTML**: Building the **DOM** (Document Object Model), a hierarchical structure of the page’s elements.
          - **Loading CSS**: Styling the DOM elements (colors, fonts, layout, etc.).
          - **Executing JavaScript**: Adding interactivity and dynamic content.
          - **Loading Assets**: Fetching images, videos, fonts, and other linked resources.
        """)

    # Step 7: Rendering Engine
    with st.expander("7. Rendering Engine"):
        st.markdown("""
        - Browsers use rendering engines to convert code into visual pages:
          - **Chrome, Edge, Opera**: Blink Engine.
          - **Safari**: WebKit Engine.
          - **Firefox**: Gecko Engine.
        - The rendering engine:
          1. Lays out page elements based on the DOM and CSS.
          2. Paints (renders) the elements on the screen.
          3. Continuously updates the page as new data arrives or JavaScript modifies it.
        """)

    # Step 8: Handling User Interaction
    with st.expander("8. Handling User Interaction"):
        st.markdown("""
        - The browser handles user inputs, such as clicks, scrolling, and form submissions.
        - JavaScript often manages these interactions dynamically.
        """)

    # Step 9: Caching and Performance Optimization
    with st.expander("9. Caching and Performance Optimization"):
        st.markdown("""
        - Browsers cache (store) resources like HTML, CSS, images, and scripts locally to load pages faster during subsequent visits.
        - Techniques like prefetching and compression optimize the browsing experience.
        """)

    # Summary Workflow
    st.subheader("Summary Workflow")
    st.markdown("""
    **1.** URL Input → **2.** DNS Lookup → **3.** Server Connection → **4.** HTTP Request → **5.** Server Response → 
    **6.** Rendering → **7.** User Interaction
    """)

    # Footer
    st.info("The browser acts as the bridge between the user and web servers, retrieving and presenting web content efficiently.")

if __name__ == "__main__":
    main()
