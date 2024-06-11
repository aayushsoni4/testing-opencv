
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, WebRtcMode
import av
import cv2
import numpy as np


class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Add a log message to check if the frame is received
        st.write("Frame received and processing started")

        # Your OpenCV image processing logic here
        img = cv2.flip(img, 1)  # Example: Mirror the image

        st.write("Frame processed, sending back")  # Another log message

        return av.VideoFrame.from_ndarray(img, format="bgr24")


def main():
    st.title("Webcam Display with Streamlit-WebRTC and OpenCV")

    webrtc_streamer(
        key="example",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={
            "iceServers": [
                {"urls": ["stun:stun.l.google.com:19302"]},  # STUN server
                {
                    "urls": ["turn:your-turn-server-address"],
                    "username": "your-turn-server-username",
                    "credential": "your-turn-server-password",
                },  # TURN server
            ]
        },
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoProcessor,
    )


if __name__ == "__main__":
    main()
