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


Step-II: Orchestrate Sentiment Analyzer’s containers and run them on GKE
In cloud shell, do the following:
Push docker frontend image to Google container registry
1. "docker pull lhu98jes/sentiment-analysis-frontend"
2. "docker tag lhu98jes/sentiment-analysis-frontend gcr.io/caramel-aria-325416/lhu98jes/sentiment-analysis-frontend"
3. "docker push gcr.io/caramel-aria-325416/lhu98jes/sentiment-analysis-frontend"

Push docker logic image to Google container registry
4. "docker pull lhu98jes/sentiment-analysis-logic"
5. "docker tag lhu98jes/sentiment-analysis-logic gcr.io/caramel-aria-325416/lhu98jes/sentiment-analysis-logic"
6. "docker push gcr.io/caramel-aria-325416/lhu98jes/sentiment-analysis-logic"

Push docker webapp image to Google container registry
4. "docker pull lhu98jes/sentiment-analysis-webapp"
5. "docker tag lhu98jes/sentiment-analysis-webapp gcr.io/caramel-aria-325416/lhu98jes/sentiment-analysis-webapp"
6. "docker push gcr.io/caramel-aria-325416/lhu98jes/sentiment-analysis-webapp"

In Google container registry, do the following:
Create pods and start service for frontend
1. Choose frontend image and click "Deploy to GKE", using the default setting
2. Click "Expose", choose Load Balancer as the service type, and use 80 for both port and target port.

Create pods and start service for logic
1. Choose logic image and click "Deploy to GKE", using the default setting
2. Click "Expose", choose cluster IP as the service type, and use 80 for port and 5000 for target port.

Create pods and start service for webapp
1. Choose logic image and click "Deploy to GKE"
2. Copy the IP address <logic-IP> from the deployment for logic, Add an environment variable: "SA_LOGIC_API_URL" -> "http://<logic-IP>"
2. Click "Expose", choose Load Balancer as the service type, and use 80 for port and 8080 for target port.

Get frontend application to connect to webapp
1. Copy the IP address and port <webapp-IP: port> from the deployment for webapp
2. In local terminal, edit "analyzeSentence" function in the file "sa-frontend/src/App.js" and use "http://<webapp-IP: port>/sentiment" to fetch
3. "yarn build"
4. "docker build -f Dockerfile -t lhu98jes/sentiment-analysis-frontend:kube ."
5. "docker push lhu98jes/sentiment-analysis-frontend:kube"
6. Push the new version of docker frontend image to Google container registry as above
7. Edit the yaml file in frontend service in GKE, to make it point to the new version of the image in container registry

