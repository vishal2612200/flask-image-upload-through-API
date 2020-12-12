export jwt="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDczNDI2NTEsIm5iZiI6MTYwNzM0MjY1MSwianRpIjoiNWZkNTI3MGMtZjA0OS00OWJkLWE2ZjEtNjNiN2NhNDEzMGQ5IiwiZXhwIjoxNjA3MzQzNTUxLCJpZGVudGl0eSI6InZpc2hhbCIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.Zx1-S6XxCSGsaA3UgNYSgCYFI4VOwuHwMgzqpnCKNOI"

echo "------ Get list of users ------"
echo

curl -X GET \
  'http://localhost:5000/user' \
  -H "Authorization: Bearer $jwt" \


echo
echo "---Post image on API---"
echo
echo

curl -H "Authorization: Bearer $jwt"\
     --output -X POST http://localhost:5000/upload -F image=@1.png 

echo
echo "---Get all uploaded files names---"
echo
echo

curl -i -H "Authorization: Bearer $jwt" --output -X GET http://localhost:5000/files

