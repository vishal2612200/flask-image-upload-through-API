echo
echo "---Register a user---"
echo
echo

curl -i -H "Content-Type: application/json"\
    -X POST -d "{\"username\":\"newuser\", \"password\":\"123\"}"\
     https://flaskimageupload.herokuapp.com/register

echo
echo "---Login with Credits---"
echo
echo

curl -i -H "Content-Type: application/json"\
     -X POST -d "{\"username\":\"newuser\", \"password\":\"123\"}"\
      https://flaskimageupload.herokuapp.com/login

