# sectors/views.py
import os
import csv
from collections import defaultdict
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CourseSerializer

class SectorCoursesView(APIView):
    def get(self, request, sector_name=None):
        data_folder = os.path.join('data', sector_name)
        modules = defaultdict(list)  # Dictionary to group by module_no

        if os.path.exists(data_folder):
            for csv_file in os.listdir(data_folder):
                if csv_file.endswith('.csv'):
                    course_data = self.read_csv_file(os.path.join(data_folder, csv_file))
                    # Append data grouped by module
                    for entry in course_data:
                        modules[entry['module_no']].append(entry)

            return Response({"sector": sector_name, "modules": modules})

        return Response({"error": "Sector not found"}, status=404)

    def read_csv_file(self, file_path):
        courses = []
        with open(file_path, 'r', encoding='utf-8') as f:  # Specify encoding
            reader = csv.DictReader(f)
            for row in reader:
                # For each row in the CSV, extract the fields including ModuleNo
                course_data = {
                    "course_name": row['CourseName'],
                    "topic_name": row['TopicName'],
                    "url": row['URL'],
                    "module_no": int(row['ModuleNo'])  # Convert ModuleNo to integer
                }
                # Validate the serializer
                serializer = CourseSerializer(data=course_data)
                if serializer.is_valid():
                    courses.append(serializer.data)
        return courses

