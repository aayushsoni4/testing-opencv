import streamlit as st
import cv2
import numpy as np
import base64

from streamlit.components.v1 import declare_component

# Declare the custom component
webcam_component = declare_component("webcam_component", path="./streamlit_webcam_component/frontend")

def main():
    st.title("Webcam Capture with Custom Component")

    # Create a checkbox for the user to toggle the video capture
    if st.checkbox("Start Video Capture"):
        component_value = webcam_component()  # Get the frame from the custom component
        if component_value:
            frame_b64 = component_value.get("image")  # Get the base64 image data
            if frame_b64 is not None:
                # Decode the base64 image data into a NumPy array
                frame_bytes = base64.b64decode(frame_b64.split(',')[1])
                frame = cv2.imdecode(np.frombuffer(frame_bytes, np.uint8), cv2.IMREAD_COLOR)
                # Process frame using OpenCV here
                # Example: Flip the image
                flipped_frame = cv2.flip(frame, 1)
                st.image(flipped_frame, channels="BGR")

if __name__ == "__main__":
    main()
