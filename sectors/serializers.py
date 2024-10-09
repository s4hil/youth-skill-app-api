# sectors/serializers.py
from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    course_name = serializers.CharField()
    topic_name = serializers.CharField()
    url = serializers.URLField()
    module_no = serializers.IntegerField()
