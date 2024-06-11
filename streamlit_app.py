import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode
import av
import cv2
import numpy as np

class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        # Convert the frame from WebRTC's format to OpenCV's format
        img = frame.to_ndarray(format="bgr24")

        # Your OpenCV image processing logic here
        # ...
        # Example: Mirror the image
        img = cv2.flip(img, 1)

        # Convert back to WebRTC's format
        return av.VideoFrame.from_ndarray(img, format="bgr24")


def main():
    st.title("Webcam Display with Streamlit-WebRTC and OpenCV")

    webrtc_streamer(
        key="example",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoProcessor,
    )

if __name__ == "__main__":
    main()
