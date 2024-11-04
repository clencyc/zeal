import axios from 'axios';

const signup = (password, email) => {
  axios.post('http://127.0.0.1:8000/api/register/', {
    password: password,
    email: email
  })
  .then(response => {
    console.log('User registered successfully', response.data);
  })
  .catch(error => {
    console.log('Error during registration', error.response.data);
  });
};
