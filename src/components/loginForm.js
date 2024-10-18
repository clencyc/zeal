import { login } from '../api/auth';
import { saveToken } from '../utils/storage';

const handleLogin = (email, password) => {
  login(email, password)
    .then(response => {
      const token = response.data.access;
      saveToken(token);
      console.log('Login successful');
    })
    .catch(error => {
      console.log('Login failed', error.response.data);
    });
};

// You can export this function or use it directly in your app.
