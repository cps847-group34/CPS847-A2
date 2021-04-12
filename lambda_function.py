import json

#testing 2
def lambda_handler(event, context):
  first_name = event.get('first_name', None)
  last_name = event.get('last_name', None)

  if first_name is None: 
    raise Exception('Please provide a first name.')
  if last_name is None: 
    raise Exception('Please provide a last name.')

  return {
    'statusCode': 200,
    'output': first_name + " " + last_name
  }
