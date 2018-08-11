test:
	DYNAMODB_HOST=http://localhost:8888 py.test

test-pdb:
	DYNAMODB_HOST=http://localhost:8888 py.test --pdb

run:
	DYNAMODB_HOST=http://localhost:8888 chalice local --stage dev

deploy-test:
	chalice deploy --stage test --no-autogen-policy

deploy-dev:
	chalice deploy --stage dev --no-autogen-policy

deploy-prod:
	chalice deploy --stage production --no-autogen-policy

start-ddb:
	java -Djava.library.path=/opt/dynamodb/DynamoDBLocal_lib -jar /opt/dynamodb/DynamoDBLocal.jar -inMemory -port 8888 &
