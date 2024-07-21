import os
import subprocess
from django.shortcuts import render
from django.conf import settings
from.models import Project, Research, CollectedData 
from .serializer import ProjectSerializer, ResearchSerializer, CollectedDataSerializer
from rest_framework.decorators import api_view,permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from Tools.AI import chat, research , data_analysis
from Tools.toolSet import read_sheet_data,start_service
from Tools.prepareForm import load
from rest_framework.parsers import MultiPartParser, FormParser



#get all methode
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_project(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_research(request):
    research = Research.objects.all()
    serializer = ResearchSerializer(research, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_collected_data(request):
    collected_data = CollectedData.objects.all()
    serializer = CollectedDataSerializer(collected_data, many=True)
    return Response(serializer.data)


#get one methodes by id
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_one_project(request, pk):
    project = get_object_or_404(Project , id=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_one_research(request, pk):
    research = get_object_or_404(Research ,id=pk)
    serializer = ResearchSerializer(research)
    return Response({'data' : serializer.data} , status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_one_collected_data(request, pk):
    collected_data = get_object_or_404(CollectedData , id=pk)
    serializer = CollectedDataSerializer(collected_data)
    return Response({'data' : serializer.data} , status = status.HTTP_200_OK)


#get all user projects
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_projects(request):
    projects = Project.objects.filter(creator=request.user)
    serializer = ProjectSerializer(projects, many=True)
    return Response({ 'data' : serializer.data , 'count' : projects.count() } , status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_research(request):
    research = Research.objects.filter(project__creator=request.user)
    serializer = ResearchSerializer(research, many=True)
    return Response({ 'data' : serializer.data , 'count' : research.count() } , status = status.HTTPjsonResponse_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_project_data(request, pk):
    project = get_object_or_404(Project , id=pk)
    collected_data = CollectedData.objects.filter(project=project)
    collected_data_serializer = CollectedDataSerializer(collected_data, many=True)
    return Response({ 'collected_data' : collected_data_serializer.data} , status = status.HTTP_200_OK)


#gets the project in which the user made the research in like a the workspace
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_research_project(request, pk):
    research = get_object_or_404(Research , id=pk)
    project = research.project
    if project:
        serializer = ProjectSerializer(project)
        return Response({'data' : serializer.data} , status = status.HTTP_200_OK)
    else:
        return Response({'data' : 'project not found'} , status = status.HTTP_200_OK)


#create methdes

def load_ai(name, description, goal, problem_statement):
    return research(name, description, goal, problem_statement)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    serializer = ProjectSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(creator = request.user)
        name , description , problem_statement , goal = request.data['name'] , request.data['description'] , request.data['problem_statement'] , request.data['goal']
        ai_suggestion = load_ai(name, description, goal, problem_statement)
        return Response({ 'data': serializer.data , 'AI' : ai_suggestion} , status = status.HTTP_201_CREATED)
    return Response({'errors' : serializer.errors} , status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_research(request):
    serializer = ResearchSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({ 'data': serializer.data} , status = status.HTTP_201_CREATED)
    return Response({'errors' : serializer.errors} , status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_collected_data(request):
    serializer = CollectedDataSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({ 'data': serializer.data} , status = status.HTTP_201_CREATED)
    return Response({'errors' : serializer.errors} , status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ask_ai(request , pk):
    project = get_object_or_404(Project , id=pk)    
    name, description, goal, problem_statement = project.name , project.description , project.goal , project.problem_statement
    question = request.data['question']
    ai_suggestion = chat(name, description, goal, problem_statement , question)
    return Response({ 'AI' : ai_suggestion} , status = status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_data_analysis(request , pk):
    sheet_id, sheet_name, sheet_range = request.data['sheet_id'], request.data['sheet_name'], request.data['sheet_range']
    data = load(sheet_id, sheet_name, sheet_range)
    Project = get_object_or_404(Project , id=pk)
    research_name , description , goal , problem_statement = Project.name , Project.description , Project.goal , Project.problem_statement 
    analysis = data_analysis(research_name, description, goal, problem_statement , data)
    return Response({ 'AI' : analysis} , status = status.HTTP_200_OK)


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_pdf_and_process(request):
    if request.method == 'POST':
        file = request.FILES['file']
        paper_name = request.data.get('paperName', '')
        author_id = request.data.get('author_id', None)
        project_id = request.data.get('project_id', None)
        author_name = request.data.get('authorName', '')
        overview = request.data.get('documentOverview', '')

        # Save the file temporarily
        temp_path = os.path.join(settings.MEDIA_ROOT, 'temp', file.name)
        with open(temp_path, 'wb+') as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)
    
        # Prepare paths for OCR processing
        ocr_script_path = r'adobe-dc-pdf-services-sdk-python\src\ocrpdf\ocr_pdf.py'
        output_dir = os.path.join(settings.MEDIA_ROOT, 'ocr_output')
        os.makedirs(output_dir, exist_ok=True)
        output_file_path = os.path.join(output_dir, 'ocr_output.pdf')

        # Call the OCR script using subprocess
        try:
            result = subprocess.run(
                ['python', ocr_script_path, temp_path, output_file_path],
                check=True,
                capture_output=True,
                text=True
            )
            ocr_output_path = result.stdout.strip()
            print(f'OCR output path: {ocr_output_path}')
        except subprocess.CalledProcessError as e:
            print(e.stderr)
            os.remove(temp_path)
            return Response({'error': 'OCR processing failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # Prepare the research data
        research_data = {
            'paperName': paper_name,
            'author': author_id,
            'project': project_id,
            'authorName': author_name,
            'documentOverview': overview,  
            'document': output_file_path, 
        }

        serializer = ResearchSerializer(data=research_data)
        if serializer.is_valid():
            serializer.save()
            os.remove(temp_path) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            os.remove(temp_path)  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#update methode
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_project(request, pk):
    project = get_object_or_404(Project , id=pk)
    serializer = ProjectSerializer(instance = project , data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({ 'data': serializer.data} , status = status.HTTP_200_OK)
    return Response({'errors' : serializer.errors} , status = status.HTTP_400_BAD_REQUEST)

