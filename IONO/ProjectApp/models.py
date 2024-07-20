from django.db import models
from pgvector.django import VectorField
from Tools.toolSet import embed

class Project(models.Model):
    creator = models.ForeignKey('UserApp.User', on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    problem_statement = models.TextField()
    goal = models.TextField()
    start_date = models.DateField(auto_now_add=True)

class Research(models.Model):
    project = models.ForeignKey('ProjectApp.Project', on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 100)
    document_overview = models.TextField()
    document = models.FileField(upload_to='research_documents/' , null= True)
    start_date = models.DateField(auto_now_add=True)
    embedding = VectorField(dimensions= 768 , null = True , blank = True) # we will embed the description of the research document
    
    def set_embedding(self):
        text = f"research name : {self.name} \n research overview : {self.document_overview}"
        self.embedding = embed(text)
    
    #over write the save method to set the embedding
    def save(self, *args, **kwargs):
        self.set_embedding()
        super(Research, self).save(*args, **kwargs)

    
class CollectedData(models.Model):
    project = models.ForeignKey('ProjectApp.Project', on_delete = models.SET_NULL, null = True)
    form_id = models.CharField(max_length=255) 
    result_id = models.CharField(max_length=255) 
    form_description = models.TextField()
    embedding = VectorField(dimensions= 768 , null = True , blank = True) # we will embed the description of form
    
    def set_embedding(self):
        text = f"form id : {self.form_id} \n form description : {self.form_description}"
        self.embedding = embed(text)
    
    #over write the save method to set the embedding
    def save(self, *args, **kwargs):
        self.set_embedding()
        super(CollectedData, self).save(*args, **kwargs)
