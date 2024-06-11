# import streamlit as st
# import cv2
# import numpy as np
# import base64

# from streamlit.components.v1 import declare_component

# # Declare the custom component
# webcam_component = declare_component("webcam_component", path="./streamlit_webcam_component/frontend")

# def main():
#     st.title("Webcam Capture with Custom Component")

#     # Create a checkbox for the user to toggle the video capture
#     if st.checkbox("Start Video Capture"):
#         component_value = webcam_component()  # Get the frame from the custom component
#         if component_value:
#             frame_b64 = component_value.get("image")  # Get the base64 image data
#             if frame_b64 is not None:
#                 # Decode the base64 image data into a NumPy array
#                 frame_bytes = base64.b64decode(frame_b64.split(',')[1])
#                 frame = cv2.imdecode(np.frombuffer(frame_bytes, np.uint8), cv2.IMREAD_COLOR)
#                 # Process frame using OpenCV here
#                 # Example: Flip the image
#                 flipped_frame = cv2.flip(frame, 1)
#                 st.image(flipped_frame, channels="BGR")

# if __name__ == "__main__":
#     main()



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
