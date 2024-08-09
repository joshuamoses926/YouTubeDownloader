import streamlit as st
import yt_dlp

# Streamlit app title
st.title("YouTube Video Downloader")

# Input field for the url
url = st.text_input("Paste a URL")

if url:
    try:
        # Define options for yt-dlp
        ydl_opts = {
            'format': 'best',  # Download the best quality video available
            'outtmpl': '%(title)s.%(ext)s',  # Save the downloaded file with the video title as the filename
        }

        # Create a YoutubeDL object with the defined options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video information and download the video
            info_dict = ydl.extract_info(url, download=True)

            # Get the video title from the extracted information
            video_title = info_dict.get('title', None)

            # Display a success message once the download is complete
            st.success(f"Downloaded '{video_title}' successfully!")
            st.write(f"File saved in: {ydl_opts['outtmpl']}")

    except Exception as e:
        # If an error occurs, display an error message with the exception details
        st.error(f"An error occurred: {e}")

# Instructions
st.write("Please note that this app is for educational purposes only. Respect YouTube's policies when downloading videos.")