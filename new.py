import boto3
s3client=boto3.client('s3')
db=boto3.resource('dynamodb')
table=db.Table('dynamodb')
s3_resp=s3client.get_object(
    Bucket='rishi1994',
    Key='target.csv'
)
csv_file=s3_resp['Body'].read().decode('utf-8')
store=csv_file.split('\r\n')
for read in store:
    print(read)
    read=read.split(',')
    table.put_item(
        Item={
            'emp_id':int(read[0]),
            'name':read[1],
            'location':read[2],
            'salary':read[3]
        }
    )

