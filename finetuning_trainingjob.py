import openai

training_file_id = 'file-f54635457746477a9d654c47042f7f49'
validation_file_id = 'file-035d2014b8454358bc7b4185e5c17822'
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
