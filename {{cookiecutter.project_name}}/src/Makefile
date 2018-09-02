test:
	STAGE_NAME=test DYNAMODB_HOST=http://localhost:8888 py.test -v --gherkin-terminal-reporter

test-pdb:
	STAGE_NAME=test DYNAMODB_HOST=http://localhost:8888 py.test -v --gherkin-terminal-reporter --pdb

run:
	STAGE_NAME=test DYNAMODB_HOST=http://localhost:8888 chalice local --stage dev

deploy-test:
	chalice deploy --stage test --no-autogen-policy

deploy-dev:
	chalice deploy --stage dev --no-autogen-policy

deploy-production:
	chalice deploy --stage production --no-autogen-policy

start-ddb:
	java -Djava.library.path=/opt/dynamodb/DynamoDBLocal_lib -jar /opt/dynamodb/DynamoDBLocal.jar -inMemory -port 8888 &

install-ddb:
	mkdir -p /opt/dynamodb/
	wget http://dynamodb-local.s3-website-us-west-2.amazonaws.com/dynamodb_local_latest.tar.gz -O /opt/dynamodb/dynamodb_local_latest.tar.gz
	tar -xzf /opt/dynamodb/dynamodb_local_latest.tar.gz -C /opt/dynamodb