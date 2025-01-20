from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.template import loader
import cv2
import tempfile

# Create your views here.
def index(request):
	return render(request, "guardian/index.html")


def upload_video(request):
	if (request.method == "POST"):
		file = request.FILES["file"]
		
		with tempfile.NamedTemporaryFile() as temp:
			temp.write(file.read())
   
			# Handle the file upload
			cap = cv2.VideoCapture(temp.name)
			print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
			print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
			# Check if the file is a video
			if not cap.isOpened():
				return HttpResponse("File is not a video")
			
			return FileResponse(open(temp.name, "rb"))
