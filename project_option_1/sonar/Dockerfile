FROM sonarqube
RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744.zip
RUN unzip sonar-scanner-cli-4.0.0.1744.zip
ENV PATH="/opt/sonarqube/sonar-scanner-4.0.0.1744/bin:${PATH}"
EXPOSE 9000

