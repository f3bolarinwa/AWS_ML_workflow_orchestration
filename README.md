# Project: Orchestrate, Deploy and Monitor an AWS Machine Learning workflow for Image Classification

## Project Description

Image Classifiers are used in the field of computer vision to identify the content of an image and it is used across a broad variety of industries, from advanced technologies like autonomous vehicles and augmented reality, to eCommerce platforms, and even in diagnostic medicine.

You are hired as a Machine Learning Engineer for a scone-delivery-focused logistics company, Scones Unlimited, and you’re working to ship an Image Classification model. The image classification model can help the team in a variety of ways in their operating environment: detecting people and vehicles in video feeds from roadways, better support routing for their engagement on social media, detecting defects in their scones, and many more!

In this project, you'll be building an image classification model that can automatically detect which kind of vehicle delivery drivers have, in order to route them to the correct loading bay and orders. Assigning delivery professionals who have a bicycle to nearby orders and giving motorcyclists orders that are farther can help Scones Unlimited optimize their operations.

As an MLE, your goal is to ship a scalable and safe model. Once your model becomes available to other teams on-demand, it’s important that your model can scale to meet demand, and that safeguards are in place to monitor and control for drift or degraded performance.

## My Work Description

In this project, I used Amazon Sagemaker to build an image classification model that can tell bicycles apart from motorcycles. I deployed my model to a sagemaker endpoint, used AWS Lambda functions to build supporting services (imput image serialization, prediction/inference, inference filter), and AWS Step Functions to compose my model and services into an event-driven application. This project serves as a portfolio-ready demo that showcases my ability to build and compose scalable, ML-enabled, AWS applications.

The project was completed live on AWS cloud platform using Amazon Sagemaker

## AWS Sagemaker Studio SetUp

Instance: ml.t3.medium instance (2 vCPU + 4 GiB)

Kernel: Python 3 (MXNet 1.8 Python 3.7 CPU Optimized)

Sagemaker Image: Data Science 3.0

## Repository Content Description

1)Solution Notebook.ipynb: project solution jupyter notebook completed on AWS sagemaker

2)MyStateMachine-o2oyarhz7.asl.json: workflow step-function state-machine in json format

3)lambda_serializeImageData.py: lambda function for encoding/serialize input image

4)lambda_classifyImageData.py: lambda function for image prediction/inference

5)lambda_filterInference.py: lambda function for inference filter

6)Images: contains screenshots of AWS UI for training job, endpoint, sagemaker studio, lambda function, step function, s3, etc
