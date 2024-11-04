import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api';

export const signup = (password, email) => {
  return axios.post(`${API_URL}/register/`, { password, email });
};

export const login = (email, password) => {
  return axios.post(`${API_URL}/token/`, { email, password });
};
