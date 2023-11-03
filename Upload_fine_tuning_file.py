# Upload fine-tuning files
import openai
import os

# openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_key = 'a1896925aed74decbfae56a9e0771915'
openai.api_base = 'https://openainorthcentraltest.openai.azure.com/'
openai.api_type = 'azure'
# This API version or later is required to access fine-tuning for turbo/babbage-002/davinci-002
openai.api_version = '2023-09-15-preview'

training_file_name = 'training_set.jsonl'
validation_file_name = 'validation_set.jsonl'

# Upload the training and validation dataset files to Azure OpenAI with the SDK.

training_response = openai.File.create(
    file=open(training_file_name, "rb"), purpose="fine-tune", user_provided_filename="training_set.jsonl"
)
training_file_id = training_response["id"]

validation_response = openai.File.create(
    file=open(validation_file_name, "rb"), purpose="fine-tune", user_provided_filename="validation_set.jsonl"
)
validation_file_id = validation_response["id"]

print("Training file ID:", training_file_id)
print("Validation file ID:", validation_file_id)

response = openai.FineTuningJob.create(
    training_file=training_file_id,
    validation_file=validation_file_id,
    model="gpt-35-turbo-0613",
)

job_id = response["id"]

# You can use the job ID to monitor the status of the fine-tuning job.
# The fine-tuning job will take some time to start and complete.

print("Job ID:", response["id"])
print("Status:", response["status"])
print(response)
