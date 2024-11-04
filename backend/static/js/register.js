import axios from 'axios';

const login = (username, password) => {
    axios.post('http://127.0.0.1:8000/api/', {
      email: email,
      password: password
    })
    .then(response => {
      const accessToken = response.data.access; // Save the token locally
      localStorage.setItem('accessToken', accessToken); // Store token in local storage for later use
      console.log('Logged in successfully');
    })
    .catch(error => {
      console.log('Login failed', error.response.data);
    });
  };
  
