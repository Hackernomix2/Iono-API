from rest_framework import serializers
from .models import Project , CollectedData , Research

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'creator', 'name', 'description', 'problem_statement', 'goal', 'start_date']

class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ['id', 'project', 'name', 'document_overview', 'document', 'start_date']

class CollectedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectedData
        fields = ['id', 'project', 'form_id', 'result_id', 'form_description']