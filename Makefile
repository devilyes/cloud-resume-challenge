.PHONY: build

build:
	sam build

deploy-infra:
	sam build && aws-vault exec ilyes-user --no-session -- sam deploy

deploy-site:
	aws-vault exec ilyes-user --no-session -- aws s3 sync ./resume-site s3://ilyesfi-website

invoke-put:
	sam build && aws-vault exec ilyes-user --no-session -- sam local invoke PutCountFunction