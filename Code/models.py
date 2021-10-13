from PIL import Image
from flask import Flask, render_template, redirect, url_for, request
from PIL import Image
import torch
import torchvision.transforms as transforms
from torch.autograd import Variable

def skin_cancer_model(location):

        model = torch.load('model_skin_saved.pt', map_location='cpu')
        label = {0:'No',1:'Yes'}
        loader = transforms.Compose([
        transforms.Resize((128,128)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0],
                                std=[1] )])

        def image_loader(image_name):
                """load image, returns cuda tensor"""
                image = Image.open(image_name)
                image = loader(image).float()
                image = image.reshape(1,3,128,128)
                image = Variable(image, requires_grad=True)
                return image

        image = image_loader(location)
        prediction = int(torch.argmax(model(image).round()))
        print(prediction)
        return label[prediction]
def brain_cancer_model(location):

        model = torch.load('model_heart_saved.pt', map_location='cpu')
        label = {0:'No',1:'Yes'}
        loader = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),
        transforms.Resize((200,200)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0],
                                std=[1] )])

        def image_loader(image_name):
                """load image, returns cuda tensor"""
                image = Image.open(image_name)
                image = loader(image).float()
                image = image.reshape(1,1,200,200)
                image = Variable(image, requires_grad=True)
                return image

        image = image_loader(location)
        prediction = int(torch.argmax(model(image).round()))
        return label[prediction]

def combined_cancer_model(location):

        model = torch.load('model_combined_saved.pt', map_location='cpu')
        label = {0:'Brain',1:'Lung',2:'Skin',3:'No'}
        loader = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),
        transforms.Resize((320,320)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0],
                                std=[1] )])

        def image_loader(image_name):
                """load image, returns cuda tensor"""
                image = Image.open(image_name)
                image = loader(image).float()
                image = image.reshape(1,1,320,320)
                image = Variable(image, requires_grad=True)
                return image

        image = image_loader(location)
        prediction = int(torch.argmax(model(image).round()))
    
        return label[prediction]

def gen_cancer_model(location):
        model = torch.load('model_combined_yesno_saved.pt', map_location='cpu')
        label = {0:'No',1:'Yes'}
        loader = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),
        transforms.Resize((128,128)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0],
                                std=[1] )])

        def image_loader(image_name):
                """load image, returns cuda tensor"""
                image = Image.open(image_name)
                image = loader(image).float()
                image = image.reshape(1,1,128,128)
                image = Variable(image, requires_grad=True)
                return image

        image = image_loader(location)
        prediction = int(torch.argmax(model(image).round()))
    
        return label[prediction]

