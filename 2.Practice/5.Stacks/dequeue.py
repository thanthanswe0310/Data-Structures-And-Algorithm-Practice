# class Node:
#     def __init__(self,value):
#         self.value =value
#         self.next  = None
#
# class Queue:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.first = new_node
#         self.last  = new_node
#         self.length = 1
#
#     def print_queue(self):
#         temp =self.first
#         while temp is not None:
#             print(temp.value)
#             temp = temp.next
#
#     def enqueue(self,value):
#         new_node = Node(value)
#         if self.first is None:
#             self.first = new_node
#             self.last  = new_node
#         else:
#             self.last.next = new_node
#             self.last = new_node
#         self.length +=1
#
#     def dequeue(self):
#         if self.length ==0:
#             return None
#         temp =self.first
#         if self.length ==1:
#             self.first = None
#             self.last  = None
#         else:
#             self.first =self.first.next
#             temp.next  = None
#         self.length -=1
#         return temp.value
#
#
#
#
#
# my_queue = Queue(1)
# my_queue.enqueue(2)
#
# # (2) Items - Returns 2 node
# print(my_queue.dequeue())
# # (1) Items - return 1 node
# print(my_queue.dequeue())
# # (0) Items - Returns None
# print(my_queue.dequeue())
#




import subprocess
import shutil
import json

def get_video_fps(video_path):
    """Get FPS of a video using ffprobe."""
    result = subprocess.run([
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=r_frame_rate",
        "-of", "json", video_path
    ], capture_output=True, text=True)

    data = json.loads(result.stdout)
    fps_str = data['streams'][0]['r_frame_rate']  # e.g., "30/1"
    num, denom = map(int, fps_str.split('/'))
    return num / denom

# === Main Program ===
if shutil.which("ffmpeg") is None:
    print("❌ Please install FFmpeg and add it to your system PATH.")
else:
    print("✅ FFmpeg found. Running command...")

    input_video = r"C:\Users\MYCOM\Downloads\final hand detect.v3i.yolov8\train\detected_images.mp4"
    output_video = "output_expanded_slowed.mp4"
    bitrate = "2524k"

    # Get original video FPS
    fps = get_video_fps(input_video)
    print(f"🎞️ Original FPS: {fps:.2f}")

    # Run FFmpeg with correct FPS to preserve timing
    subprocess.run([
        "ffmpeg",
        "-i", input_video,
        "-r", str(fps),          # 🔑 Set output frame rate
        "-b:v", bitrate,
        "-bufsize", bitrate,
        "-maxrate", bitrate,
        "-y",                    # Overwrite output
        output_video
    ])

    print(f"✅ Output saved as: {output_video}")
