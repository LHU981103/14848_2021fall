import boto3
import csv

# Create s3 bucket
s3 = boto3.resource('s3', 
                    aws_access_key_id='AKIASNFLMCGY4I6QXGFN', 
                    aws_secret_access_key='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')

#try:
#    s3.create_bucket(Bucket='database-14848hw3', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
#except Exception as e:
#    print (e)

## Access bucket
#bucket = s3.Bucket("database-14848hw3")
#bucket.Acl().put(ACL='public-read')

## Upload files
#s3.Object('database-14848hw3', 'exp1.csv').put(Body=open('exp1.csv', 'rb'))
#s3.Object('database-14848hw3', 'exp2.csv').put(Body=open('exp2.csv', 'rb'))
#s3.Object('database-14848hw3', 'exp3.csv').put(Body=open('exp3.csv', 'rb'))
#s3.Object('database-14848hw3', 'experiments.csv').put(Body=open('experiments.csv', 'rb'))

# Create DynamoDB table
dyndb = boto3.resource('dynamodb', region_name='us-west-2',
                       aws_access_key_id='AKIASNFLMCGY4I6QXGFN', 
                    aws_secret_access_key='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')

#try:
#    table = dyndb.create_table(
#            TableName='14848hw3',
#            KeySchema=[
#                {
#                    'AttributeName': 'PartitionKey',
#                    'KeyType': 'HASH'  # Partition key
#                },
#                {
#                    'AttributeName': 'RowKey',
#                    'KeyType': 'RANGE'  # Sort key
#                }
#            ],
#            AttributeDefinitions=[
#                {
#                    'AttributeName': 'PartitionKey',
#                    'AttributeType': 'S'
#                },
#                {
#                    'AttributeName': 'RowKey',
#                    'AttributeType': 'S'
#                }
#            ],
#            ProvisionedThroughput={
#                'ReadCapacityUnits': 5,
#                'WriteCapacityUnits': 5
#            }
#        )
#except Exception as e:
#    print(e)

## Reading csv file
#table = dyndb.Table("14848hw3")
#with open('experiments.csv', 'r') as csvfile:
#     csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for item in csvf:
#         if item[0].isdigit():
#             md = s3.Object('database-14848hw3', item[4]).Acl().put(ACL='public-read')
#             url = "https://s3-us-west-2.amazonaws.com/database-14848hw3/"+item[4]

#             metadata_item = {'PartitionKey': f'Experiment{item[0]}', 'RowKey': f'Data{item[0]}', 
#                              'Id': item[0], 'Temp': item[1], 
#                              'Conductivity' : item[2], 'Concentration' : item[3], 'url':url} 
#             try:
#                table.put_item(Item=metadata_item)
#                print("item sent to table")
#             except:
#                print ("item may already be there or another failure")

table = dyndb.Table("14848hw3")
response = table.get_item(
     Key={
     'PartitionKey': 'Experiment3',
     'RowKey': 'Data3'
     }
)
item = response['Item']
print(item)
print(response)