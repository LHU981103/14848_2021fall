Sentiment-Analysis

URLs for all of your Docker Hub images:
* frontend: https://hub.docker.com/r/lhu98jes/sentiment-analysis-frontend
* webapp: https://hub.docker.com/r/lhu98jes/sentiment-analysis-webapp
* logic: https://hub.docker.com/r/lhu98jes/sentiment-analysis-logic

Breakdown:

Step-I: Build Container Image for Each Service and push them to Docker Hub.
1. Setting up frontend app and push to docker: 
	i. Download NodeJS and NPM 
	ii. In terminal, do "npm install" & "npm start" & "npm run build"
	iii. "docker build -f Dockerfile -t lhu98jes/sentiment-analysis-frontend ."
	iv. "docker push lhu98jes/sentiment-analysis-frontend"

2. Setting up webapp and push to docker:
	i. Download Maven
	ii. In terminal, do "mvn install"
	iii. Go to "target" dir, and do "java -jar sentiment-analysis-web-0.0.1-SNAPSHOT.jar --sa.logic.api.url=http://localhost:5000"
	iv. "docker build -f Dockerfile -t lhu98jes/sentiment-analysis-webapp ."
	v. "docker push lhu98jes/sentiment-analysis-webapp"

3. Setting up logic and push to docker:
	i. In sa-logic/sa dir, do "python -m pip install -r requirements.txt"
	ii. "python -m textblob.download_corpora"
	iii. "docker build -f Dockerfile -t lhu98jes/sentiment-analysis-logic ."
	iv. "docker push lhu98jes/sentiment-analysis-logic"

4. Running all containers:
	i. "docker run -d -p 5050:5000 --name sa-logic lhu98jes/sentiment-analysis-logic"
	ii. "docker run -d -p 8080:8080 --link sa-logic -e SA_LOGIC_API_URL='http://sa-logic:5000' lhu98jes/sentiment-analysis-webapp"
	iii. "docker run -d -p 80:80 lhu98jes/sentiment-analysis-frontend"
	
	* https://github.com/rinormaloku/k8s-mastery/issues/25

5. Test:
	Open browser and go to localhost:80, and you are able to get the result when you type anything in the analyzer.