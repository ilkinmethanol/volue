#Installing dependencies (Docker)

echo "*********************************"
echo "**                             **"
echo "**  API & CALC SERVICE SETUP   **"
echo "**                             **"
echo "*********************************"


API_SERVICE_DIR="api_service/"
CALC_SERVICE_DIR="calculating_service/"

if [ -x "$(command -v docker)" ]; then
    echo "Docker has already been installed, skipping"
    
else
    echo "Installing docker"
    if command -v apt-get >/dev/null; then
       echo "Installing docker"
       apt-get install docker -y 
    elif command -v yum >/dev/null; then
       yum install docker-compose
    fi


fi

if [ -x "$(command -v docker-compose)" ]; then
    echo "Docker-compose has already been installed, skipping"
    
else
    echo "Installing docker-compose"
    if command -v apt-get >/dev/null; then
       echo "Installing docker"
       apt-get install docker-compose -y 
    elif command -v yum >/dev/null; then
       yum install docker-compose
    fi

fi
# Setting up API Service

cd $API_SERVICE_DIR
echo $(pwd)
docker-compose up -d
docker ps --filter name=apiservice_web_1 -q

if [ $? -eq 0 ]; then
   echo OK
   echo "API Service has been set up on http://0.0.0.0:8003"
else
   set -e
fi


cd ..
# Setting up Calculation service
cd $CALC_SERVICE_DIR
docker-compose up -d
docker ps --filter name=calculatingservice_web_1 -q

if [ $? -eq 0 ]; then
   echo OK
   echo "Calculation service is ready : http://0.0.0.0:8006"
else
   set -e
fi


echo $(pwd)
cd ..

echo "More info about API Usage : APIServiceOpenapi.yaml / CalcServiceOpenapi.yaml"

