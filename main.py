import streamlit as st
import yt_dlp


# Function to download video
def download_video(url):
    ydl_opts = {
        'format': 'best',  # Download the best video and audio streams
        'merge_output_format': None,  # Merge video and audio if needed
        'outtmpl': '%(title)s.%(ext)s',  # Use video title as filename
        'noplaylist': True,  # Download only single video, not a playlist
    }

    # Create a YoutubeDL object with the options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        title = info_dict.get('title', 'downloaded_video')
        ext = info_dict.get('ext', 'mp4')
        return f"{title}.{ext}"


# Streamlit UI
st.title('YouTube Video Downloader')

# Input for YouTube video URL
url = st.text_input('Enter YouTube video URL')

# Button to download the video
if st.button('Download Video'):
    if url:
        try:
            st.write("Downloading video...")
            filename = download_video(url)
            st.write("Download complete!")
            st.success("Video downloaded successfully.")
            # Provide download link for the user
            st.markdown(f'[Download video](./{filename})')
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a valid YouTube URL.")
